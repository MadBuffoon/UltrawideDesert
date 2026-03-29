# UltraWide Desert - Python Builder

**Camera overhaul for Crimson Desert, built for 32:9 and 21:9 ultrawide monitors.**

[![NexusMods](https://img.shields.io/badge/NexusMods-Pre--Built%20Presets-orange?style=for-the-badge&logo=nexusmods)](https://www.nexusmods.com/crimsondesert/mods/383)
[![GitHub Release](https://img.shields.io/badge/GitHub-Python%20Builder%20v1.2-blue?style=for-the-badge&logo=github)](https://github.com/FitzDegenhub/UltrawideDesert/releases)

![UltraWide Desert - 32:9 Gameplay](screenshot.png)

---

> **Most users should grab the [Pre-Built Presets from NexusMods](https://www.nexusmods.com/crimsondesert/mods/383)** — no Python, no setup, just extract and play.
>
> This repo is the **Python Builder** for advanced users or when the game updates and the pre-built presets are outdated.

---

## When to Use This

- The game updated and the NexusMods presets say "size mismatch"
- You want to customise camera values beyond the 336 presets
- You prefer building from source

## Features

| Feature | Description |
|---------|-------------|
| **8 Camera Styles** | Panoramic, Frontier, Low Rider, Smoothed, Close-Up, Ground Level, Dirt Cam, Survival |
| **Adjustable FoV** | +10 to +40 degrees (up to 80 total) with per-aspect-ratio recommendations |
| **Steadycam** | Eliminates camera sway and bobbing during movement |
| **Centered Mode** | Places your character in the center of the screen instead of off to the left |
| **Combat Zoom** | 3 levels — Default, Wider (+50%), Maximum (+100%) |
| **Mount Fixes** | Consistent FoV and distance across Horse, Elephant, Wyvern, Warmachine, Broom |
| **Combat Smoothing** | Reduced aggressive zoom during lock-on and shield combat |

## How It Works

The builder dynamically patches `playercamerapreset.xml` inside the game's `0.paz` archive. It decrypts (ChaCha20), decompresses (LZ4), modifies the XML, size-matches, recompresses, re-encrypts, and writes it back.

Because it reads the game's `0.pamt` index dynamically, **it auto-adapts to game updates** without needing a mod update.

## Requirements

- **Python 3.10+** — [Download](https://www.python.org/downloads/) (check "Add python.exe to PATH" during install)
- **cryptography** and **lz4** packages (installed automatically by the installer)

## Installation

1. Download the [latest release](https://github.com/FitzDegenhub/UltrawideDesert/releases) or clone this repo
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

- **[@TheFitzy](https://www.nexusmods.com/profile/TheFitzy)** — Creator of UltraWide Desert
- **[@lazorr410](https://github.com/lazorr410)** — [crimson-desert-unpacker](https://github.com/lazorr410/crimson-desert-unpacker) — without which this mod would not exist
- **[@Maszradine](https://www.nexusmods.com/profile/Maszradine)** — [CDCamera](https://www.nexusmods.com/crimsondesert/mods/65) — camera rules, steadycam system, and style presets
- **[@manymanecki](https://www.nexusmods.com/profile/manymanecki)** — [CrimsonCamera](https://www.nexusmods.com/crimsondesert/mods/373) — dynamic PAZ modification approach

## License

This project uses code from [crimson-desert-unpacker](https://github.com/lazorr410/crimson-desert-unpacker) (MIT License).
