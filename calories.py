from temperature import Temperature


class Calories:
    """
    Calculate and represent the calories required based on the formula:
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, weight, height, age, temp):
        self.weight = weight
        self.height = height
        self.age = age
        # Convert Fahrenheit to Celsius
        self.temperature = (5/9)*(temp-32)

    def calculate(self):
        result = 10*self.weight + 6.5*self.height + 5*self.age + 5 - 10*self.temperature
        return round(result)


temp = Temperature(country="USA", city="Omaha")
calories = Calories(weight=70, height=171, age=19, temp=temp.get())
print(calories.calculate())
