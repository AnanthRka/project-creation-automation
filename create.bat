@echo off
REM Save this batch file as create.bat in C:\Windows\System32\create.bat
REM Give full path of file below like C:\python\programs\automate_project.py
python path\to\python\file.py %1

REM Enter the drive short name which has your projects below like C: or S: 
drive_name:
REM Now give the path of the project folder like S:\Projects\Office_Projects
cd \Project\folder

REM This creates a folder with the name of the project you mentioned as arguments
mkdir %1
cd %1

REM creates an empty Readme file
echo $null >> README.md

REM Git commands
git init
git add README.md
git add .
git commit -m "First Commit"
git branch -M main
git remote add origin https://github.com/your_username/%1.git
git push -u origin main
code .