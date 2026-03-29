"""CDCamera modification rules as pure data.

Extracted from CDCamera v1.6.1 presets. Each layer (shared base, style,
bane, combat) defines element-level attribute changes composed together
by build_modifications() into a single ModificationSet.

CDCamera uses additive FoV: fov_value is the delta (e.g. 10, 20) added
to every Fov attribute on TPS/TwoTargetLockOn sections.
"""

from dataclasses import dataclass, field


@dataclass
class ModificationSet:
    element_mods: dict = field(default_factory=dict)
    fov_value: int = 0


# ── Section lists ──────────────────────────────────────────────────

_BASIC_SECTIONS = [
    'Player_Basic_Default',
    'Player_Basic_Default_Walk',
    'Player_Basic_Default_Run',
    'Player_Basic_Default_Runfast',
]

_WEAPON_SECTIONS = [
    'Player_Weapon_Default',
    'Player_Weapon_Default_Walk',
    'Player_Weapon_Default_Run',
    'Player_Weapon_Default_RunFast',
    'Player_Weapon_Default_RunFast_Follow',
]

_DEFAULT_ONLY = [
    'Player_Basic_Default',
    'Player_Weapon_Default',
]

_WALK_RUN = [
    'Player_Basic_Default_Walk',
    'Player_Basic_Default_Run',
    'Player_Basic_Default_Runfast',
    'Player_Weapon_Default_Walk',
    'Player_Weapon_Default_Run',
    'Player_Weapon_Default_RunFast',
    'Player_Weapon_Default_RunFast_Follow',
]

_ALL_MAIN = _BASIC_SECTIONS + _WEAPON_SECTIONS

_BANE_SECTIONS = _BASIC_SECTIONS + [
    'Player_Basic_Default_Aim_Zoom',
] + _WEAPON_SECTIONS


# ── Shared base (always applied) ──────────────────────────────────
# Smoothing, horse camera fixes, steadycam behavior, FoV normalization.
# These changes are present in ALL CDCamera presets including steady_nofov.

