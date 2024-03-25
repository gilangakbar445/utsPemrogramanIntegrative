class BMI:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    def BMI_Value(self):
        return self.weight / (self.height ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False


w1 = float(input("Enter person 1 weight(pounds) : "))
h1 = float(input("Enter person 2 height(feet) : "))
w2 = float(input("Enter person 1 weight(pounds) : "))
h2 = float(input("Enter person 2 height(feet) : "))
person1 = BMI(w1, h1)
person2 = BMI(w2, h2)
print(f"Person 1 BMI Value = {person1.BMI_Value()}")
print(f"Person 2 BMI Value = {person2.BMI_Value()}")
print(f"Are person 1 and person 2 equal?, {person1 == person2}")