@echo off
setlocal EnableDelayedExpansion
title UltraWide Desert - Widescreen Camera Mod
color 0F
mode con cols=72 lines=55

set "SD=%~dp0"
set "VER=1.0"

:: Verify we're not running from inside a zip
if not exist "%SD%lib\camera_mod.py" (
    echo.
    echo   ERROR: Cannot find mod files.
    echo   Right-click the zip and choose "Extract All" first.
    echo   Do NOT run from inside the zip file.
    echo.
    pause
    exit /b
)

:: ============================================================
:: PYTHON CHECK
:: ============================================================
set "PYTHON="

where py >nul 2>nul
if errorlevel 1 goto TRY_PYTHON
for /f "delims=" %%V in ('py -3 --version 2^>nul') do set "_PV=%%V"
if not defined _PV goto TRY_PYTHON
set "PYTHON=py -3"
goto PYTHON_OK

:TRY_PYTHON
where python >nul 2>nul
if errorlevel 1 goto NO_PYTHON
for /f "delims=" %%V in ('python --version 2^>nul') do set "_PV=%%V"
if not defined _PV goto NO_PYTHON
set "PYTHON=python"
goto PYTHON_OK

:NO_PYTHON
cls
echo.
echo   ============================================================
echo.
echo    ERROR: Python 3 is not installed or not in PATH.
echo.
echo    Please install Python 3.10 or newer from:
echo    https://www.python.org/downloads/
echo.
echo    IMPORTANT: Check "Add python.exe to PATH" during install.
echo.
echo   ============================================================
echo.
pause
exit /b

:PYTHON_OK

:: Check required packages (uses pip show to avoid -c flag AV false positives)
!PYTHON! -m pip show cryptography >nul 2>nul
if errorlevel 1 goto INSTALL_DEPS
!PYTHON! -m pip show lz4 >nul 2>nul
if errorlevel 1 goto INSTALL_DEPS
goto DEPS_OK

:INSTALL_DEPS
echo.
echo   Installing required Python packages...
echo.
!PYTHON! -m pip install --disable-pip-version-check cryptography lz4
if errorlevel 1 (
    echo.
    echo   ERROR: Failed to install required packages.
    echo   Try running manually: pip install cryptography lz4
    echo.
    pause
    exit /b
)
:DEPS_OK

:: ============================================================
:: FIND CRIMSON DESERT GAME DIRECTORY
:: ============================================================

set "GAMEDIR="

:: === Common Steam library paths (one per line - easier and more reliable) ===
set "paths[1]=C:\Program Files (x86)\Steam\steamapps\common\Crimson Desert"
set "paths[2]=C:\Program Files\Steam\steamapps\common\Crimson Desert"
set "paths[3]=D:\SteamLibrary\steamapps\common\Crimson Desert"
set "paths[4]=E:\SteamLibrary\steamapps\common\Crimson Desert"
set "paths[5]=F:\SteamLibrary\steamapps\common\Crimson Desert"

:: You can easily add more drives/folders here:
:: set "paths[6]=G:\SteamLibrary\steamapps\common\Crimson Desert"

:: Check common paths
for /L %%i in (1,1,5) do (
    if exist "!paths[%%i]!\0010\0.paz" (
        set "GAMEDIR=!paths[%%i]!"
        goto :found_game
    )
)

:: Fallback: try relative path from current mod folder
for %%I in ("%SD%..") do set "GAMEDIR=%%~fI"
if exist "!GAMEDIR!\0010\0.paz" goto :found_game

:: ==================== Game not found ====================
cls
echo.
echo ============================================================
echo ERROR: Crimson Desert game directory not found.
echo ============================================================
echo.
echo Alternatively, make sure the game is installed in one of these locations:
echo.
for /L %%i in (1,1,5) do echo     !paths[%%i]!
echo.
echo If your game is on another drive (G:, H:, etc.), edit the script and add the path.
echo.
pause
exit /b

:found_game
echo Game directory found: !GAMEDIR!

set "PAZ=!GAMEDIR!\0010\0.paz"
if not exist "!PAZ!" (
    cls
    echo.
    echo   ============================================================
    echo    ERROR: Game archive not found.
    echo   ============================================================
    echo.
    echo    This mod folder must be placed inside the Crimson Desert
    echo    game directory, for example:
    echo.
    echo      Crimson Desert\UltraWideDesert\install.bat
    echo.
    echo    The "0010" folder should be next to this mod folder.
    echo.
    pause
    exit /b
)

