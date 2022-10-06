#!/usr/bin/python3
import subprocess
import sys #calls for system process
greeting = "Welcome to ur script which would you like? "
option = ['nmap', 'exit']
choice = input(option)
if choice == "nmap":
    subprocess.call('./nmap.sh', shell=True)

else: print("exiting script")
raise SystemExit