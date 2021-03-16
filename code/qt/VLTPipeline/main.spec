# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['D:\\Projects\\Apps\\VLTPipeline\\code\\qt\\VLTPipeline'],
             binaries=[("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/form.ui","."), ("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/LoadProjects.ui","."),("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/loadProjectsWindow.ui","."), ("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/setBlendFiles.ui",".")],
             datas=[("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/form.ui","."), ("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/LoadProjects.ui","."),("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/loadProjectsWindow.ui","."), ("D:/Projects/Apps/VLTPipeline/code/qt/VLTPipeline/setBlendFiles.ui",".")],
             hiddenimports=['PySide2.QtXml'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
