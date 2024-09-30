"""
CP1404 - Practical
Convert Fahrenheit temperatures to Celsius and save the results.

def generate_temperatures()
    open file using write
    for i in range(number_of_temperatures):
        temperature = random.uniform(-200, 200)
        file write

def fahrenheit_to_celsius(fahrenheit):
   (fahrenheit - 32) * 5.0 / 9.0

def read_temperatures()
    open file using read
    line strip in float

def write_temperatures()
    open file using write

def main()
"""

import random

def generate_temperatures(filename, count = 15):
    """Generate random temperatures and save to a file."""
    with open(filename, "w") as file:
        for _ in range(count):
            temperature = random.uniform(-200,200)
            file.write(f"{temperature}\n")

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5.0 / 9.0

def read_temperatures(filename):
    """Read temperatures from a file."""
    with open(filename, "r") as file:
        return [float(line.strip()) for line in file]

def write_temperatures(temperatures, filename):
    """Write temperatures to a file."""
    with open(filename, "w") as file:
        for temp in temperatures:
            file.write(f"{temp}\n")

def main():
    """Main program to generate and convert temperatures."""
    input_file = "temps_input.txt"
    output_file = "temps_output.txt"

    generate_temperatures(input_file)
    fahrenheit_temps = read_temperatures(input_file) # Read fahrenheit temperatures in input file
    celsius_temps = [fahrenheit_to_celsius(temp) for temp in fahrenheit_temps] # Celsius conversion
    write_temperatures(celsius_temps, output_file) # Write Celsius temperatures to output file

if __name__ == "__main__":
    main()