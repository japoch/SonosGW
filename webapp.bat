@echo off
set "PYTHON_DIR=C:\Python38_64"
set "PYTHON_BIN=%PYTHON_DIR%\python.exe"

echo.--- run play.py
"%PYTHON_BIN%" %~dp0/submodules/SoCo/examples/webapp/index.py
