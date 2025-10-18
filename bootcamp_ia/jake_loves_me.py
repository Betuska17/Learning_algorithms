from my_colors import MY_COLORS as colors
from datetime import datetime
now = datetime.now()

for value in output:
        shuttle = value[0]
        location = value[1]
        state = value[3]
        time = value[2]

        minutes = (now - time).total_seconds() / 60
        if minutes < 20:
            color = colors.GREEN
        elif minutes < 60:
            color = colors.YELLOW
        else:
            color = colors.RED

        if minutes < 60:
            time_str = f"{int(minutes)} seconds"
            #print(f"{color}{shuttle} {state} at {location} since --> {time} ({time_str}) ago {reset}")
            #reset = "\033[0m"

        elif minutes < 3600:
            time_str = f"{int(minutes // 60)} minutes"
            #print(f"{color}{shuttle} {state} at {location} since --> {time} ({time_str}) ago {reset}")
            #reset = "\033[0m"

        else:
            horas = minutes / 3600
            time_str = f"{horas:.1f} hours"
           # print(f"{color}{shuttle} {state} at {location} since --> {time} ({time_str}) ago {reset}")
           # reset = "\033[0m"

            reset = colors.WHITE
            print(f"{color}{shuttle} {state} at {location} since --> {time} ({time_str}) ago{reset}")