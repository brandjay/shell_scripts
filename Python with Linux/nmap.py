#!/usr/bin/python3
import subprocess
import sys #calls for system process
greeting = print("Welcome to ur script which would you like? Type nmap or exit")
option = ['nmap', 'exit']
choice = input(option)
if choice == "nmap":
        with open("reults.txt", 'w') as output:
            subprocess.call('./nmap.sh', shell=True, stdout=output)
            print('check file for data')
        
else: print("exiting script")
raise SystemExit