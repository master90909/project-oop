class TekkenCharacter:
    def __init__(self,name,ability):
        self.name = name
        self.ability = ability
    def introduce(self,func):
        def decorator(*args, **kwargs):

            print("..... executing a function")
            func(*args, **kwargs)

            print("This character is amazing! ")
        return decorator
char = TekkenCharacter("nina", "Fatal Judgement")
@char.introduce
def character_intro():
    print(f"I am {char.name} and I can use {char.ability}")
