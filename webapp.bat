@echo off
set "PYTHON_DIR=C:\Python38_64"
rem set "PYTHON_BIN=%PYTHON_DIR%\python.exe"
set "PYTHON_BIN=python.exe"

echo.--- run webapp.py
"%PYTHON_BIN%" %~dp0/src/webapp.py
