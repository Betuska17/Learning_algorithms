with open("archivo.txt", "r", encoding="utf-8") as archivo:
    texto = archivo.read()

import string
texto = texto.lower()
for signo in string.punctuation:
    texto = texto.replace(signo, "")

palabras = texto.split()

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

hapax = 0
for palabra in frecuencia:
    if frecuencia[palabra] == 1:
        hapax += 1

print("Cantidad de hápax en el documento:", hapax)



select transporter_name, transporter_pos, max(tsth_date),
case 
when transporter_state = -5 then 'suspended'
when transporter_state = 10 then 'maintence'
when transporter_state = -10 then 'disabled'
end as state 
from transporter_locations
join locations on tl_loc_id = loc_id
join transporters on tl_transporter_id = transporter_id
join transporter_state_trans_hist on tl_transporter_id = tsth_transporter_id
where transporter_name like 'SHUT%'
and transporter_osr_id = 1 
and transporter_pos like '%C0%'
and transporter_state != 0
group by transporter_name;

select transporter_name, transporter_pos, max(tsth_date),
case 
when transporter_state = -5 then 'suspended'
when transporter_state = 10 then 'maintence'
when transporter_state = -10 then 'disabled'
end as state 
from transporter_locations
join locations on tl_loc_id = loc_id
join transporters on tl_transporter_id = transporter_id
join transporter_state_trans_hist on tl_transporter_id = tsth_transporter_id
where transporter_name like 'SHUT%'
and transporter_osr_id = 1 
and transporter_pos like '%C0%'
and transporter_state != 0
group by transporter_name;