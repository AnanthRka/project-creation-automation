@echo off
REM Save this batch file as create.bat in C:\Windows\System32\create.bat
REM Give full path of file below like C:\python\programs\automate_project.py
python path\to\file\automate.py %1

REM Now give the path of the project folder like S:\Projects\Office_Projects
pushd drive\project\folder

REM This creates a folder with the name of the project you mentioned as arguments
mkdir %1
cd %1

REM creates an empty Readme file
echo Readme file for project %1. >> README.md

REM Git commands
git init
git add README.md
git add .
git commit -m "First Commit"
git branch -M main
git remote add origin https://github.com/your_username/%1.git
git push -u origin main
code .