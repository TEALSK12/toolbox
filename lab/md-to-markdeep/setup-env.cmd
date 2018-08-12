@echo off

REM -- Add the md-to-markdeep/tools director to the execution path.

path | findstr >nul -i md-to-markdeep/tools
if %errorlevel% equ 0 goto :setupCurriculumDir
echo Setting up path.
if not exist tools (
    echo 1>&2Error: Run this command while in the md-to-markdeep directory.
    exit /b 1
)

path %cd%\tools;%path%

REM -- Aet the APCSA_CURRICULUM environment variable to point to the APCSA curriculum source.

:setupCurriculumDir
if defined APCSA_CURRICULUM goto :foundCurriculum

set APCSA_CURRICULUM=..\..\..\apcsa-instructor\apcsa-public\curriculum

if exist %APCSA_CURRICULUM% goto :foundCurriculumDirectory
set APCSA_CURRICULUM=
echo 1>&2Error: APCSA_CURRICULUM is not defined, and apcsa-public not found via expected path.
exit /b 1

:foundCurriculumDirectory
pushd %APCSA_CURRICULUM%
    set APCSA_CURRICULUM=%CD%
popd

:foundCurriculum
echo APCSA_CURRICULUM = %APCSA_CURRICULUM%

exit /b 0