_SHARED_BASE = {
    # Global CameraBlendParameter transitions — these control camera state
    # blend timings (how smoothly the camera transitions between modes).
    'CameraBlendParameter#1': {
        'BlendInEaseType': ('SET', 'OutQuad'),
        'BlendInTime': ('SET', '1'),
        'BlendOutTime': ('SET', '1'),
    },
    'CameraBlendParameter#2': {
        'BlendInEaseType': ('SET', 'InOutQuad'),
        'BlendInTime': ('SET', '1.2'),
        'BlendOutEaseType': ('SET', 'InOutQuad'),
        'BlendOutTime': ('SET', '1.2'),
    },
    'CameraBlendParameter#3': {
        'BlendInTime': ('SET', '0.5'),
        'BlendOutTime': ('SET', '1.0'),
    },
    'CameraBlendParameter#4': {
        'BlendInEaseType': ('SET', 'OutQuad'),
        'BlendInTime': ('SET', '2.0'),
        'BlendOutEaseType': ('SET', 'OutQuad'),
        'BlendOutTime': ('SET', '2.0'),
    },
    'CameraBlendParameter#5': {
        'BlendInEaseType': ('SET', 'InQuad'),
        'BlendInTime': ('SET', '4.0'),
        'BlendOutTime': ('SET', '2.5'),
    },
    'CameraBlendParameter#6': {
        'BlendInEaseType': ('SET', 'OutQuad'),
        'BlendInTime': ('SET', '2.0'),
        'BlendOutTime': ('SET', '2.0'),
    },
    'CameraBlendParameter#8': {
        'BlendInEaseType': ('REMOVE', ''),
        'BlendInTime': ('REMOVE', ''),
        'BlendOutEaseType': ('REMOVE', ''),
        'BlendOutTime': ('REMOVE', ''),
    },

    # Section-level FoV normalization (reduce vanilla 45/53 to 40)
    'Player_Basic_Default_Run': {'Fov': ('SET', '40')},
    'Player_Basic_Default_Runfast': {'Fov': ('SET', '40')},
    'Player_Basic_Default_Walk': {'Fov': ('SET', '40')},
    'Player_Weapon_Default': {'Fov': ('SET', '40')},
    'Player_Weapon_Default_Run': {'Fov': ('SET', '40')},
    'Player_Weapon_Default_RunFast': {'Fov': ('SET', '40')},
    'Player_Weapon_Default_RunFast_Follow': {'Fov': ('SET', '40')},
    'Player_Weapon_Default_Walk': {'Fov': ('SET', '40')},

    # Two-target lock-on distance caps
    'Player_Interaction_TwoTarget/ZoomLevel[3]': {
        'MaxZoomDistance': ('SET', '10'),
    },
    'Player_Interaction_TwoTarget/ZoomLevel[4]': {
        'MaxZoomDistance': ('SET', '10'),
    },

    # Player OffsetByVelocity elimination (remove camera sway on move)
    'Player_Basic_Default_Run/OffsetByVelocity': {
        'OffsetLength': ('SET', '0'),
    },
    'Player_Basic_Default_Runfast/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },
    'Player_Weapon_Default_Run/OffsetByVelocity': {
        'OffsetLength': ('SET', '0'),
    },
    'Player_Weapon_Default_RunFast/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },
    'Player_Weapon_Default_RunFast_Follow/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },

    # Animal mount smoothing
    'Player_Animal_Default/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
    },
    'Player_Animal_Default_Run/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
    },
    'Player_Animal_Default_Run/OffsetByVelocity': {
        'OffsetLength': ('SET', '0'),
    },
    'Player_Animal_Default_Runfast/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
    },
    'Player_Animal_Default_Runfast/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
        'DampSpeed': ('SET', '0.5'),
    },
    'Player_Animal_Default_Walk/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
    },

    # Horse — blend and offset
    'Player_Ride_Horse/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Horse/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },

    # Horse Run
    'Player_Ride_Horse_Run': {
        'FollowPitchSpeedRate': ('SET', '0.8'),
        'FollowStartTime': ('SET', '1'),
    },
    'Player_Ride_Horse_Run/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },

    # Horse Fast Run
    'Player_Ride_Horse_Fast_Run': {
        'FollowPitchSpeedRate': ('SET', '0.8'),
        'FollowStartTime': ('SET', '1'),
        'FollowYawSpeedRate': ('SET', '0.8'),
    },
    'Player_Ride_Horse_Fast_Run/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Horse_Fast_Run/OffsetByVelocity': {
        'DampSpeed': ('SET', '0.5'),
        'OffsetLength': ('SET', '0.0'),
    },

    # Horse Dash
    'Player_Ride_Horse_Dash': {
        'Fov': ('SET', '40'),
        'FollowPitchSpeedRate': ('SET', '0.8'),
        'FollowStartTime': ('SET', '1'),
        'FollowYawSpeedRate': ('SET', '0.8'),
    },
    'Player_Ride_Horse_Dash/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Horse_Dash/OffsetByVelocity': {
        'DampSpeed': ('SET', '0.5'),
        'OffsetLength': ('SET', '0.0'),
    },

    # Horse Dash Attack
    'Player_Ride_Horse_Dash_Att': {
        'Fov': ('SET', '40'),
        'FollowPitchSpeedRate': ('SET', '0.8'),
        'FollowStartTime': ('SET', '1'),
        'FollowYawSpeedRate': ('SET', '0.8'),
    },
    'Player_Ride_Horse_Dash_Att/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Horse_Dash_Att/CameraDamping': {
        'PivotDampingMaxDistance': ('SET', '0.5'),
    },
    'Player_Ride_Horse_Dash_Att/OffsetByVelocity': {
        'DampSpeed': ('SET', '0.5'),
        'OffsetLength': ('SET', '0.0'),
    },

    # Horse Thrust Attack
    'Player_Ride_Horse_Att_Thrust': {
        'Fov': ('SET', '40'),
        'FollowPitchSpeedRate': ('SET', '0.8'),
        'FollowStartTime': ('SET', '1'),
        'FollowYawSpeedRate': ('SET', '0.8'),
    },

    # Horse Left/Right Attacks
    'Player_Ride_Horse_Att_L': {
        'Fov': ('SET', '40'),
    },
    'Player_Ride_Horse_Att_L/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Horse_Att_L/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },
    'Player_Ride_Horse_Att_R': {
        'Fov': ('SET', '40'),
    },
    'Player_Ride_Horse_Att_R/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Horse_Att_R/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },

    # Elephant mount
    'Player_Ride_Elephant': {
        'FollowPitchSpeedRate': ('SET', '0.8'),
        'FollowYawSpeedRate': ('SET', '0.8'),
    },
    'Player_Ride_Elephant/CameraBlendParameter': {
        'BlendInTime': ('SET', '0.3'),
        'BlendOutTime': ('SET', '0.3'),
    },
    'Player_Ride_Elephant/CameraDamping': {
        'PivotDampingMaxDistance': ('SET', '0.5'),
    },
    'Player_Ride_Elephant/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },

    # Wyvern mount
    'Player_Ride_Wyvern': {
        'FollowStartTime': ('SET', '1'),
        'FollowYawSpeedRate': ('SET', '0.8'),
    },
    'Player_Ride_Wyvern/OffsetByVelocity': {
        'OffsetLength': ('SET', '0.0'),
    },
}


