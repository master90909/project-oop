from turtles import Leonardo, Michelangelo, Donatello, Rapheal

tur1 = Leonardo("Leonardo", "madog")
tur2 = Michelangelo("Michelangelo", "techman")
tur3 = Donatello("Donatello", "wisman")
tur4 = Rapheal("Rapheal", "clownman")

for i in [tur1,tur2,tur3,tur4]:
    print(i.alias)
