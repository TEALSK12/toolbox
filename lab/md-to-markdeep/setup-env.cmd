@echo off

if not exist tools (
    echo 1>&2Error: Run this command while in the md-to-markdeep directory.
    exit /b 1
)

path %cd%\tools;%path%
