@echo off & setlocal

if not defined APCSA_CURRICULUM (
    echo 1>&2Error: APCSA_CURRICULUM undefined. Did you forget to run `setup-env.cmd`?
    exit /b 1
)

mkdir >nul out
robocopy /mir %APCSA_CURRICULUM% out
