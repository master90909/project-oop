class phone():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def describePhone(self):
        print(f"The phone brand is {self.brand} and {self.model}")

class android(phone):
    def __init__(self, brand, model):
        phone.__init__(self,brand, model)

p = phone("vivo","y19")
p.describePhone()
a = android("vivo", "x21")
a.describePhone()