:: Write permission check (batch-native, no PowerShell to avoid AV flags)
copy /b NUL "!GAMEDIR!\0010\_perm_test.tmp" >nul 2>nul
if not errorlevel 1 (
    del "!GAMEDIR!\0010\_perm_test.tmp" >nul 2>nul
    goto PERM_OK
)
cls
echo.
echo   ============================================================
echo    ERROR: Cannot write to game files.
echo   ============================================================
echo.
echo    If using Xbox App / Game Pass, the game folder may be
echo    read-only. Try one of these fixes:
echo.
echo    1. Xbox App ^> Crimson Desert ^> Manage ^> Move to
echo       a different drive
echo    2. Right-click the game folder ^> Properties ^>
echo       uncheck "Read-only" ^> Apply to all subfolders
echo.
pause
exit /b
:PERM_OK

:: ============================================================
:: FIRST-RUN CHECK
:: ============================================================
if exist "!SD!backups\original_backup.bin" goto SKIP_FIRSTRUN
cls
echo.
echo   ============================================================
echo    UltraWide Desert v%VER%  --  First Time Setup
echo   ============================================================
echo.
echo    This looks like your first time running this mod.
echo.
echo    IMPORTANT: If you have another camera mod installed
echo    (CDCamera, CrimsonCamera, etc.), you MUST uninstall it
echo    first or verify your game files:
echo.
echo      Steam ^> Crimson Desert ^> Properties
echo      ^> Installed Files ^> "Verify integrity of game files"
echo.
echo    If this is a clean install with no other camera mods,
echo    you're good to go.
echo.
set /p "FRC=   Continue? [Y/N]: "
if /i not "!FRC!"=="Y" goto :EOF
:SKIP_FIRSTRUN

:: ============================================================
:: VARIABLES
:: ============================================================
set "STYLE=default"
set "SNAME=Default"
set "FOV=0"
set "FOVNAME=No FoV Change"
set "BANE="
set "COMBAT=default"

:: ============================================================
:: STEP 1 - CAMERA STYLE
:: ============================================================
:STEP1
cls
echo.
echo   ============================================================
echo   ^|^|                                                        ^|^|
echo   ^|^|   U L T R A W I D E    D E S E R T    v%VER%           ^|^|
echo   ^|^|                                                        ^|^|
echo   ^|^|        Camera Mod for Crimson Desert                   ^|^|
echo   ^|^|        "Because size matters."                         ^|^|
echo   ^|^|                                                        ^|^|
echo   ^|^|     For 32:9  ^|  21:9  ^|  Ultrawide Displays          ^|^|
echo   ^|^|                                                        ^|^|
echo   ============================================================
echo    Created by @TheFitzy
echo    Inspired by @Maszradine (CDCamera) ^& @manymanecki (CrimsonCamera)
echo   ------------------------------------------------------------
echo    Game: !GAMEDIR!
echo   ------------------------------------------------------------
echo.
echo   Step 1 of 4: Camera Style
echo.
echo    RECOMMENDED FOR ULTRAWIDE:
echo.
echo    [1] Panoramic       Wide pullback, filmic exploration
echo    [2] Frontier        Heroic shoulder cam, great framing
echo    [3] Low Rider       Hip-level, full body + wide horizon
echo    [4] Smoothed        Vanilla framing + smoothing
echo.
echo    MORE STYLES:
echo.
echo    [5] Close-Up        Close over-the-shoulder (16:9 feel)
echo    [6] Ground Level    Below hip, dramatic angle
echo    [7] Dirt Cam        Ground-level, extreme low
echo    [8] Survival        Tight horror-game OTS (16:9 feel)
echo.
echo    [R] Restore Vanilla Camera    [Q] Quit
echo.
set /p "S1=   Choose [1-8, R, Q]: "

if /i "!S1!"=="Q" goto :EOF
if /i "!S1!"=="R" goto RESTORE
if "!S1!"=="1" set "STYLE=cinematic"&set "SNAME=Panoramic"& goto STEP2
if "!S1!"=="2" set "STYLE=western"&set "SNAME=Frontier"& goto STEP2
if "!S1!"=="3" set "STYLE=lowcam"&set "SNAME=Low Rider"& goto STEP2
if "!S1!"=="4" set "STYLE=default"&set "SNAME=Smoothed"& goto STEP2
if "!S1!"=="5" set "STYLE=immersive"&set "SNAME=Close-Up"& goto STEP2
if "!S1!"=="6" set "STYLE=vlowcam"&set "SNAME=Ground Level"& goto STEP2
if "!S1!"=="7" set "STYLE=ulowcam"&set "SNAME=Dirt Cam"& goto STEP2
if "!S1!"=="8" set "STYLE=re2"&set "SNAME=Survival"& goto STEP2
echo    Invalid choice.
timeout /t 2 >nul
goto STEP1

