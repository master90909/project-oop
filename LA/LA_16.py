class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        return "Operating!"

    def info(self):
        return f"{self.brand} {self.model}"

class WashingMachine(Appliance):
    def operate(self):
        return "Washing clothes!"

class Refrigerator(Appliance):
    def operate(self):
        return "Keeping food cold!"

class Microwave(Appliance):
    def operate(self):
        return "Heating food!"

appliances = [
    WashingMachine("LG", "T70"),
    Refrigerator("Samsung", "RF28"),
    Microwave("Panasonic", "NN-SN966S"),
]

for appliance in appliances:
    print(appliance.info())
    print(appliance.operate())

