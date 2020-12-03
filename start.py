import os
import time
import sys
import subprocess

os.system('cls') # Clear Terminal

print("""
    __        __ _               _____  _
    \ \      / /(_)  _ __       |  ___|(_)
     \ \ /\ / / | | | '_ \      | |_   | |
      \ V  V /  | | | | | |     |  _|  | |
       \_/\_/   |_| |_| |_|     |_|    |_|


[1] Show Saved Wi-Fi Passwords (With Details)
[2] Show Saved Wi-Fi Passwords (Without Details)
[3] Show Wireless Device Capabilities
[4] Disconnect from a Wireless Network
[0] Exit
    """)

choice = input(" Choose a number: ")
choice = int(choice)

if choice == 3:
    extra_data = subprocess.check_output(['netsh', 'wlan', 'show', 'wirelesscapabilities']).decode('utf-8').split('\n')
    output_WDI_Win = [line.split(":")[1][1:-1] for line in extra_data if "WDI Version (Windows)" in line]
    output_WDI_IHV = [line.split(":")[1][1:-1] for line in extra_data if "WDI Version (IHV)" in line]
    output_firm = [line.split(":")[1][1:-1] for line in extra_data if "Firmware Version" in line]
    print(f'\n WDI Version (Windows)  : {output_WDI_Win[0]} \n WDI Version (IHV)      : {output_WDI_IHV[0]} \n Firmware Version       : {output_firm[0]} \n')
    print("      Coded By AbirHasan2005      ")
    print("")
    os.system('pause')
    exit()

elif choice == 4:
    print("\nDisconnecting from connected Router!")
    print("")
    time.sleep(2)
    #disconnect = subprocess.check_output(['netsh', 'wlan', 'disconnect']).decode('utf-8').split('\n')
    os.system('netsh wlan disconnect')
    print("")
    os.system('pause')
    exit()

elif choice == 0:
    print("")
    exit()

elif choice == 2:
    print("")
    print("Wi-Fi Router Names & Passwords:")
    time.sleep(1)
    print("")

########## Main Code ############# Main Code ############# Main Code ##########

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    router = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

    for name in router:
        info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8').split('\n')
        passwrd = [line.split(':')[1][1:-1] for line in info if "Key Content" in line]

        try:
            # Output with Password
            print(f' Router   : {name} \n Password : {passwrd[0]} \n')
        except IndexError:
            # Output without Password
            print(f' Router   : {name} \n Password : Not Found! \n')

    print("      Coded By AbirHasan2005      ")
    print("")
    os.system('pause')
    exit()

elif choice == 1:
    print("")
    print("Wi-Fi Router Names, Passwords & Other Details:")
    time.sleep(1)
    print("")

    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
    router = [line.split(':')[1][1:-1] for line in data if "All User Profile" in line]

    for name in router:
        info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', name, 'key=clear']).decode('utf-8').split('\n')
        passwrd = [line.split(':')[1][1:-1] for line in info if "Key Content" in line]
        net = [line.split(':')[1][1:-1] for line in info if "Network type" in line]
        version = [line.split(':')[1][1:-1] for line in info if "Version" in line]
        sec = [line.split(':')[1][1:-1] for line in info if "Authentication" in line]
        try:
            # Output with Password
            print(f' Router   : {name} \n Password : {passwrd[0]} \n Network  : {net[0]} \n Version  : {version[0]} \n Security : {sec[0]} \n')
        except IndexError:
            # Output without Password
            print(f' Router   : {name} \n Password : Not Found! \n Network  : {net[0]} \n Version  : {version[0]} \n Security : {sec[0]} \n')

########## Main Code ############# Main Code ############# Main Code ##########

    print("      Coded By AbirHasan2005      ")
    print("")
    os.system('pause')
    exit()

else:
    os.system('cls')
    os.system('python start.py')
