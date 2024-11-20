class Spiderman:
    def __init__(self, name, age):
        self.name = name.lower()
        self.age = age
    def describeSpiderman(self):
        print(f"Name: {self.name} Age: {self.age} ")

class Tobey(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Andrew(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

class Tom(Spiderman):
    def __init__(self, name, age, movietitle):
        super().__init__(name, age)
        self.movietitle = movietitle

stobey = Tobey("Tobey", 26, "Spider-Man")
sandrew = Andrew("Andrew", 41, "The Amazing Spider-Man")
stom = Tom("Tom", 28, "Homecoming")

print(stobey.describeSpiderman(), stobey.movietitle.upper())
print(sandrew.describeSpiderman(), sandrew.movietitle.upper())
print(stom.describeSpiderman(), stom.movietitle.upper())