# ── Shared steadycam UpOffset normalization ────────────────────────
# These UpOffset→0.3 changes are present in ALL CDCamera presets and
# form the steadycam foundation that style layers may override.

def _build_shared_steadycam():
    """Build UpOffset normalization applied to all configs."""
    mods = {}

    # Basic Default: ZL3, ZL4 only
    mods['Player_Basic_Default/ZoomLevel[3]'] = {'UpOffset': ('SET', '0.3')}
    mods['Player_Basic_Default/ZoomLevel[4]'] = {'UpOffset': ('SET', '0.3')}

    # Aim_Zoom: ZL3 only
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.3'),
    }

    # Basic Walk / Run / Runfast: ZL2, ZL3, ZL4
    for sec in ('Player_Basic_Default_Walk', 'Player_Basic_Default_Run',
                'Player_Basic_Default_Runfast'):
        mods[f'{sec}/ZoomLevel[2]'] = {'UpOffset': ('SET', '0.30')}
        mods[f'{sec}/ZoomLevel[3]'] = {'UpOffset': ('SET', '0.3')}
        mods[f'{sec}/ZoomLevel[4]'] = {'UpOffset': ('SET', '0.3')}

    # All Weapon sections: ZL3, ZL4 only
    for sec in _WEAPON_SECTIONS:
        mods[f'{sec}/ZoomLevel[3]'] = {'UpOffset': ('SET', '0.3')}
        mods[f'{sec}/ZoomLevel[4]'] = {'UpOffset': ('SET', '0.3')}

    return mods


# ── Style layers ───────────────────────────────────────────────────
# Applied on top of the shared base. 'default' = no style changes.

