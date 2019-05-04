.@echo off&setlocal enableDelayedExpansion
set "r=1.txt"
for /f "tokens=2 delims=:" %%a in ('find /c /v "" "%r%"') do set m=%%a
for /l %%a in (1,1,%m:~1%) do set #!random!!random!!random!==%%a
for /f "tokens=2 delims==#" %%a in ('set #') do call:n %%a
exit
:n
if %1==%m:~1% (set n=) else set "n=skip=%1 "
for /f "%n%tokens=1* delims=:" %%a in ('findstr /n .* "%r%"') do (
>>temp.txt echo;%%b
goto:eof