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
        
        

######
#!/usr/bin/python3
import os
import re

# Mensaje recibido (puede ser copiado desde WhatsApp, correo, etc.)
mensaje = input("Paste the message containing tote numbers:\n")

# Buscar códigos tipo AC3000126354
totes = re.findall(r"AC\d{10,}", mensaje)

# Si no se encontró ningún código, pedirlos manualmente
if not totes:
    manual = input('No totes found. Write tote numbers separated by commas:\n')
    replaced = manual.replace(',', ' ')
    totes = replaced.split()

# Confirmar envío
send = input('Want to send these totes?\n')
if send.lower() in ['yes', 'y']:
    target = input("INSERT TARGET:\n")
    osrid = os.environ.get('OSR_ID', 'default_id')  # Fallback si no está definida

    for tote in totes:
        command = f"get_tray --tray {tote} --target {target} --osr-id {osrid}"
        print(f'Running: {command}')
        os.system(command)
else:
    print("Totes parsed:")
    for tote in totes:
        print(f"'{tote}',")


