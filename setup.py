# setup.py
# Please run with administrator privileges to avoid errors.
import os, sys
import ctypes
import time

# Check if the user has administrator privileges.
try:
    is_admin = os.getuid() == 0
except AttributeError:
    is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
if is_admin == False:
    print("Please run this file with administrator privileges.")
    exit()

# Call the python file to install common free software
os.system("python software/commonsoftware.py")
print("Finished calling the script to install common free software.")

# Call the python file to install the user's browser of choice
os.system("python software/browser.py")
print("Finished calling the script to install user's browser of choice.")

# Ask the user if they want to install Steam
INSTALL_STEAM = input("Do you want to install Steam on your Windows system? (y or n): ")
if INSTALL_STEAM == "y":
    os.system("winget install -e --id Valve.Steam")
    print("Finished installing Steam.")