def _build_western():
    """Western: raised UpOffset 0.4, ZoomDistance 2.5/5, wide shoulder."""
    mods = {}
    for sec in _ALL_MAIN:
        mods[f'{sec}/ZoomLevel[2]'] = {
            'UpOffset': ('SET', '0.4'),
            'InDoorUpOffset': ('SET', '0.4'),
            'ZoomDistance': ('SET', '2.5'),
        }
        mods[f'{sec}/ZoomLevel[3]'] = {
            'UpOffset': ('SET', '0.4'),
            'ZoomDistance': ('SET', '5'),
        }
        mods[f'{sec}/ZoomLevel[4]'] = {
            'UpOffset': ('SET', '0.4'),
        }
    # RightOffset 0.8 on ZL4 for walk/run + Weapon_Default (not Basic Default)
    mods['Player_Weapon_Default/ZoomLevel[4]']['RightOffset'] = ('SET', '0.8')
    for sec in _WALK_RUN:
        mods[f'{sec}/ZoomLevel[4]']['RightOffset'] = ('SET', '0.8')
    # Basic walk/run ZL2 RightOffset (not Weapon)
    for sec in _WALK_RUN:
        if sec.startswith('Player_Basic'):
            mods[f'{sec}/ZoomLevel[2]']['RightOffset'] = ('SET', '0.5')

    # Weapon walk/run: tighter ZL2 ZoomDistance
    for sec in _WALK_RUN:
        if sec.startswith('Player_Weapon'):
            mods[f'{sec}/ZoomLevel[2]']['ZoomDistance'] = ('SET', '2')

    # Walk/Run ZL4 ZoomDistance (Run sections tighter at 5.0)
    for sec in _WALK_RUN:
        if sec.endswith('_Run'):
            mods[f'{sec}/ZoomLevel[4]']['ZoomDistance'] = ('SET', '5.0')
        else:
            mods[f'{sec}/ZoomLevel[4]']['ZoomDistance'] = ('SET', '8')

    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[2]'] = {
        'UpOffset': ('SET', '0.4'),
        'InDoorUpOffset': ('SET', '0.4'),
        'ZoomDistance': ('SET', '2.5'),
    }
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.4'),
    }
    return mods


def _build_cinematic():
    """Cinematic: wider pullback with shoulder offset on movement."""
    mods = {}
    for sec in _DEFAULT_ONLY:
        mods[f'{sec}/ZoomLevel[2]'] = {'ZoomDistance': ('SET', '3.0')}
        mods[f'{sec}/ZoomLevel[3]'] = {'UpOffset': ('SET', '0.3')}
    # Basic Default ZL4: no RightOffset change (keep vanilla 1.1)
    mods['Player_Basic_Default/ZoomLevel[4]'] = {
        'UpOffset': ('SET', '0.3'),
        'ZoomDistance': ('SET', '9'),
    }
    # Weapon Default ZL4: set RightOffset
    mods['Player_Weapon_Default/ZoomLevel[4]'] = {
        'UpOffset': ('SET', '0.3'),
        'ZoomDistance': ('SET', '9'),
        'RightOffset': ('SET', '0.8'),
    }
    for sec in _WALK_RUN:
        is_weapon = sec.startswith('Player_Weapon')
        mods[f'{sec}/ZoomLevel[2]'] = {'ZoomDistance': ('SET', '3.0')}
        if not is_weapon:
            mods[f'{sec}/ZoomLevel[2]']['RightOffset'] = ('SET', '0.5')
        mods[f'{sec}/ZoomLevel[3]'] = {'ZoomDistance': ('SET', '6.0')}
        mods[f'{sec}/ZoomLevel[4]'] = {
            'RightOffset': ('SET', '0.8'),
            'ZoomDistance': ('SET', '9'),
        }

    # Run sections: tighter ZL4 ZoomDistance
    for sec in ('Player_Basic_Default_Run', 'Player_Weapon_Default_Run'):
        mods[f'{sec}/ZoomLevel[4]']['ZoomDistance'] = ('SET', '6.0')

    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[2]'] = {
        'ZoomDistance': ('SET', '3.0'),
    }
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.3'),
    }
    return mods


def _build_immersive():
    """Immersive: western pattern with closer ZoomDistances 2.0/4.0/6.0."""
    mods = {}
    for sec in _ALL_MAIN:
        mods[f'{sec}/ZoomLevel[2]'] = {
            'UpOffset': ('SET', '0.4'),
            'InDoorUpOffset': ('SET', '0.4'),
            'ZoomDistance': ('SET', '2.0'),
        }
        mods[f'{sec}/ZoomLevel[3]'] = {
            'UpOffset': ('SET', '0.4'),
            'ZoomDistance': ('SET', '4.0'),
        }
        mods[f'{sec}/ZoomLevel[4]'] = {
            'UpOffset': ('SET', '0.4'),
            'RightOffset': ('SET', '0.8'),
            'ZoomDistance': ('SET', '6.0'),
        }
    for sec in _WALK_RUN:
        mods[f'{sec}/ZoomLevel[2]']['RightOffset'] = ('SET', '0.5')

    for sec in _WALK_RUN:
        if sec.startswith('Player_Weapon'):
            mods[f'{sec}/ZoomLevel[2]']['ZoomDistance'] = ('SET', '2')

    # Run sections get tighter ZL4
    for sec in ('Player_Basic_Default_Run', 'Player_Weapon_Default_Run'):
        mods[f'{sec}/ZoomLevel[4]']['ZoomDistance'] = ('SET', '4.0')

    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[2]'] = {
        'UpOffset': ('SET', '0.4'),
        'InDoorUpOffset': ('SET', '0.4'),
        'ZoomDistance': ('SET', '2.0'),
    }
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.4'),
    }
    return mods


