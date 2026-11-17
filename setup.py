import sys
import os
from cx_Freeze import setup, Executable

shortcut_table = [
    (
        "DesktopShortcut",
        "DesktopFolder",
        "RhexoStation 5 Music",
        "TARGETDIR",
        "[TARGETDIR]RhexoSpotifyPS5.exe",
        None,
        "PlayStation 5 Console Flow Music Client",
        None,
        None,
        None,
        None,
        "TARGETDIR"
    ),
    (
        "ProgramMenuShortcut",
        "ProgramMenuFolder",
        "RhexoStation 5 Music",
        "TARGETDIR",
        "[TARGETDIR]RhexoSpotifyPS5.exe",
        None,
        "PlayStation 5 Console Flow Music Client",
        None,
        None,
        None,
        None,
        "TARGETDIR"
    )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {
    "data": msi_data,
    "add_to_path": True,
    "initial_target_dir": r"[ProgramFilesFolder]\RhexoStation5",
    "upgrade_code": "{E98A53B2-3714-4B29-9A21-A495861E7B92}"
}

build_exe_options = {
    "packages": ["os", "sys", "shutil", "zipfile", "subprocess", "time", "webview"],
    "include_files": ["rhexo_ps5.ico"],
    "excludes": ["tkinter", "unittest"]
}

base = "gui" if sys.platform == "win32" else None

setup(
    name="RhexoStation5",
    version="2.5.0",
    description="PlayStation 5 Native Spotify Injector and Music OS",
    author="Rhexo",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables=[
        Executable(
            "app.py",
            base=base,
            target_name="RhexoSpotifyPS5.exe",
            icon="rhexo_ps5.ico",
            shortcut_name="RhexoStation 5 Music",
            shortcut_dir="DesktopFolder"
        )
    ]
)
