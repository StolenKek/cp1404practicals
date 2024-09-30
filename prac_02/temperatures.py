"""
CP1404 - Practical
Temperature Conversion Program

def celsius_to_fahrenheit()
    celsius * 9.0 / 5.0 + 32

def fahrenheit_to_celsius()
    (fahrenheit - 32) * 5.0 / 9.0

def main()
    header
    menu
        Option 1: celsius to fahrenheit
        Option 2: fahrenheit to celsius
        Invalid option
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5.0 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0


def main():
    """Main function to handle input and temperature conversions."""
    choice = input("Temperature Converter\n'C': Convert Celsius to Fahrenheit\n'F': Convert Fahrenheit to Celsius\n>>> ").upper()
    if choice == 'C':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is {fahrenheit:.2f}°F.")

    elif choice == 'F':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is {celsius:.2f}°C.")

    else:
        print("Invalid option. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()