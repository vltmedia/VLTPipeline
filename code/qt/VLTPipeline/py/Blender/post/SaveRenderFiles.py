#Use this script in Blender 2.8 +  with arguments sceneoutputfolder 


import bpy
import os
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"
argv = [f.split(",") for f in argv][0]
print("````````````````````````````````````````````````````````````````")
print(argv)
print("````````````````````````````````````````````````````````````````")

path = bpy.data.filepath
dirname = os.path.dirname(path) 
bigpath =os.path.abspath(os.path.join(dirname, os.pardir))
dirname = bigpath
basename = os.path.basename(path)
basenameBlend = basename.split(".blend")[0]
namesplit = basenameBlend.split("_")
basenamenoversion = ""
for i in range(0, 2):
    newname = basenamenoversion +"_"+ namesplit[i]
    
    if i == 0:
        newname = basenamenoversion + namesplit[i]
        
    basenamenoversion = newname
Version = namesplit[2]


scenefolder = argv[0] + "\\" +Version+ "\\" + basenamenoversion+ "\\" 
eeveeblend = scenefolder + basenamenoversion + "_eevee.blend"
pbblend = scenefolder + basenamenoversion + "_pb.blend"

# eeveeblend = dirname + "\\" + basenamenoversion + "_eevee.blend"
# pbblend = dirname + "\\" + basenamenoversion + "_pb.blend"

outbatpb =  argv[0] + "\\pipeline\\batchexportpb.bat"
outbateevee =  argv[0] + "\\pipeline\\batchexporteevee.bat"
outfoldereevee = scenefolder + "eevee\\"
outfoldereeveeFilepath = scenefolder + "eevee\\" + basenamenoversion + "_eevee_"
outfolderpb = scenefolder  + "\\pb\\"
outfolderpbFilepath = scenefolder+ "pb\\" + basenamenoversion + "_pb_"

print("`````````````````dirname````````````````````````")
print(eeveeblend)

print("`````````````````````````````````````````")
print("````````````````outfoldereevee`````````````````````````")
print(outfoldereevee)

print("`````````````````````````````````````````")


print("`````````````````dirname````````````````````````")
print(pbblend)

print("`````````````````````````````````````````")
print("````````````````outfoldereevee`````````````````````````")
print(outfolderpb)

print("`````````````````````````````````````````")




def UpdateBatFiles():
    
    # Append-adds at last 
    # append mode 
    # if argv[1] == "clear":
    #     file1 = open(outbatpb, "w")  
    #     file1.write("\n") 
        
    #     file1.close()
    #     file1 = open(outbateevee, "w")  
    #     file1.write("\n") 
        
    #     file1.close()
    file1 = open(outbatpb, "a")   

    # writing newline character 
    file1.write("\n") 
    # Write Blender Line
    file1.write('blender -b "'+pbblend+'" -a ') 

    file1.write("\n") 
    #Write FFMPEG
    file1.write('ffmpeg -start_number 1000 -r 24 -f image2 -s 1920x1080 -i "'+outfolderpbFilepath+'%%04d.png" -vcodec libx264 -crf 25  -pix_fmt yuv420p "'+outfolderpbFilepath+'.mp4"') 
    file1.close()
    
    file1 = open(outbateevee, "a")   

    # writing newline character 
    file1.write("\n") 
    # Write Blender Line
    file1.write('blender -b "'+eeveeblend+'" -a ') 

    file1.write("\n") 
    #Write FFMPEG
    file1.write('ffmpeg -start_number 1000 -r 24 -f image2 -s 1920x1080 -i "'+outfoldereeveeFilepath+'%%04d.png" -vcodec libx264 -crf 25  -pix_fmt yuv420p "'+outfoldereeveeFilepath+'.mp4"') 
    
    file1.close()


# Make Output Folders
def MakeOutputFolders():
    if os.path.exists(outfoldereevee) == False:
        os.makedirs(outfoldereevee)
    if os.path.exists(outfolderpb) == False:
        os.makedirs(outfolderpb)

def SaveEeveeBlender():
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'

    bpy.context.scene.render.filepath = outfoldereeveeFilepath
    
    bpy.ops.wm.save_as_mainfile(filepath=eeveeblend)
    print("Saved Eevee Blend File: " + outfoldereeveeFilepath)
    
    

def SaveWorkBenchBlender():
    
    bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
    bpy.data.scenes['Scene'].display.shading.color_type = 'TEXTURE'
    bpy.data.scenes['Scene'].display.shading.show_cavity = True
    bpy.data.scenes['Scene'].display.shading.light = 'MATCAP'
    bpy.data.scenes['Scene'].display.shading.studio_light = 'basic_side.exr'


    bpy.context.scene.render.filepath = outfolderpbFilepath
    
    bpy.ops.wm.save_as_mainfile(filepath=pbblend)
    print("Saved WorkBench Blend File: " + outfolderpbFilepath)
    
    
MakeOutputFolders()
SaveEeveeBlender()
SaveWorkBenchBlender()
UpdateBatFiles()


print("Done!")