:: ============================================================
:: STEP 2 - FIELD OF VIEW
:: ============================================================
:STEP2
cls
echo.
echo   ============================================================
echo    UltraWide Desert v%VER%  --  !SNAME! Camera
echo   ============================================================
echo.
echo   Step 2 of 4: Field of View
echo.
echo    FoV widens your peripheral view. Vanilla is a narrow 40
echo    degrees which feels like tunnel vision on ultrawides.
echo.
echo    "When your monitor is wider than your desk,
echo     you need FoV to match."
echo.
echo    .-------------------------------------------------------.
echo    ^|  ##  ^| Change ^| Total  ^| Notes                        ^|
echo    ^|------^|--------^|--------^|----------------------------^|
echo    ^| [0]  ^| None   ^| 40 deg ^| Vanilla (not recommended)   ^|
echo    ^| [1]  ^| +10    ^| 50 deg ^| Minimal, good for 16:9      ^|
echo    ^| [2]  ^| +15    ^| 55 deg ^| Subtle improvement           ^|
echo    ^| [3]  ^| +20    ^| 60 deg ^| * Sweet spot for 21:9       ^|
echo    ^| [4]  ^| +25    ^| 65 deg ^| * Great for 21:9 + 32:9     ^|
echo    ^| [5]  ^| +30    ^| 70 deg ^| * Perfect for 32:9          ^|
echo    ^| [6]  ^| +40    ^| 80 deg ^| Extreme, slight fisheye      ^|
echo    '------'--------'--------'----------------------------'
echo.
echo    * = Recommended for widescreen monitors
echo.
set /p "S2=   Choose [0-6]: "

if "!S2!"=="0" set "FOV=0"&set "FOVNAME=No Change (40 deg)"& goto STEP3
if "!S2!"=="1" set "FOV=10"&set "FOVNAME=+10 (= 50 deg)"& goto STEP3
if "!S2!"=="2" set "FOV=15"&set "FOVNAME=+15 (= 55 deg)"& goto STEP3
if "!S2!"=="3" set "FOV=20"&set "FOVNAME=+20 (= 60 deg)"& goto STEP3
if "!S2!"=="4" set "FOV=25"&set "FOVNAME=+25 (= 65 deg)"& goto STEP3
if "!S2!"=="5" set "FOV=30"&set "FOVNAME=+30 (= 70 deg)"& goto STEP3
if "!S2!"=="6" set "FOV=40"&set "FOVNAME=+40 (= 80 deg)"& goto STEP3
echo    Invalid choice.
timeout /t 2 >nul
goto STEP2

:: ============================================================
:: STEP 3 - CENTERED MODE
:: ============================================================
:STEP3
cls
echo.
echo   ============================================================
echo    UltraWide Desert v%VER%  --  !SNAME!, !FOVNAME!
echo   ============================================================
echo.
echo   Step 3 of 4: Centered Camera
echo.
echo    In vanilla, the character stands off-center to the left
echo    with an over-the-shoulder view.
echo.
echo    Centered Mode places the character in the middle of the
echo    screen instead. On ultrawide monitors this can look
echo    incredibly cinematic -- especially with wider FoV.
echo.
echo    [Y] Yes  --  Center the character
echo    [N] No   --  Keep shoulder offset (default)
echo.
set /p "S3=   Enable Centered Mode? [Y/N]: "

if /i "!S3!"=="Y" set "BANE=--bane"& goto STEP4
if /i "!S3!"=="N" set "BANE="& goto STEP4
echo    Invalid choice.
timeout /t 2 >nul
goto STEP3

:: ============================================================
:: STEP 4 - COMBAT CAMERA
:: ============================================================
:STEP4
set "BANELABEL=OFF"
if defined BANE set "BANELABEL=ON"
cls
echo.
echo   ============================================================
echo    UltraWide Desert v%VER%  --  !SNAME!, !FOVNAME!
echo   ============================================================
echo    Centered: !BANELABEL!
echo.
echo   Step 4 of 4: Combat Camera
echo.
echo    How far should the camera pull back during lock-on combat?
echo.
echo    Wider combat view = see more enemies around you.
echo    On ultrawide you already have the real estate, so going
echo    wider can feel incredibly immersive in big fights.
echo.
echo    [0] Default    Standard combat camera
echo    [1] Wider      More room to see the battlefield
echo    [2] Maximum    Widest possible combat view
echo.
set /p "S4=   Combat zoom [0-2]: "

