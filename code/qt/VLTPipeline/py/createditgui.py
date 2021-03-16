from createeditbat import CreateEditJSON
from createffmpegeditfiles import LoadJSON
from pipelineclasses import Project
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import csv
import json
MainProject = Project()
scriptloc = os.path.dirname(__file__) + "/" +os.path.basename(__file__)
dirname  = os.path.dirname(__file__)+ "/"
outjsonpath = dirname + "editjson.json"
Loaded = MainProject.FromIni(dirname + "project.ini")
# create the root window
root = tk.Tk()
root.title('Create Edit Files')
root.resizable(False, False)
root.geometry('300x150')

csvfile = ""
audiofile = ""
outputfolderpath = ""

def LoadProjectInfo():
    global MainProject
    MainProject.FromIni(dirname + "project.ini")
    print(MainProject.AudioFile)

def getFolderPath():
    global outputfolderpath
    global outjsonpath
    global MainProject
    folder_selected = fd.askdirectory(title='Select Output Folder Path')
    outputfolderpath=folder_selected
    outjsonpath = outputfolderpath + "/pipeline/" + "editjson.json"
    MainProject.OutputPathPipleline =  outputfolderpath + "/pipeline/" + "project.ini"
    
    # try:
    #     if not os.path.exists(outputfolderpath + "/pipeline")
    #         os.makedirs(outputfolderpath + "/pipeline")
    # except :
    #     print("Failed making Pipeline Dir")
    
def select_file():
    filetypes = (
        ('Edit CSV', '*.csv'),
        ('Premiere Markers CSV', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Select an Edit CSV File',
        initialdir='/',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )
    global csvfile
    csvfile = filename
    UpdateProjectClass()
    
def select_audio_file():
    filetypes = (
        ('Audio file', '*.wav'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Select an Audio File',
        initialdir='/',
        filetypes=filetypes)

    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )
    global audiofile
    audiofile = filename
    UpdateProjectClass()
    
def CreateEditJSONFile():
    jsonpath = outjsonpath
    
    CreateEditJSON(csvfile, 'utf-16', outjsonpath )
    showinfo(
        title='Success!',
        message="Successfully created the Edit JSON File! : " + outjsonpath
    )
    
def UpdateProjectClass():
    global MainProject
    
    MainProject.UpdateProject("VTBITCY2101H", "01", audiofile, outputfolderpath, outjsonpath, csvfile)
    

def CheckCSVFile():
    global MainProject
    outputpath = dirname +"/project.ini"
    outpipelineprojpath = outputfolderpath + "/pipeline/" + "project.ini"
    UpdateProjectClass()
    # MainProject.UpdateProject("VTBITCY2101H", "01", audiofile, outputfolderpath, outjsonpath, csvfile)
    # MainProject.OutputPathPipleline = outpipelineprojpath
    MainProject.CreateConfig(outputpath)
    print(csvfile)
    print(outputfolderpath)

# open button
open_button = ttk.Button(
    root,
    text='Select Edit CSV File',
    command=select_file
)

open_button.pack(expand=True)


# open button
selectaudio_button = ttk.Button(
    root,
    text='Select Backing Audio File',
    command=select_audio_file
)

selectaudio_button.pack(expand=True)



# open button
outputfolderpath_button = ttk.Button(
    root,
    text='Set Output Folder Path',
    command=getFolderPath
)

outputfolderpath_button.pack(expand=True)


# open button
CreateEditFiles_button = ttk.Button(
    root,
    text='Create Edit JSON File',
    command=CreateEditJSONFile
)

CreateEditFiles_button.pack(expand=True)


# open button
checkcsvfile_button = ttk.Button(
    root,
    text='Check CSV File',
    command=CheckCSVFile
)

checkcsvfile_button.pack(expand=True)


LoadProjectInfo()
# run the application
root.mainloop()