def _build_lowcam_variant(basic_run_zl2_up, basic_zl3_indoor, weapon_zl3_indoor):
    """Low camera variants with per-section vertical offsets.

    Args:
        basic_run_zl2_up: ZL2 UpOffset for Basic Walk/Run/Runfast
        basic_zl3_indoor: ZL3 InDoorUpOffset for Basic sections + Aim_Zoom
        weapon_zl3_indoor: ZL3 InDoorUpOffset for Weapon sections
    """
    mods = {}

    # Basic Default (non-walk/run)
    mods['Player_Basic_Default/ZoomLevel[2]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', '0.0'),
        'ZoomDistance': ('SET', '2.5'),
    }
    mods['Player_Basic_Default/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', basic_zl3_indoor),
        'ZoomDistance': ('SET', '5'),
    }
    mods['Player_Basic_Default/ZoomLevel[4]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', '0.0'),
    }

    # Basic Walk/Run/Runfast
    for sec in ('Player_Basic_Default_Walk', 'Player_Basic_Default_Run',
                'Player_Basic_Default_Runfast'):
        mods[f'{sec}/ZoomLevel[2]'] = {
            'UpOffset': ('SET', basic_run_zl2_up),
            'InDoorUpOffset': ('SET', '0.0'),
            'RightOffset': ('SET', '0.5'),
            'ZoomDistance': ('SET', '2.5'),
        }
        zl3_dist = '5' if sec.endswith('_Walk') else '5.0'
        mods[f'{sec}/ZoomLevel[3]'] = {
            'UpOffset': ('SET', '0.0'),
            'InDoorUpOffset': ('SET', basic_zl3_indoor),
            'ZoomDistance': ('SET', zl3_dist),
        }
        if sec.endswith('_Run'):
            zl4_dist = '5.0'
        elif sec.endswith('_Runfast'):
            zl4_dist = '08'
        else:
            zl4_dist = '8'
        mods[f'{sec}/ZoomLevel[4]'] = {
            'UpOffset': ('SET', '0.0'),
            'InDoorUpOffset': ('SET', '0.0'),
            'RightOffset': ('SET', '0.8000'),
            'ZoomDistance': ('SET', zl4_dist),
        }

    # Weapon Default
    mods['Player_Weapon_Default/ZoomLevel[2]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', '0.0'),
        'ZoomDistance': ('SET', '2.5'),
    }
    mods['Player_Weapon_Default/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', weapon_zl3_indoor),
        'ZoomDistance': ('SET', '5'),
    }
    mods['Player_Weapon_Default/ZoomLevel[4]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', '0.0'),
        'RightOffset': ('SET', '0.8000'),
    }

    # Weapon Walk/Run/RunFast/RunFast_Follow
    for sec in ('Player_Weapon_Default_Walk', 'Player_Weapon_Default_Run',
                'Player_Weapon_Default_RunFast',
                'Player_Weapon_Default_RunFast_Follow'):
        mods[f'{sec}/ZoomLevel[2]'] = {
            'UpOffset': ('SET', '0.0'),
            'InDoorUpOffset': ('SET', '0.0'),
            'ZoomDistance': ('SET', '2'),
        }
        zl3_dist = '5' if sec.endswith('_Walk') else '5.0'
        mods[f'{sec}/ZoomLevel[3]'] = {
            'UpOffset': ('SET', '0.0'),
            'InDoorUpOffset': ('SET', weapon_zl3_indoor),
            'ZoomDistance': ('SET', zl3_dist),
        }
        if sec.endswith('_Run'):
            zl4_dist = '5.0'
        elif '_RunFast' in sec:
            zl4_dist = '08'
        else:
            zl4_dist = '8'
        mods[f'{sec}/ZoomLevel[4]'] = {
            'UpOffset': ('SET', '0.0'),
            'InDoorUpOffset': ('SET', '0.0'),
            'RightOffset': ('SET', '0.8000'),
            'ZoomDistance': ('SET', zl4_dist),
        }

    # Aim_Zoom
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[2]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', '0.0'),
        'ZoomDistance': ('SET', '2.5'),
    }
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[3]'] = {
        'UpOffset': ('SET', '0.0'),
        'InDoorUpOffset': ('SET', basic_zl3_indoor),
    }

    return mods


