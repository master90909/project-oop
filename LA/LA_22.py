class Party():
    def __init__(self,food,special,theme):
        self.food = food
        self.special = special
        self.theme = theme
    def __special_food(self):
        print(f"the special is {self.special}")
    def list_food(self):
        self.__special_food()
    def dish_food(self):
        print(f"the food {self.food}")
   
food1 = Party("ice cream" , "cake" ,"birthday")
food2 = Party("palabok" , "adobo" ,"holloween")
food3 = Party("fried chicken" , "halo holo" ,"christmas")

for i in [food1,food2,food3]:
    i.dish_food()
    i.list_food()
