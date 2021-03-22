set /p uifile=UI File Path: 
set /p pythonoutputname=Python Output File Path: 

set batdir=%~dp0

"%batdir%pyside2-uic.exe" "%uifile%" > "%pythonoutputname%"

echo "Finished converting the UI File."

pause
@REM pyside2-uic.exe