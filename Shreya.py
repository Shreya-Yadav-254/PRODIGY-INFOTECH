def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C/F/K): ").strip().upper()

if unit == 'C':
    print(f"Fahrenheit: {celsius_to_fahrenheit(temp):.2f}")
    print(f"Kelvin: {celsius_to_kelvin(temp):.2f}")
elif unit == 'F':
    print(f"Celsius: {fahrenheit_to_celsius(temp):.2f}")
    print(f"Kelvin: {fahrenheit_to_kelvin(temp):.2f}")
elif unit == 'K':
    print(f"Celsius: {kelvin_to_celsius(temp):.2f}")
    print(f"Fahrenheit: {kelvin_to_fahrenheit(temp):.2f}")
else:
    print("Invalid unit entered. Please enter C, F, or K.")
