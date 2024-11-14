class toy():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def describeToys(self):
        print(f"The toys name is {self.name} and the {self.price}")

class car(toy):
    def __init__(self, name, price):
        super().__init__(name, price)

t = toy("dogtoys", 120)
t.describeToys()
c = car("toycar", 50)
c.describeToys()
