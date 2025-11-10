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

def main():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("\nSelect conversion (1-7): ")

        if choice == "7":
            print("K-On Selamanya!")
            break

        try:
            value = float(input("Enter temperature value: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if choice == "1":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C = {result:.2f}°F")
        elif choice == "2":
            result = celsius_to_kelvin(value)
            print(f"{value}°C = {result:.2f}K")
        elif choice == "3":
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F = {result:.2f}°C")
        elif choice == "4":
            result = fahrenheit_to_kelvin(value)
            print(f"{value}°F = {result:.2f}K")
        elif choice == "5":
            result = kelvin_to_celsius(value)
            print(f"{value}K = {result:.2f}°C")
        elif choice == "6":
            result = kelvin_to_fahrenheit(value)
            print(f"{value}K = {result:.2f}°F")
        else:
            print("Invalid choice. Please select from 1 to 7.")

if __name__ == "__main__":
    main()