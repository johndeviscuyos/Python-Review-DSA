
class Temperature:
    def __init__(self):
        self.temperature = None
        self.scale = None

    def get_scale(self):
        while True:
            try:
                self.scale = int(input("Choose a conversion: \n Type '1' for Celsius to Fahrenheit \n Type '2' for Fahrenheit to Celsius \n"))
                if self.scale in [1, 2]:
                    return self.scale
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def get_temperature(self):
        while True:
            try:
                self.temperature = float(input("Enter temperature: "))
                return self.temperature
            except ValueError:
                print("Invalid input. Please enter a valid temperature.")

    def conversion(self):
        if self.scale == 1:
            # Celsius to Fahrenheit conversion
            converted_temp = (self.temperature * 9/5) + 32
            print(f"{self.temperature}°C is equal to {converted_temp:.2f}°F")
            return converted_temp
        elif self.scale == 2:
            # Fahrenheit to Celsius conversion
            converted_temp = (self.temperature - 32) * 5/9
            print(f"{self.temperature}°F is equal to {converted_temp:.2f}°C")
            return converted_temp

# Example usage
temp = Temperature()
temp.get_scale()
temp.get_temperature()
temp.conversion()

