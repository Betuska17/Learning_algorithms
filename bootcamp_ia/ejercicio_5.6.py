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
  
  
  
  
  
WITH ultima_fecha AS (
  SELECT tsth_transporter_id, MAX(tsth_date) AS fecha_última
  FROM transporter_state_trans_hist
  GROUP BY tsth_transporter_id
),
estado_reciente AS (
  SELECT th.tsth_transporter_id, th.transporter_state, th.tsth_date
  FROM transporter_state_trans_hist th
  JOIN ultima_fecha uf
    ON th.tsth_transporter_id = uf.tsth_transporter_id
   AND th.tsth_date = uf.fecha_última
)
SELECT 
  tr.transporter_name,
  tl.transporter_pos,
  er.tsth_date,
  CASE 
    WHEN er.transporter_state = -5 THEN 'suspended'
    WHEN er.transporter_state = 10 THEN 'maintence'
    WHEN er.transporter_state = -10 THEN 'disabled'
    ELSE 'unknown'
  END AS state
FROM transporter_locations tl
JOIN locations l ON tl.tl_loc_id = l.loc_id
JOIN transporters tr ON tl.tl_transporter_id = tr.transporter_id
JOIN estado_reciente er ON tl.tl_transporter_id = er.tsth_transporter_id
WHERE tr.transporter_name LIKE 'SHUT%'
  AND tr.transporter_osr_id = 1 
  AND tl.transporter_pos LIKE '%C0%'
  AND er.transporter_state != 0;
  
  
  
todo en ingkes 


WITH latest_state_date AS (
  SELECT tsth_transporter_id, MAX(tsth_date) AS latest_date
  FROM transporter_state_trans_hist
  GROUP BY tsth_transporter_id
),
latest_state AS (
  SELECT th.tsth_transporter_id, th.tsth_date, th.tsth_state AS transporter_state
  FROM transporter_state_trans_hist th
  JOIN latest_state_date ld
    ON th.tsth_transporter_id = ld.tsth_transporter_id
   AND th.tsth_date = ld.latest_date
)
SELECT 
  tr.transporter_name,
  tl.transporter_pos,
  ls.tsth_date,
  CASE 
    WHEN ls.transporter_state = -5 THEN 'suspended'
    WHEN ls.transporter_state = 10 THEN 'maintenance'
    WHEN ls.transporter_state = -10 THEN 'disabled'
    ELSE 'unknown'
  END AS state
FROM transporter_locations tl
JOIN locations l ON tl.tl_loc_id = l.loc_id
JOIN transporters tr ON tl.tl_transporter_id = tr.transporter_id
JOIN latest_state ls ON tl.tl_transporter_id = ls.tsth_transporter_id
WHERE tr.transporter_name LIKE 'SHUT%'
  AND tr.transporter_osr_id = 1 
  AND tl.transporter_pos LIKE '%C0%'
  AND ls.transporter_state != 0;
  
  
  
ultima 


SELECT transporter_name, transporter_pos,
  MAX(tsth_date),
  CASE 
    WHEN transporter_state = -5 THEN 'suspended'
    WHEN transporter_state = 10 THEN 'maintence'
    WHEN transporter_state = -10 THEN 'disabled'
  END AS state
FROM transporter_locations
JOIN locations ON tl_loc_id = loc_id
JOIN transporters ON tl_transporter_id = transporter_id
JOIN transporter_state_trans_hist ON tl_transporter_id = tsth_transporter_id
WHERE transporter_name LIKE 'SHUT%'
  AND transporter_osr_id = 1
  AND transporter_pos LIKE '%C0%'
  AND transporter_state != 0
GROUP BY transporter_name, transporter_pos, transporter_state;




