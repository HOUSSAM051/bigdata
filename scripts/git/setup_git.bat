@echo off
rem =============================================
rem Git setup script for the "fintched bigdata" project
rem =============================================

rem Change directory to the project root (one level up from this script)
cd ..\..

rem Initialize a new Git repository if none exists
if not exist .git (
    git init
) else (
@echo off
rem =============================================
rem Git setup script for the "fintched bigdata" project
rem =============================================

rem Change directory to the project root (one level up from this script)
cd ..\..

rem Initialize a new Git repository if none exists
if not exist .git (
    git init
) else (
    echo Git repository already initialized.
)

rem Add all files to staging
git add .

rem Create initial commit if repository has no commits
git rev-parse --verify HEAD >nul 2>&1
if errorlevel 1 (
    rem No commits yet, create initial commit
    git commit -m "Initial commit"
) else (
    rem Repository already has commits, commit any changes
    git diff-index --quiet HEAD || git commit -m "Update"
)

rem Ensure the main branch is named "main"
git branch -M main

rem Add remote origin (replace URL if different)
git remote remove origin >nul 2>&1
git remote add origin https://github.com/HOUSSAM051/bigdata.git

rem Push to remote repository
git push -u origin main
git push -u origin main

echo Git setup complete.
pause
