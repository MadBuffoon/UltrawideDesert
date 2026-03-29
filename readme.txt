================================================================
  UltraWide Desert v1.2 - Python Builder
  Camera Overhaul for Crimson Desert
================================================================
  Created by @TheFitzy
  Inspired by @Maszradine (CDCamera) & @manymanecki (CrimsonCamera)
================================================================

  >> This is the PYTHON BUILDER version (from GitHub).  <<
  >> Requires Python 3.10+ with cryptography and lz4.  <<
  >>                                                    <<
  >> Most users should download the Pre-Built Presets   <<
  >> from NexusMods instead -- no Python required.      <<
  >> https://www.nexusmods.com/crimsondesert/mods/383   <<


WHEN TO USE THIS VERSION
------------------------
Use the Python Builder if:

  - The game updated and the pre-built presets are outdated
  - You want to customise camera values beyond the presets
  - You prefer building from source

If you just want to install the mod and play, download the
Pre-Built Presets from NexusMods instead:
https://www.nexusmods.com/crimsondesert/mods/383


REQUIREMENTS
------------
- Python 3.10 or newer
  Download: https://www.python.org/downloads/
  IMPORTANT: Check "Add python.exe to PATH" during install.

- Two Python packages: cryptography and lz4
  (The installer will install these automatically on first run)


INSTALLATION
------------
1. Extract this folder into your Crimson Desert game directory.

   Default Steam location:
   C:\Program Files (x86)\Steam\steamapps\common\Crimson Desert\

   To find your game directory:
   Steam > Right-click Crimson Desert > Manage > Browse Local Files

2. Your folder structure should look like this:

   Crimson Desert\
   +-- 0010\                     <-- game data (already exists)
   |   +-- 0.paz
   |   +-- 0.pamt
   +-- UltraWideDesert\          <-- this mod
   |   +-- install.bat
   |   +-- lib\
   |   |   +-- camera_mod.py
   |   |   +-- camera_rules.py
   |   |   +-- ...
   |   +-- backups\              <-- created automatically
   +-- ...

3. Double-click install.bat

4. Follow the 4-step wizard:
   Step 1: Camera Style
   Step 2: Field of View
   Step 3: Centered Camera
   Step 4: Combat Camera

The Python builder reads your game's actual camera data,
applies modifications on the fly, and patches the result
back. This means it works with ANY game version -- even if
a patch changes the camera data format.


CAMERA STYLES
-------------
Recommended for Ultrawide:
  [1] Panoramic     - Wide pullback, filmic exploration
  [2] Frontier      - Heroic shoulder cam (RDR2 feel)
  [3] Low Rider     - Hip-level, full body + wide horizon
  [4] Smoothed      - Vanilla framing + smoothing

More Styles:
  [5] Close-Up      - Close over-the-shoulder (16:9 feel)
  [6] Ground Level  - Below hip, dramatic angle
  [7] Dirt Cam      - Ground-level, extreme low
  [8] Survival      - Tight horror-game OTS (16:9 feel)


HOW IT WORKS (TECHNICAL)
------------------------
The builder reads the game's 0.pamt index to locate
playercamerapreset.xml inside 0.paz, decrypts it (ChaCha20),
decompresses it (LZ4), applies your chosen camera modifications
to the XML, size-matches the output to the exact compressed
size, re-compresses, re-encrypts, and patches the archive
in-place.

A backup of the original data is saved automatically on first
run. The mod always starts from this vanilla backup so changes
never stack on top of each other.


CHANGING SETTINGS
-----------------
Run install.bat again and pick different options. No need to
uninstall first - the mod always starts from a clean backup.


UNINSTALLATION
--------------
Option A: Run install.bat and choose [R] Restore Vanilla Camera
Option B: Steam > Crimson Desert > Properties > Installed Files
          > "Verify integrity of game files"
Option C: Delete the UltraWideDesert folder and verify files


TROUBLESHOOTING
---------------
"Python is not installed or not in PATH"
  Install Python 3.10+ from python.org. Make sure to check
  "Add python.exe to PATH" during installation.

"Game files appear to be already modified"
  Another camera mod is installed. Verify game files in Steam,
  then run the installer again.

"Cannot write to game files"
  Close the game first. If using Xbox/Game Pass, try moving
  the game to a different drive via the Xbox app.

Game crashes after installing:
  1. Run install.bat and choose [R] Restore
  2. If that fails: Steam > Verify integrity of game files
  3. Delete the UltraWideDesert\backups folder
  4. Run the installer again

================================================================
