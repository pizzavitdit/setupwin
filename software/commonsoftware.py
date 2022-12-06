# software/free.py
# This python file installs common free software
import os, sys

# Install VLC
os.system("winget install -e --id VideoLAN.VLC")
# Install OBS Studio
os.system("winget install -e --id OBSProject.OBSStudio")
# Install PowerToys
os.system("winget install -e --id Microsoft.PowerToys")
# Install qBittorrent
os.system("winget install -e --id qBittorrent.qBittorrent")

# Ask the user if they want to install VSCodium
VSCODE = input("Do you want to install VSCodium on your system? (y or n): ")
if VSCODE == "y":
    os.system("winget install -e --id VSCodium.VSCodium")