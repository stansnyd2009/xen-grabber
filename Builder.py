@echo off
cd /d %~dp0
call Data\Requirements.bat
if not %errorlevel%==0 (
    color 4 && title Error
    pause > NUL
)