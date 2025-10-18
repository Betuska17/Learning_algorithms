from my_colors import MY_COLORS as colors
from datetime import datetime

now = datetime.now()

for value in output:
    shuttle = value[0]
    location = value[1]
    state = value[3]
    time = value[2]

    minutes = (now - time).total_seconds() / 60

    # Semáforo por tiempo
    if minutes < 20:
        color = colors.GREEN
    elif minutes < 60:
        color = colors.YELLOW
    else:
        color = colors.RED

    # Formato de tiempo
    if minutes < 1:
        time_str = f"{int(minutes * 60)} segundos"
    elif minutes < 60:
        time_str = f"{int(minutes)} minutos"
    else:
        horas = minutes / 60
        time_str = f"{horas:.1f} horas"

    reset = colors.WHITE
    print(f"{color}{shuttle} {state} at {location} since --> {time} ({time_str} ago){reset}")
