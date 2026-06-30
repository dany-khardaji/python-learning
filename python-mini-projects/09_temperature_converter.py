
def c_to_f(celsius):
    return (celsius * 1.8) + 32

def f_to_c(farenheit):
    return (farenheit - 32) / 1.8

def c_to_k(celsius):
    return celsius + 273.15

def k_to_c(kelvin):
    return kelvin - 273.15


while True:
    print("====== Temperature Converter ======")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Quit")
    print("===================================")

    chosen_option = input("Choose an option: ")

    if chosen_option == "1":
        while True:
            try:
                celsius = int(input("Enter Celsius: "))
                break
            except ValueError:
                print("Invalid entry.")
        print(f"Farenheit conversion:{c_to_f(celsius):.1f} °F")

    elif chosen_option == "2":
        while True:
            try:
                farenheit = int(input("Enter farenheit: "))
                break
            except ValueError:
                print("Invalid entry.")
        print(f"Celsius conversion: {f_to_c(farenheit):.1f} °C")
        
    elif chosen_option == "3":
        while True:
            try:
                celsius = int(input("Enter celsius: "))
                break
            except ValueError:
                print("Invalid entry.")
        print(f"Kelvin conversion: {c_to_k(celsius):.1f} °K")
    
    elif chosen_option == "4":
        while True:
            try:
                kelvin = int(input("Enter kelvin: "))
                break
            except ValueError:
                print("Invalid entry.")
        print(f"Celsius conversion: {k_to_c(kelvin):.1f} °C")

    elif chosen_option == "5":
        print("Applcation terminated.")
        break

    else:
        print("Invalid entry.")

