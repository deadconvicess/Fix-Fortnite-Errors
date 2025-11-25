import os
import subprocess

os.system("title by @deadconvicess")

def code_14():
    cmds = [
        r'Reg.exe delete "HKLM\Software\Policies\Microsoft\Windows\QoS\FortniteClient-Win64" /f',
        r'Reg.exe delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\FortniteClient-Win64-Shipping.exe\PerfOptions" /f',
        r'Reg.exe delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\FortniteClient-Win64-Shipping.exe" /v "UseLargePages" /f'
    ]
    for c in cmds:
        subprocess.call(c, shell=True)
    input("Done. Press Enter...")

def dns():
    cmds = [
        "ipconfig /flushdns",
        "ipconfig /release",
        "ipconfig /renew",
        "netsh winsock reset",
        "netsh int ip reset",
        "arp -d *",
        "netsh advfirewall reset"
    ]
    for c in cmds:
        subprocess.call(c, shell=True)
    input("Done. Restart your PC. Press Enter...")

def verify():
    subprocess.call(r'start com.epicgames.launcher://apps/Fortnite?action=verify', shell=True)
    input("Error Checking Fortnite...")

def main():
    os.system("cls")
    print("Fortnite error fixer")
    print("")
    print("1. Fix error code 14")
    print("2. Fix DNS errors")
    print("3. Error checker")
    print("")
    c = input("->> ")

    if c == "1":
        code_14()
    elif c == "2":
        dns()
    elif c == "3":
        verify()

if __name__ == "__main__":
    main()
