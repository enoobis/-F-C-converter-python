def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

while True:
    # Prompt the user to enter a temperature in either Fahrenheit or Celsius
    temperature = input("Enter a temp in °F or °C: ")

    # Check if the temperature is in Fahrenheit
    if temperature.endswith("/F") or temperature.endswith("/f"):
        # Extract the temperature value from the input string and convert it to float
        temperature_value = float(temperature[:-2])
        # Convert the temperature to Celsius
        temperature_in_celsius = fahrenheit_to_celsius(temperature_value)
        # Print the result
        print(f'{temperature_value}°F is {temperature_in_celsius}°C')
    # Check if the temperature is in Celsius
    elif temperature.endswith("/C") or  temperature.endswith("/c"):
        # Extract the temperature value from the input string and convert it to float
        temperature_value = float(temperature[:-2])
        # Convert the temperature to Fahrenheit
        temperature_in_fahrenheit = celsius_to_fahrenheit(temperature_value)
        # Print the result
        print(f'{temperature_value}°C is {temperature_in_fahrenheit}°F')
    # If the input is invalid, print an error message
    else:
        print("Invalid input")

