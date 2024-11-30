@echo off
:: Set the root directory explicitly
set ROOT_DIR=C:\Users\Bearach\mapping_project

:: Change to the correct drive and directory
cd /d %ROOT_DIR%

:: Generate the directory tree and save it to dirtree.txt
tree /F /A > "%ROOT_DIR%\documentation\dirtree.txt"

:: Inform the user where the directory tree has been saved
echo Directory tree has been generated and saved to %ROOT_DIR%\documentation\dirtree.txt

:: Pause to keep the window open
pause
