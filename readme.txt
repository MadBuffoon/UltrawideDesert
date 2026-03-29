================================================================
  UltraWide Desert v2.0 - Widescreen Camera Mod
  Camera Overhaul for Crimson Desert
================================================================
  Created by @TheFitzy
  Inspired by @Maszradine (CDCamera) & @manymanecki (CrimsonCamera)
================================================================


WHAT THIS MOD DOES
------------------
Overhauls the camera for ultrawide monitors (32:9 and 21:9).
Adds wider FoV, 8 camera styles, steadycam smoothing, centered
camera mode, combat zoom options, and horse camera fixes.


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
   |   +-- backups\              <-- created automatically
   +-- ...

3. Double-click install.bat

4. Follow the 4-step wizard:
   Step 1: Camera Style
   Step 2: Field of View
   Step 3: Centered Camera
   Step 4: Combat Camera


CAMERA STYLES
-------------
Recommended for Ultrawide:
  [1] Cinematic     - Wide pullback, filmic exploration
  [2] Western       - RDR2/Witcher 3 heroic framing
  [3] Low Camera    - Hip-level, full body + wide horizon
  [4] Default       - Vanilla framing + smoothing

More Styles:
  [5] Immersive     - Close over-the-shoulder (16:9 feel)
  [6] Very Low Cam  - Below hip, dramatic angle
  [7] Ultra Low Cam - Ground-level, extreme low
  [8] RE2 Style     - Tight horror-game OTS (16:9 feel)


FIELD OF VIEW
-------------
  Change  |  Total  |  Notes
  --------|---------|-------------------------------
  None    |  40 deg |  Vanilla (not recommended)
  +10     |  50 deg |  Minimal, good for 16:9
  +15     |  55 deg |  Subtle improvement
  +20     |  60 deg |  * Sweet spot for 21:9
  +25     |  65 deg |  * Great for 21:9 + 32:9
  +30     |  70 deg |  * Perfect for 32:9
  +40     |  80 deg |  Extreme, slight fisheye

  * = Recommended for widescreen monitors


CHANGING SETTINGS
-----------------
Run install.bat again and pick different options. No need to
uninstall first - the mod always starts from a clean backup.


UNINSTALLATION
--------------
Option A: Run install.bat and choose [R] Restore Vanilla Camera
Option B: Steam > Crimson Desert > Properties > Installed Files
          > "Verify integrity of game files"
Option C: Delete the UltraWideDesert folder and verify game files


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


COMPATIBILITY
-------------
- Works with any version of Crimson Desert
- Compatible with Steam, Epic Games, Xbox/Game Pass
- NOT compatible with CDCamera, CrimsonCamera, or other
  camera mods. Uninstall those first.
- Safe for online play (pure XML data modification)


CREDITS
-------
@TheFitzy    - Creator of UltraWide Desert
@Maszradine  - Original CDCamera (Camera Overhaul for Crimson Desert)
@manymanecki  - CrimsonCamera (Improved Camera Utility)
