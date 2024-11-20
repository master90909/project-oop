class Dog:
    def __init__(self,name,):
        self.name = name
    def speak(self):
        return "Bark"

class Cat:

    def __init__(self,name,):
        self.name = name
    def speak(self):
        return "Meow"

class Bird:

    def __init__(self,name,):
        self.name = name
    def speak(self):
        return "Chirp"
class Fish:

    def __init__(self,name,):
        self.name = name
    def speak(self):
        return "...."
def Animel_sounds(animel):
    print(f"{animel.name} says: {animel.speak()}")
dog = Dog("dog")
cat = Cat("cat")
bird = Bird("bird")
fish = Fish("fish")
arr = [dog,cat,bird,fish]

for count in arr:
    Animel_sounds(count)