def _build_re2():
    """RE2-style tight over-the-shoulder: ZoomDistance 1.8/3/6."""
    mods = {}
    for sec in _ALL_MAIN:
        mods[f'{sec}/ZoomLevel[2]'] = {'ZoomDistance': ('SET', '1.8')}
        mods[f'{sec}/ZoomLevel[3]'] = {'ZoomDistance': ('SET', '3')}
        mods[f'{sec}/ZoomLevel[4]'] = {'ZoomDistance': ('SET', '6')}
    for sec in _WALK_RUN:
        mods[f'{sec}/ZoomLevel[2]']['RightOffset'] = ('SET', '0.4')
        mods[f'{sec}/ZoomLevel[3]']['RightOffset'] = ('SET', '0.7')

    # Weapon walk/run: tighter ZL2 ZoomDistance
    for sec in _WALK_RUN:
        if sec.startswith('Player_Weapon'):
            mods[f'{sec}/ZoomLevel[2]']['ZoomDistance'] = ('SET', '1')

    # Run/Runfast sections: ZL3 ZoomDistance='3.5'
    _run_runfast = [
        'Player_Basic_Default_Run',
        'Player_Basic_Default_Runfast',
        'Player_Weapon_Default_Run',
        'Player_Weapon_Default_RunFast',
        'Player_Weapon_Default_RunFast_Follow',
    ]
    for sec in _run_runfast:
        mods[f'{sec}/ZoomLevel[3]']['ZoomDistance'] = ('SET', '3.5')

    # ZL4 RightOffset='0.7000' for walk/run + Weapon_Default
    for sec in _WALK_RUN + ['Player_Weapon_Default']:
        mods[f'{sec}/ZoomLevel[4]']['RightOffset'] = ('SET', '0.7000')

    # Run sections: ZL4 ZoomDistance='3.5'
    for sec in ('Player_Basic_Default_Run', 'Player_Weapon_Default_Run'):
        mods[f'{sec}/ZoomLevel[4]']['ZoomDistance'] = ('SET', '3.5')

    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[2]'] = {
        'ZoomDistance': ('SET', '1.8'),
    }
    mods['Player_Basic_Default_Aim_Zoom/ZoomLevel[3]'] = {
        'ZoomDistance': ('SET', '3'),
    }
    return mods


_STYLE_BUILDERS = {
    'western':   _build_western,
    'cinematic': _build_cinematic,
    'immersive': _build_immersive,
    'lowcam':    lambda: _build_lowcam_variant('-0.2', '-0.2', '-0.2'),
    'vlowcam':   lambda: _build_lowcam_variant('-0.4', '-0.4', '-0.4'),
    'ulowcam':   lambda: _build_lowcam_variant('-0.6', '-0.6', '-0.6'),
    're2':       _build_re2,
}


# ── Bane layer (zero RightOffset for centered framing) ────────────

