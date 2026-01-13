@echo off
:: Run this script in a shell where `git` is available (Developer PowerShell or Git Bash)
:: It stages and commits all workspace changes with a sensible message.

git add -A
git commit -m "Fix: Add DLL loader helpers and build/test scripts; ensure custom_rasterizer imports in dev env"
if %ERRORLEVEL% neq 0 (
  echo "Git commit failed; inspect 'git status' and run the commands manually."
)
