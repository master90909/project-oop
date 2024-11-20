class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name} for {self.power} damage.")
        print(f"{target.name}'s health is now {target.health}.")

    def special_move(self):
        raise NotImplementedError("Subclasses must override this method.")

class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash! Power doubled for the next attack.")
        self.power *= 2

class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball! Deals 100 damage.")
        self.power += 100

class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots Piercing Arrow! Ignores defenses.")

class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars! Gains 50 health.")
        self.health += 50

warrior = Warrior("Warrior", 150, 20)
mage = Mage("Mage", 100, 30)
archer = Archer("Archer", 120, 25)
monster = Monster("Monster", 200, 40)

characters = [warrior, mage, archer, monster]
for character in characters:
    character.special_move()
    
