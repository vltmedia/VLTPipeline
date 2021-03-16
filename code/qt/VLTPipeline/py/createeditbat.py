import os
import csv
import json
scriptloc = os.path.dirname(__file__) + "/" +os.path.basename(__file__)
dirname  = os.path.dirname(__file__)+ "/"
outjsonpath = dirname + "editjson.json"
keys = []
Json ={}
def CreateEditJSON(filepath, encoding, output_file):
    # with open('M:/Projects/VT/VTBITCY01/01-Working/28-JJ/04-3D/Scene/out/01/edit.csv', newline='', encoding='utf-16') as csvfile:
    with open(filepath, newline='', encoding=encoding) as csvfile:
        editCSV = csv.reader(csvfile, delimiter=',', quotechar='"')
        count = 0
        js = {"Clips" : []}
        for row in editCSV:
            if count == 0:
                keys=row
            else :
                jss = {}
                valc = 0
                for val in row:
                    jss[keys[valc]] = val
                    newv = valc + 1
                    valc = newv
                js["Clips"].append(jss)
                    
            newc = count + 1
            count = newc
            # print(', '.join(editCSV[row]))

        Json = js

    with open(output_file, 'w') as json_file:
        json.dump(Json, json_file)


    print(keys)
    print(Json)
    print('basename:    ', scriptloc)
