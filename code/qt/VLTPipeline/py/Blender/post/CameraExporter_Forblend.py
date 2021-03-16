import bpy
import os
import sys

# blender --background "M:\Projects\VT\VTBITCY01\01-Working\28-JJ\04-3D\Test\SC04_Shot01\SC04_Shot01_01.blend" --python "D:\Projects\Apps\VLTPipeline\code\qt\VLTPipeline\py\Blender\post\CameraExporter.py" -- "M:\Projects\VT\VTBITCY01\01-Working\28-JJ\04-3D\Test\out\01\SC04_Shot01",ExportAll
# blender --background "blendfile" --python "scriptfile" -- Outputfolder,ExportAll
# Arguments -- Outputfolder,ExportAll
# Arguments -- D:/Sanic/01/SC01_Shot01,True
basedir = ""
ExportAll = "ExportAll"
try:
    argv = sys.argv
    argv = argv[argv.index("--") + 1:]  # get all args after "--"
    argv = [f.split(",") for f in argv][0]  # split by ","

    # output blend file folder location 
    basedir =  argv[0]
    ExportAll =  argv[1]
    
except :
    
    basedir = "M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Test/out/01/SC02_SHOT01"
    ExportAll = "ExportAll"
    
# whether to export all cameras or not. True, False
#ExportAll =  argv[1]
class CameraExporter():
    
    def __init__(self, outputfolder):
        super().__init__()
        self.basedir = outputfolder
        if not os.path.exists(outputfolder):
            os.makedirs(outputfolder)
        self.cameras = []
    

    def GetParent(self, obj):
        lastparent = []
        if obj.hide_viewport:
            obj.hide_viewport = False # toggle to test visibility
        print("par | ", obj.parent)
        if obj.parent != None:
            print("B | ", obj.parent)
            
            lastparent.append(self.GetParent(obj.parent))
            return lastparent
        else:
            return obj

    def GetCleanedName(self, obj):
        lastparent = self.GetParent(obj)
        print(lastparent)
        lastparentname = ""
        try:
            lastparentname = lastparent[0][0].name
        except :
            try:
                lastparentname = lastparent[0].name
            except :
                lastparentname = lastparent.name
    
        namesplit = [lastparentname]
        nameout = lastparentname
        if "." in lastparentname:
            namesplit = lastparentname.split(".")
            nameout = "_".join(namesplit[i] for i in range(len(namesplit)))
        return nameout

    def BakeKeyframesOfObject(self, obj):
        # obj.select_set(True)
        
        try:
            bpy.ops.object.select_all(action='DESELECT')
            obj.select_set(True)
            
            # try:
            # obj.select_set(True)
            # except :
            #     print("Failed Selecting")
            #bpy.ops.nla.bake(visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'OBJECT'})
            bpy.ops.nla.bake(frame_start=bpy.context.scene.frame_start, frame_end=bpy.context.scene.frame_end, visual_keying=True, clear_constraints=True, clear_parents=True, bake_types={'OBJECT'})
            return True
        except :
            print("Failed Selecting")
            
            return False
    def ExportFBXFile(self, obj):
        name = bpy.path.clean_name(obj.name)
        camerasfolder = os.path.join(self.basedir, "cameras/" + name)
        if not os.path.exists(camerasfolder):
            os.makedirs(camerasfolder)
        bpy.ops.object.select_all(action='DESELECT')
        obj.select_set(True)    
        fn = os.path.join(camerasfolder, name)
        print(name)
        bpy.ops.export_scene.fbx(filepath=fn + ".fbx", use_selection=True)
        print("Successfully Wrote FBX File | ", fn + ".fbx")
        bpy.ops.wm.alembic_export(filepath=fn + ".abc", selected=True, renderable_only=False, visible_objects_only=False,start=bpy.context.scene.frame_start, end=bpy.context.scene.frame_end)
        print("Successfully Wrote Alembic File | ", fn + ".abc")
        
        
    def ExportObject(self,obj):
        self.objectname = self.GetCleanedName(obj)
        obj.name = self.objectname
        if self.BakeKeyframesOfObject(obj) == True:
            print("Exporting Cam | " , obj)
            self.ExportFBXFile(obj)
        else:
            print("``````````````````````````````````````````")
            print("Not in Viewlayer | ", self.objectname)
            print("``````````````````````````````````````````")

    def ExportAllCameras(self):
        self.SelectCameras()
        self.ExportCameras()
            
    def ExportCameras(self):
        count = 0
        for cam in self.cameras:
            
            print("Exporting Camera " + str(count) +"/" + str(len(self.cameras) - 1))
            self.ExportObject(cam)
            newcount = count + 1
            count = newcount
    
    def SelectCameras(self):
        for ob in bpy.data.objects:
            if ob.type == 'CAMERA':
                if ob.hide_get() == 0:
                    self.cameras.append(ob)
    
if __name__ == '__main__':
    cameraExporter = CameraExporter(basedir)
    cameraExporter.ExportAllCameras()
    # print("```````````````````````````````````````")
    # print(cameraExporter.cameras)
    # print(cameraExporter.basedir)
    # print("```````````````````````````````````````")
    
    # cameraExporter.ExportObject(bpy.context.object)