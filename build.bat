@echo off
set "PYTHON_DIR=C:\Program Files (x86)\Python36-32"
set "PYTHON_BIN=%PYTHON_DIR%\python.exe"
set "PYARMOR_BIN=%PYTHON_DIR%\Scripts\pyarmor.exe"
set "PYINSTALLER_BIN=%PYTHON_DIR%\Scripts\pyinstaller.exe"
set "NUITKA_BIN=%PYTHON_DIR%\python.exe -m nuitka"
set "ROOT_DIR=D:\workspaces\PetersDashboard"

echo.--- install python packages
"%PYTHON_DIR%\Scripts\pip3.exe" install soco
if %errorlevel% neq 0 exit /b

"%PYTHON_BIN%" ./src/play.py
if %errorlevel% neq 0 exit /b

exit /b

rem echo.--- remove old distribution
rem if exist "%ROOT_DIR%\build" rmdir /s /q "%ROOT_DIR%\build"

echo.--- move to build folder
if not exist "%ROOT_DIR%\build" mkdir build
cd build
if %errorlevel% neq 0 exit /b

echo.--- show hardware info
rem %PYTHON_BIN% -OO -m py_compile %ROOT_DIR%\src\dashboard.py
set PYTHONOPTIMIZE=2
%PYARMOR_BIN% hdinfo
if %errorlevel% neq 0 exit /b

echo.--- create licenses
%PYARMOR_BIN% licenses --bind-disk "ACE4_2E00_9007_3C9D" --bind-mac "3c:2c:30:d0:cb:37" code-iccaunb065
%PYARMOR_BIN% licenses --bind-mac "3c:2c:30:d0:cb:37" code-raspberry
if %errorlevel% neq 0 exit /b

echo.--- show available plattform names
%PYARMOR_BIN% download --list

echo.--- obfuscate packages
rem set "PYARMOR_OPTS=--recursive --platform windows.x86_64 --with-license licenses/code-iccaunb065/license.lic"
rem set "PYARMOR_OPTS=--platform windows.x86_64 --with-license licenses/code-iccaunb065/license.lic"
set "PYARMOR_OPTS=--platform linux.armv7 --platform windows.x86_64 --with-license licenses/code-iccaunb065/license.lic"
%PYARMOR_BIN% init --src %ROOT_DIR%\src\Tools --entry __init__.py Tools
%PYARMOR_BIN% build --output dist --only-runtime %PYARMOR_OPTS% Tools
%PYARMOR_BIN% build --output dist --no-runtime %PYARMOR_OPTS% Tools
if %errorlevel% neq 0 exit /b

echo.--- obfuscate application
%PYARMOR_BIN% obfuscate --output dist %PYARMOR_OPTS% %ROOT_DIR%\src\dashboard.py
if %errorlevel% neq 0 exit /b

echo.--- bundles the application
tar -vczf package.tgz -C dist *.*
if %errorlevel% neq 0 exit /b

echo.--- build executable
set "PATH_OLD=%PATH%"
set "PATH=%PATH%;C:\MinGW64\mingw64\bin;"
set "CCACHE_CONFIGPATH=%ROOT_DIR%\ccache.conf"
set "NUITKA_OPTS=--output-dir=. --jobs=1 --mingw64"
rem set "NUITKA_OPTS=%NUITKA_OPTS% --generate-c-only"
rem set "NUITKA_OPTS=%NUITKA_OPTS% --recompile-c-only"
set "NUITKA_OPTS=%NUITKA_OPTS% --follow-imports"
rem set "NUITKA_OPTS=%NUITKA_OPTS% --include-plugin-directory=C:\Python38_64\lib\site-packages\pynput"
rem set "NUITKA_OPTS=%NUITKA_OPTS% --include-plugin-directory=C:\Python38_64\Lib\site-packages\numpy"
set "NUITKA_OPTS=%NUITKA_OPTS% --include-module=pynput"
rem set "NUITKA_OPTS=%NUITKA_OPTS% --include-module=numpy"
set "NUITKA_OPTS=%NUITKA_OPTS% --plugin-enable=pylint-warnings --plugin-enable=numpy"
set "NUITKA_OPTS=%NUITKA_OPTS% --show-progress --show-scons --show-modules"
set "NUITKA_OPTS=%NUITKA_OPTS% --standalone --windows-dependency-tool=pefile --experimental=use_pefile_recurse"
%NUITKA_BIN% %NUITKA_OPTS% %ROOT_DIR%\src\test.py
if %errorlevel% neq 0 exit /b
test.dist\test.exe
if %errorlevel% neq 0 exit /b
%NUITKA_BIN% %NUITKA_OPTS% %ROOT_DIR%\src\dashboard.py
if %errorlevel% neq 0 exit /b
dashboard.dist\dashboard.exe
if %errorlevel% neq 0 exit /b
set "PATH=%PATH_OLD%"

echo.--- done
cd ..
exit /b
