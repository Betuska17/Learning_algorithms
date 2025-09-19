from car import Car, ElectricCar
#my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

my_bettle = Car('volkswagen', 'beetle', 2016)
print(my_bettle.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())



processedList = []
    for order in re.findall(regex, inp):
        processedList.append(order)
    return processedList


lines = list(iter(lambda: input().strip(), ''))
totes = ' '.join(lines)
print(f"{COLORS.GREEN}-------------------------------------------------------------------------------{COLORS.END}")

totes_detected = re.findall(r"\bAC\d{8,}", totes)

if totes_detected:
    lst = totes_detected
else:
    replaced = totes.replace(',',' ')
    lst = replaced.split()
