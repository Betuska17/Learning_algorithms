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

print("Cantidad de hápax en el documento:", 


WITH ultima_fecha AS (
  SELECT tsth_transporter_id, MAX(tsth_date) AS fecha_última
  FROM transporter_state_trans_hist
  GROUP BY tsth_transporter_id
),
estado_reciente AS (
  SELECT tsth_transporter_id, transporter_state, tsth_date
  FROM transporter_state_trans_hist
  JOIN ultima_fecha 
    ON tsth_transporter_id = ultima_fecha.tsth_transporter_id
   AND tsth_date = ultima_fecha.fecha_última
)
SELECT 
  transporter_name,
  transporter_pos,
  estado_reciente.tsth_date,
  CASE 
    WHEN estado_reciente.transporter_state = -5 THEN 'suspended'
    WHEN estado_reciente.transporter_state = 10 THEN 'maintence'
    WHEN estado_reciente.transporter_state = -10 THEN 'disabled'
    ELSE 'unknown'
  END AS state
FROM transporter_locations
JOIN locations ON tl_loc_id = loc_id
JOIN transporters ON tl_transporter_id = transporter_id
JOIN estado_reciente ON tl_transporter_id = estado_reciente.tsth_transporter_id
WHERE transporter_name LIKE 'SHUT%'
  AND transporter_osr_id = 1 
  AND transporter_pos LIKE '%C0%'
  AND estado_reciente.transporter_state != 0;
