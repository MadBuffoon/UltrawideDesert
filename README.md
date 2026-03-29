# UltraWide Desert - Widescreen Camera Mod

**Camera overhaul for Crimson Desert, built for 32:9 and 21:9 ultrawide monitors.**

[![NexusMods](https://img.shields.io/badge/NexusMods-UltraWide%20Desert-orange?style=for-the-badge&logo=nexusmods)](https://www.nexusmods.com/crimsondesert/mods/383)

> Updated for Patch 1.01.00 - Works while other camera mods are broken!

---

**[Download from NexusMods](https://www.nexusmods.com/crimsondesert/mods/383)** | **[Download from GitHub Releases](https://github.com/FitzDegenhub/UltrawideDesert/releases)** | **[VirusTotal Scan (0 detections)](https://www.virustotal.com/gui/file/b206399424ca75a05a9b506faa9d73c1cd0eb7c5bf0fda021fd354f8df6ae703)**

## Features

| Feature | Description |
|---------|-------------|
| **8 Camera Styles** | Panoramic, Frontier, Low Rider, Smoothed, Close-Up, Ground Level, Dirt Cam, Survival |
| **Adjustable FoV** | +10 to +40 degrees (up to 80 total) with per-aspect-ratio recommendations |
| **Steadycam** | Eliminates camera sway and bobbing during movement |
| **Centered Mode** | Places your character in the center of the screen instead of off to the left |
| **Combat Zoom** | 3 levels - Default, Wider (+50%), Maximum (+100%) |
| **Horse Fixes** | Smoothed FollowSpeed, DampSpeed, BlendTime, and OffsetByVelocity |

## How It Works

The mod dynamically patches `playercamerapreset.xml` inside the game's `0.paz` archive at runtime. No pre-built binaries, no DLL injection - just Python scripts that decrypt (ChaCha20), decompress (LZ4), modify the XML, size-match, recompress, re-encrypt, and write it back.

Because it reads the game's file index dynamically, it auto-adapts to most game updates without needing a mod update.

## Requirements

- **Python 3.10+** - [Download](https://www.python.org/downloads/) (check "Add python.exe to PATH" during install)
- **cryptography** and **lz4** packages (installed automatically by the installer)

## Installation

1. Download and extract the zip
2. Move the `UltraWideDesert` folder into your Crimson Desert game directory:
```
C:\Program Files (x86)\Steam\steamapps\common\Crimson Desert\
```
3. Double-click `install.bat` and follow the 4-step wizard

### Folder Structure
```
Crimson Desert/
├── 0010/                    <- game data
│   ├── 0.paz
│   └── 0.pamt
├── UltraWideDesert/         <- this mod
│   ├── install.bat
│   ├── uninstall.bat
│   ├── lib/
│   │   ├── camera_mod.py
│   │   ├── camera_rules.py
│   │   ├── paz_crypto.py
│   │   ├── paz_parse.py
│   │   └── paz_repack.py
│   └── backups/             <- created automatically
└── ...
```

## FoV Recommendations

| Change | Total | Best For |
|--------|-------|----------|
| +20 | 60 deg | Sweet spot for 21:9 |
| +25 | 65 deg | Great for 21:9 and 32:9 |
| +30 | 70 deg | Perfect for 32:9 |
| +40 | 80 deg | Extreme, slight fisheye |

## Uninstall

- Run `install.bat` and choose **[R] Restore Vanilla Camera**, or
- Steam > Crimson Desert > Properties > Installed Files > "Verify integrity of game files"

## Credits

- **[@TheFitzy](https://www.nexusmods.com/profile/TheFitzy)** - Creator of UltraWide Desert
- **[@lazorr410](https://github.com/lazorr410)** - [crimson-desert-unpacker](https://github.com/lazorr410/crimson-desert-unpacker) - without which this mod would not exist
- **[@Maszradine](https://www.nexusmods.com/profile/Maszradine)** - [CDCamera](https://www.nexusmods.com/crimsondesert/mods/65) - camera rules, steadycam system, and style presets
- **[@manymanecki](https://www.nexusmods.com/profile/manymanecki)** - [CrimsonCamera](https://www.nexusmods.com/crimsondesert/mods/373) - dynamic PAZ modification approach

## License

This project uses code from [crimson-desert-unpacker](https://github.com/lazorr410/crimson-desert-unpacker) (MIT License).
