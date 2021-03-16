#!/usr/bin/env python
""" Ingest edit.json and export bat and txt files to concact a directory to mp4 videos.
Will create 2 .bat files to run to start the merging of videos. This is just to create those files.
Usage:
Example:  RunMainProcess("M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/py/editjson.json", "M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/out/01","VTBITCY2101H", "M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/PB-01_01C_1.wav" )
Example:  RunMainProcess(editjsonpath, outputfolder," projectname, audiofile )

Appropriate %editjsonpath% must include: example: {"Clips":[{"Description": "", "Marker Name": "SC07_SHOT01", "Marker Type": "Comment", "In": "00:00:13:17", "Out": "00:00:14:23", "Frames": "30", "Duration": "00:00:01:06", "FrameRange": "1000:1030"}]}

Appropriate %ShotID% must be: %SceneName%_%ShotNumber% | SC02_SHOT01

Appropriate directories in %outputfolder% must follow:
%outputfolder%/%ShotID%/eevee/%ShotID%_eevee_.mp4 | /01/SC02_SHOT01/eevee/SC02_SHOT01_eevee_mp4
%outputfolder%/%ShotID%/pb/%ShotID%_pb_.mp4 | /01/SC02_SHOT01/pb/SC02_SHOT01_pb_mp4

Files are saved to:
%outputfolder%/pipeline
%outputfolder%/pipeline/pipeline/ffmpegconcat_eevee.txt | Files to merge into video that exist
%outputfolder%/pipeline/pipeline/ffmpegconcat_pb.txt | Files to merge into video that exist
%outputfolder%/pipeline/pipeline/ffmpegconcat_eevee.bat | Small app to just double click to run. Will export 2 video files, %outputfolder%/%ProjectName%_eevee_edit_%date%_nosound.mp4 & %ProjectName%_eevee_edit_%date%_sound.mp4 
%outputfolder%/pipeline/pipeline/ffmpegconcat_pb.bat | Small app to just double click to run. Will export 2 video files, %outputfolder%/%ProjectName%_pb_edit_%date%_nosound.mp4 & %ProjectName%_pb_edit_%date%_sound.mp4 

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Justin Jaro"
__authors__ = ["Justin Jaro"]
__contact__ = "info@vltmedia.com"
__copyright__ = "Copyright 2021, VLT Media LLC"
__credits__ = ["Justin Jaro"]
__date__ = "2021/03/14"
__deprecated__ = False
__email__ =  "info@vltmedia.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"


import json
import os
from datetime import datetime
now = datetime.now() # current date and time
date_time = "_"+now.strftime("%Y%m%d%H%M%S")+"_"

def LoadJSON(filepath):
    with open(filepath) as f:
        data = json.load(f)
        f.close()
    return data
    # Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
def GetDirectories(dirpath):
    folder_paths = []
    for entry_name in os.listdir(dirpath):
        entry_path = os.path.join(dirpath, entry_name)
        if os.path.isdir(entry_path):
            folder_paths.append([entry_path,os.path.basename(entry_path)])
    return folder_paths
def CleanNames(foldersarray):
    names = []
    for f in foldersarray:
        names.append(f[1])
        
    return(names)

def CleanEditShotIDS(editjson):
    names = []
    for f in editjson["Clips"]:
        names.append(f["Marker Name"])
        
    return(names)


def GetRenderIDS(editjson, foldernamesarray, exportdirectory):
    names = {"Clips" : []}
    for f in foldernamesarray:
        if f in editjson:
            newclip = {}
            newclip["ShotID"] = f
            newclip["VidFileEevee"] = exportdirectory + "/" +f+ "/eevee/" + f + "_eevee_.mp4"
            newclip["VidFilePB"] = exportdirectory + "/" +f+ "/pb/" + f + "_pb_.mp4"
            names["Clips"].append(newclip)
        
    return(names)


def CreateFFMPEGConcat(RenderIDSJson, exportdirectory, ProjectName, audioFile):
    eeveefiles = []
    eeveefilepath = exportdirectory + "/pipeline/ffmpegconcat_eevee.txt"
    eeveeconcactbatch = "ffmpeg -f concat -safe 0 -i \"" +eeveefilepath + "\" -c copy \"" + exportdirectory +"/" + ProjectName+ "_eevee_edit"+date_time+"nosound.mp4\" -y"
    eeveeconcactbatchsound = "ffmpeg -i \"" + exportdirectory +"/" + ProjectName+ "_eevee_edit"+date_time+"nosound.mp4\""+" -i \"" +audioFile+   "\" -map 0:v -map 1:a -c:v copy -shortest \"" + exportdirectory +"/" + ProjectName+ "_eevee_edit"+date_time+"sound.mp4\" -y"
    eeveeconcactbatchfilepath = exportdirectory + "/pipeline/ffmpegconcat_eevee.bat"
    for f in RenderIDSJson["Clips"]:
        if os.path.exists(f["VidFileEevee"]):
            eeveefiles.append("file 'file:"+f["VidFileEevee"] + "'")
        
        
        
        
        # eeveefiles.append("ffmpeg -f concat -safe 0 -i /""+f["VidFileEevee"] + "/" -c copy /"" + ProjectName+ "_edit.mp4/"")
        
    
    pbfiles = []
    pbfilepath = exportdirectory + "/pipeline/ffmpegconcat_pb.txt"
    pbconcactbatch = "ffmpeg -f concat -safe 0 -i \"" +pbfilepath + "\" -c copy \"" + exportdirectory +"/" + ProjectName+ "_pb_edit"+date_time+"nosound.mp4\" -y"
    pbconcactbatchsound = "ffmpeg -i \"" + exportdirectory +"/" + ProjectName+ "_pb_edit"+date_time+"nosound.mp4\""+" -i \"" +audioFile+   "\" -map 0:v -map 1:a -c:v copy -shortest \"" + exportdirectory +"/" + ProjectName+ "_pb_edit"+date_time+"sound.mp4\" -y"
    
    pbconcactbatchfilepath = exportdirectory + "/pipeline/ffmpegconcat_pb.bat"
    
    if not os.path.exists(exportdirectory + "/pipeline"):
        os.makedirs(exportdirectory + "/pipeline")
    
    for f in RenderIDSJson["Clips"]:
        if os.path.exists(f["VidFilePB"]):
            pbfiles.append("file 'file:"+f["VidFilePB"] + "'")
        
        
        
        
        # eeveefiles.append("ffmpeg -f concat -safe 0 -i /""+f["VidFileEevee"] + "/" -c copy /"" + ProjectName+ "_edit.mp4/"")
        
        
    with open(eeveefilepath, 'w') as filehandle:
        
        filehandle.writelines("%s\n" % place for place in eeveefiles)
        filehandle.close()
        
    with open(pbfilepath, 'w') as filehandle:
        
        filehandle.writelines("%s\n" % place for place in pbfiles)
        filehandle.close()
        
    with open(eeveeconcactbatchfilepath, 'w') as filehandle:
        
        filehandle.write(eeveeconcactbatch)
        filehandle.write("\n")
        
        filehandle.write(eeveeconcactbatchsound)
        filehandle.close()
                
    with open(pbconcactbatchfilepath, 'w') as filehandle:
        
        filehandle.write(pbconcactbatch)
        filehandle.write("\n")
        filehandle.write(pbconcactbatchsound)
        filehandle.close()
        
        
        
    print("Saved to : ", eeveefilepath)
    

def RunMainProcess(editjsonpath, exportdirectory, ProjectName, audioFile):
    editjson = LoadJSON(editjsonpath)
    foldersarray = GetDirectories(exportdirectory)
    foldernamesarray = CleanNames(foldersarray)
    editjsonarray = CleanEditShotIDS(editjson)
    RenderIdsJSON = GetRenderIDS(editjsonarray, foldernamesarray, exportdirectory)
    CreateFFMPEGConcat(RenderIdsJSON, exportdirectory,ProjectName, audioFile)
    print(RenderIdsJSON)
    
    
if __name__ == '__main__':
    print("Nope")
    # RunMainProcess("M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/py/editjson.json", "M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/out/01","VTBITCY2101H", "M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/PB-01_01C_1.wav" )