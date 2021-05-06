class Dog(object):
    min_speed = 40

    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def check_dog_requirements(self):
        return "Qualified" if self.age < 10 and self.speed > self.min_speed else "Not qualified"

    @classmethod
    def change_min_speed(cls, new_speed):
        cls.min_speed = new_speed

    @staticmethod
    def check_weather(temperature):
        return "Weather is ok" if temperature > 10 else "Weather is not ok"


if __name__ == '__main__':
    dog1 = Dog("Nicky", 4, 45)
    dog1.change_min_speed(45)
    print(dog1.check_dog_requirements())
    print(dog1.check_weather(11))
