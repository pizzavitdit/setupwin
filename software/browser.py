# scripts/browser.py
# This python file installs the user's browser of choice!
import os, sys
print("1) Google Chrome\n2) Chromium\n3) Ungoogled Chromium\n4) Firefox\n5) LibreWolf\n6) Brave\n7) None of the above")
BROWSER_NUMBER = input(int("Please enter the browser's number according to the output above. (1, 2, 3, 4, 5, 6 or 7): "))
if BROWSER_NUMBER == 1:
    os.system("winget install -e --id Google.Chrome")
    print("Installed Google Chrome")
elif BROWSER_NUMBER == 2:
    os.system("winget install -e --id Hibbiki.Chromium")
    print("Installed Chromium")
elif BROWSER_NUMBER == 3:
    os.system("winget install -e --id eloston.ungoogled-chromium")
    print("Installed Ungoogle Chromium")
elif BROWSER_NUMBER == 4:
    os.system("winget install -e --id Mozilla.Firefox")
    print("Installed Mozilla Firefox")
elif BROWSER_NUMBER == 5:
    os.system("winget install -e --id LibreWolf.LibreWolf")
    print("Installed LibreWolf")
elif BROWSER_NUMBER == 6:
    os.system("winget install -e --id BraveSoftware.BraveBrowser")
    print("Installed Brave")