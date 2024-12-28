# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(temperature):
    
    celsius = (temperature - 32) * 5 / 9
    print(f"{temperature}°F is {celsius:.2f}°C")
    return celsius

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(temperature):
    
    fahrenheit = (temperature * 9 / 5) + 32
    print(f"{temperature}°C is {fahrenheit:.2f}°F")
    return fahrenheit

# Main function
def main():
    
    while True:
       
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("0. Exit")
        
        choice = input("Choose an option (0-2): ")
        
        if choice == "0":
            print("Exiting...")
            break
        
        elif choice == "1":
            temp = float(input("Enter temperature in Celsius: "))
            celsius_to_fahrenheit(temp)
        
        elif choice == "2":
            temp = float(input("Enter temperature in Fahrenheit: "))
            fahrenheit_to_celsius(temp)
        
        else:
            print("Invalid option. Please enter a number between 0 and 2.")

if __name__ == "__main__":
    main()
