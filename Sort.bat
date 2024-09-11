@echo off
if "%~1"=="" (
    echo Drag and drop a text file onto this script to sort numbers.
    pause
    exit /b
)

set "inputFile=%~1"
if not exist "%inputFile%" (
    echo File "%inputFile%" does not exist.
    pause
    exit /b
)

powershell -command "(Get-Content '%inputFile%' | ForEach-Object {[decimal]$_} | Sort-Object) | ForEach-Object { $_.ToString('F0') } | Set-Content '%inputFile%'"

echo Numbers in "%inputFile%" have been sorted.
pause