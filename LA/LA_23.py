class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def introduce(self, func):
        def intro(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return intro

anime_character = AnimeCharacter("Naruto", "shadow clone jutsu")
@anime_character.introduce
def character_intro():
    print(f"I am {anime_character.name} and I can use {anime_character.ability}")

character_intro()
