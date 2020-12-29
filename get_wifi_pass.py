import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode().split('\n')
wifi = [line.split(':')[1][1:-1] for line in data if 'All User Profile' in line]

for wifis in wifi:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifis, 'key=clear']).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "Key Content" in line]
    try:
        print(f'Name : {wifis}, Password : {results[0]}')
    except IndexError:
        print(f'Name : {wifis}, Password : Cannot be read')