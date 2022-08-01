@echo off

start

"%PYTHONPATH% = "C:/Program Files/Blender Foundation/Blender/2.80/python/bin/"

python ./get-pip.py

start %PYTHONPATH%python.exe -m pip install PySide2

pause

exit