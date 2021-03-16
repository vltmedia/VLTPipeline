#blender --background test.blend --python mytest.py -- example args 123
import os


def RunProcess(blendfile, scriptfile, args):
    argument = "blender --background \""+blendfile+"\" --python \""+scriptfile+"\" -- \""+args+"\""
    print(argument)
    os.system('cmd /c "'+argument+'"')

if __name__ == '__main__':
    print("Mainyoto")

