class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def makes_sound(self, sound):
        print(f"{self.name} says {sound}!")

    def play(self):
        print(f"{self.name} is now playing with you.")

    def eat(self):
        print(f"{self.name} is now eating food")


cat1 = Animal("tiger", 5, 8)
cat1.eat()