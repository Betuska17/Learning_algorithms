#!/usr/bin/python3
import os
import sys

totes = input('Write tote numbers, once you finish enter done\n')

replaced = totes.replace(',', ' ')
lst = replaced.split()
send = input('Want to send this totes?\n')
if send.lower() in ['yes' , 'y']:
    target = input("INSERT TARGET: \n")
    osrid = os.environ['OSR_ID']
    #osrid = osrid[-1]

    #osr = int(input('Osr number: \n'))
    for tote in lst:
        command = f"get_tray --tray {tote} --target {target} --osr-id {osrid}"
        run = os.system(command)
        print(f'Running: {command}')
else:
    for tote in lst:
        print("'" + tote + "',")

