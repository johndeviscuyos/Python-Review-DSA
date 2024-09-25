
value = int(input("Type the corresponding number to find the value you are looking for\n Type 1 for Volts \n Type 2 for Current \n Type 3 for Resistance\n"))

if value == 1:
    current = int(input("What is the current: "))
    resistance = int(input("What is the resistance: "))
    voltage = current * resistance
    print(voltage)

elif value == 2:
    voltage = int(input("What is the voltage: "))
    resistance = int(input("What is the resistance: "))
    try:
        current = voltage / resistance
        print(current)
    except ZeroDivisionError:
        print("You can't divide by zero")

elif value == 3:
    voltage = int(input("What is the voltage: "))
    current = int(input("What is the current: "))
    try:
        resistance = voltage / current
        print(resistance)
    except ZeroDivisionError:
        print("You can't divide by zero")