if "!S4!"=="0" set "COMBAT=default"& goto CONFIRM
if "!S4!"=="1" set "COMBAT=wide"& goto CONFIRM
if "!S4!"=="2" set "COMBAT=max"& goto CONFIRM
echo    Invalid choice.
timeout /t 2 >nul
goto STEP4

:: ============================================================
:: CONFIRMATION
:: ============================================================
:CONFIRM
set "BANELABEL=OFF  (shoulder offset)"
if defined BANE set "BANELABEL=ON   (centered framing)"
set "COMBATLABEL=Default"
if "!COMBAT!"=="wide" set "COMBATLABEL=Wider"
if "!COMBAT!"=="max" set "COMBATLABEL=Maximum"
cls
echo.
echo   ============================================================
echo    UltraWide Desert v%VER%  --  Confirm Install
echo   ============================================================
echo.
echo    Game:     !GAMEDIR!
echo.
echo    .----------------------------------------------------.
echo    ^|  Camera Style:   !SNAME!
echo    ^|  Field of View:  !FOVNAME!
echo    ^|  Centered:       !BANELABEL!
echo    ^|  Combat Camera:  !COMBATLABEL!
echo    '----------------------------------------------------'
echo.
echo    [Y] Install now    [N] Start over    [Q] Quit
echo.
set /p "OK=   Continue? [Y/N/Q]: "

if /i "!OK!"=="Q" goto :EOF
if /i "!OK!"=="N" goto STEP1
if /i not "!OK!"=="Y" goto CONFIRM

:: ============================================================
:: INSTALL
:: ============================================================
:INSTALL
cls
echo.
echo   ============================================================
echo    Installing...
echo   ============================================================
echo.

set "PYARGS=--style !STYLE! --fov !FOV! --combat !COMBAT!"
if defined BANE set "PYARGS=!PYARGS! --bane"

echo    Camera:  !SNAME!
echo    FoV:     !FOVNAME!
echo    Centered:!BANELABEL!
echo    Combat:  !COMBATLABEL!
echo.
echo    Patching game files...
echo.

!PYTHON! "%SD%lib\camera_mod.py" "!GAMEDIR!" !PYARGS!

if errorlevel 1 (
    echo.
    echo   ============================================================
    echo    INSTALLATION FAILED
    echo   ============================================================
    echo.
    echo    Make sure the game is NOT running, then try again.
    echo    If the game was recently updated, try restoring first.
    echo.
    pause
    goto STEP1
)

echo.
echo   ============================================================
echo   ^|^|                                                        ^|^|
echo   ^|^|              S U C C E S S !                           ^|^|
echo   ^|^|                                                        ^|^|
echo   ^|^|   Your ultrawide desert awaits.                        ^|^|
echo   ^|^|   "Go forth and see... everything."                    ^|^|
echo   ^|^|                                                        ^|^|
echo   ============================================================
echo.
echo    Camera:  !SNAME!
echo    FoV:     !FOVNAME!
echo    Centered:!BANELABEL!
echo    Combat:  !COMBATLABEL!
echo.
echo    Launch the game to see your new camera!
echo.
echo    To change settings:  run install.bat again
echo    To restore vanilla:  choose [R] in the menu
echo.
echo   ------------------------------------------------------------
echo    UltraWide Desert v%VER% -- by @TheFitzy
echo    Inspired by @Maszradine (CDCamera) ^& @manymanecki (CrimsonCamera)
echo   ------------------------------------------------------------
echo.
pause
goto STEP1

:: ============================================================
:: RESTORE
:: ============================================================
:RESTORE
cls
echo.
echo   ============================================================
echo    UltraWide Desert  --  Restore Vanilla Camera
echo   ============================================================
echo.
echo    Game: !GAMEDIR!
echo.
echo    This will restore the original vanilla camera settings.
echo    Your ultrawide monitor will weep, but it's your choice.
echo.
set /p "RC=   Continue? [Y/N]: "
if /i not "!RC!"=="Y" goto STEP1

echo.
!PYTHON! "%SD%lib\camera_mod.py" "!GAMEDIR!" --restore

if errorlevel 1 (
    echo.
    echo    Restore failed or no backup found.
    echo    Use Steam: Verify integrity of game files
    echo.
    pause
    goto STEP1
)

echo.
echo   ============================================================
echo    Vanilla camera restored.
echo    Your monitor feels smaller already.
echo   ============================================================
echo.
pause
goto STEP1