def _build_bane_mods():
    """Set RightOffset=0.0 on ZL 2/3/4 across all TPS sections.

    Also zeros InDoorRightOffset where vanilla defines it:
    ZL2 on Basic sections + Aim_Zoom, and ZL4 on Runfast.
    """
    mods = {}
    _indoor_right_zl2 = {'Player_Basic_Default', 'Player_Basic_Default_Aim_Zoom',
                          'Player_Weapon_Default'}
    for sec in _BANE_SECTIONS:
        for lvl in (2, 3, 4):
            key = f'{sec}/ZoomLevel[{lvl}]'
            entry = mods.setdefault(key, {})
            entry['RightOffset'] = ('SET', '0.0')
            if lvl == 2 and sec in _indoor_right_zl2:
                entry['InDoorRightOffset'] = ('SET', '0.0')
            if lvl == 4 and sec == 'Player_Basic_Default_Runfast':
                entry['InDoorRightOffset'] = ('SET', '0.0')

    # Gliding and freefall
    _air_bane = {
        'Player_Basic_Gliding/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Gliding/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Gliding_Fast/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Gliding_Fast/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Gliding_Zoom/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Gliding_Fall/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Gliding_Fall/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Glide_Kick_Aim_Zoom/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Glide_Bow_Aim_Zoom/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall_Start/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall_Start/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall_Lv2/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall_Lv2/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall_Aim/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_FreeFall_Aim/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_SuperJump/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_SuperJump/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
    }
    mods.update(_air_bane)

    # Swimming, climbing, traversal
    _traversal_bane = {
        'Player_Swim_Default/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Swim_Default/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_PointClimb/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_PointClimb/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_PointClimb/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_PointClimb_Follow/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_PointClimb_Follow/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_PointClimb_Follow/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_CharacterClimb/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_CharacterClimb/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_CharacterClimb/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Climb/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Climb/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_RopeSwing/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_RopeSwing/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_RopeSwing/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_RopePull/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_RopePull/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_RopePull/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_WaterFallPass/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_WaterFallPass/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_WaterFallPass/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Wood_Hanging/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Wagon/ZoomLevel[1]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Wagon/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Wagon_Wait/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Wagon_Wait/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
    }
    mods.update(_traversal_bane)

    # Weapon combat states (guard, rush, zoom, lock-on, aim)
    _combat_bane = {
        'Player_Weapon_Guard/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Guard/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Guard/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Rush/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Rush/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Rush/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Down/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Down/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Down/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Indoor/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom_Light/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom_Light/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom_Out/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_Zoom_Out/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_LockOn_System/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_LockOn_System/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Weapon_LockOn_System/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Revive_LockOn_System/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Revive_LockOn_System/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Revive_LockOn_System/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Cinematic_LockOn/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Cinematic_LockOn/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Cinematic_LockOn/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Hit_Throw/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Hit_Throw/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Hit_Throw/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
    }
    mods.update(_combat_bane)

    # Animal form
    _animal_bane = {
        'Player_Animal_Default/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Walk/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Walk/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Walk/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Run/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Run/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Run/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Runfast/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Runfast/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Animal_Default_Runfast/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
    }
    mods.update(_animal_bane)

    # Misc gameplay (rest, contemplation, fishing, etc.)
    _misc_bane = {
        'Player_Rest/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Rest/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Rest/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_NoZoom/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_NoZoom/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
        'Player_Basic_Teleport/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
    }
    mods.update(_misc_bane)

    # Ride and mount sections
    _ride_bane = {
        'Player_Ride_Broom/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Broom/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Canoe/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Canoe/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Elephant/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Elephant/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Att_L/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Att_L/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Att_R/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Att_R/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Att_Thrust/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Att_Thrust/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Dash/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Dash/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Dash_Att/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Dash_Att/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Fast_Run/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Fast_Run/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Run/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Horse_Run/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Warmachine/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Warmachine/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Warmachine_Aim/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Warmachine_Dash/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Wyvern/ZoomLevel[2]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Wyvern/ZoomLevel[3]': {'RightOffset': ('SET', '0.0')},
        'Player_Ride_Wyvern/ZoomLevel[4]': {'RightOffset': ('SET', '0.0')},
    }
    mods.update(_ride_bane)

    return mods


