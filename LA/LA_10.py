class vehicle():
    def __init__(self,brand,model,fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print (f"The vehicle's brand:{self.brand}, model:{self.model}, and the fuel type:{self.fuel_type}" )
class car(vehicle):
    pass
class motorcycle(vehicle):
    pass


Cars = car("honda","Envix 1996","decals")
Motor = motorcycle("Kawasaki" ,"Barako", "decals" )

Cars.describeVehicle()
Motor.describeVehicle()
