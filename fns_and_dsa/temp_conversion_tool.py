# ===== Global Conversion Factors =====
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# ===== Conversion Functions =====
def convert_to_celsius(fahrenheit):
    # use global variable (read only, no need to declare `global`)
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # use global variable (read only, no need to declare `global`)
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# ===== Main interaction =====
def main():
    try:
        temp_input = input("Enter the temperature to convert: ")
        # try to convert to float
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C")
    elif unit == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {fahrenheit}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