# ── Combat lock-on layers ─────────────────────────────────────────

_COMBAT_LOCKON = {
    'wide': {
        'Player_FollowLearn_LockOn_Boss/ZoomLevel[2]': {
            'ZoomDistance': ('SET', '4.5'),
        },
        'Player_FollowLearn_LockOn_Boss/ZoomLevel[3]': {
            'ZoomDistance': ('SET', '8.3'),
        },
        'Player_FollowLearn_LockOn_Boss/ZoomLevel[4]': {
            'ZoomDistance': ('SET', '9.9'),
        },
        'Player_Force_LockOn/ZoomLevel[2]': {
            'ZoomDistance': ('SET', '15'),
        },
        'Player_LockOn_Titan/ZoomLevel[1]': {
            'ZoomDistance': ('SET', '15'),
        },
        'Player_Weapon_LockOn/ZoomLevel[3]': {
            'ZoomDistance': ('SET', '9.8'),
        },
        'Player_Weapon_TwoTarget/ZoomLevel[1]': {
            'ZoomDistance': ('SET', '5.3'),
        },
        'Player_Weapon_TwoTarget/ZoomLevel[2]': {
            'ZoomDistance': ('SET', '9'),
        },
        'Player_Weapon_TwoTarget/ZoomLevel[3]': {
            'ZoomDistance': ('SET', '9'),
        },
    },
    'max': {
        'Player_FollowLearn_LockOn_Boss/ZoomLevel[2]': {
            'ZoomDistance': ('SET', '6.0'),
        },
        'Player_FollowLearn_LockOn_Boss/ZoomLevel[3]': {
            'ZoomDistance': ('SET', '9.9'),
        },
        'Player_FollowLearn_LockOn_Boss/ZoomLevel[4]': {
            'ZoomDistance': ('SET', '9.9'),
        },
        'Player_Force_LockOn/ZoomLevel[2]': {
            'ZoomDistance': ('SET', '20'),
        },
        'Player_LockOn_Titan/ZoomLevel[1]': {
            'ZoomDistance': ('SET', '20'),
        },
        'Player_Weapon_LockOn/ZoomLevel[3]': {
            'ZoomDistance': ('SET', '9.9'),
        },
        'Player_Weapon_TwoTarget/ZoomLevel[1]': {
            'ZoomDistance': ('SET', '7.0'),
        },
        'Player_Weapon_TwoTarget/ZoomLevel[2]': {
            'ZoomDistance': ('SET', '9'),
        },
        'Player_Weapon_TwoTarget/ZoomLevel[3]': {
            'ZoomDistance': ('SET', '9'),
        },
    },
}


# ── Composition ────────────────────────────────────────────────────

def _merge(base, overlay):
    """Deep-merge overlay into base (overlay wins on conflict)."""
    for key, attrs in overlay.items():
        if key in base:
            base[key].update(attrs)
        else:
            base[key] = dict(attrs)


def build_modifications(style, fov, bane, combat):
    """Build the complete modification set from user choices.

    Args:
        style: 'default', 'western', 'cinematic', 'immersive',
               'lowcam', 'vlowcam', 'ulowcam', or 're2'
        fov: int — additive FoV delta (0=no change, 10/15/20/25/30/40)
        bane: bool — zero RightOffset for centered framing
        combat: 'default', 'wide', or 'max'

    Returns:
        ModificationSet with element_mods and fov_value
    """
    mods = {}

    # Layer 1: shared base — always applied
    _merge(mods, _SHARED_BASE)
    _merge(mods, _build_shared_steadycam())

    # Layer 2: style-specific overrides
    if style in _STYLE_BUILDERS:
        _merge(mods, _STYLE_BUILDERS[style]())

    # Layer 3: bane — zero RightOffset (applied after style so it wins)
    if bane:
        _merge(mods, _build_bane_mods())

    # Layer 4: combat lock-on distance
    if combat in _COMBAT_LOCKON:
        _merge(mods, _COMBAT_LOCKON[combat])

    return ModificationSet(element_mods=mods, fov_value=fov)
