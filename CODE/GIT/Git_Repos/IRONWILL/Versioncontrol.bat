@echo off
rem setlocal EnableDelayedExpansion

rem set "result="
rem for /f "delims=" %%a in ('dir /A:D') do set "result=!result!%%a
rem "

rem echo !result!

setlocal EnableDelayedExpansion
set "output="
for /f "delims=" %%a in ('dir /A:D') do set "output=!output!%%a^
"
echo !output!
