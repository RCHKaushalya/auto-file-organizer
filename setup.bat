@echo off
title File Organizer Test Setup
echo Creating test environment...

:: 1. Create the test directory
set "folderName=OrganizeMe_Test"
if not exist %folderName% mkdir %folderName%
cd %folderName%

echo Generating dummy files...

:: --- Images ---
type nul > photo.jpg
type nul > background.png
type nul > meme.gif

:: --- Documents ---
type nul > manual.pdf
type nul > notes.txt
type nul > spreadsheet.xlsx
type nul > report.docx

:: --- Audio ---
type nul > song.mp3
type nul > recording.wav
type nul > track.aac

:: --- Videos ---
type nul > movie.mp4
type nul > clip.avi
type nul > tutorial.mkv

:: --- Archives ---
type nul > backup.zip
type nul > project.rar
type nul > source.tar.gz

:: --- Applications ---
type nul > installer.exe
type nul > mac_app.dmg
type nul > linux_pkg.deb

:: --- Code ---
type nul > script.py
type nul > website.html
type nul > styles.css
type nul > logic.js
type nul > program.cpp

:: --- Duplicate Test (To test your get_unique_filename function) ---
:: Note: Create a folder first, then a file with the same name outside 
:: so you can test if the script renames it when moving.
mkdir Images
type nul > photo.jpg

:: --- Unsorted/Unknown ---
type nul > mysterious_file.unknown
type nul > no_extension_file

echo.
echo ======================================================
echo Setup Complete! 
echo Folder created: %CD%
echo ======================================================
echo.
echo Now run your Python script and paste the path above.
pause