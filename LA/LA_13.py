#LA#13
class animal():
    def __init__(self,name,types):
        self.name = name
        self.type = types

class fish(animal):
    def __init__(self,name,types,):
        super().__init__(name,types)
        self.can_swim = True

    def describeToys(self):
        print(f"\nThe name of fish is {self.name} type of fish {self.type} can swim {self.can_swim}")


f = fish("flappyfish","floating fish",)
f.can_swim = True
f.describeToys()
