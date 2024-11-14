class Hero:
    def __init__(self, name, role, stats, stories):
        self.name = name
        self.role = role
        self.stats = stats
        self.stories = stories

    def __str__(self):
        return f"{self.name} is a {self.role}"

    def story(self):
        return self.stories

    def stat_info(self):
        
        stats_list = self.stats.split("\n")
        hp, mana, hp_regen, mana_regen, pa, pd, md, atk_speed = stats_list

    
        hp = hp.strip()
        mana = mana.strip()
        hp_regen = hp_regen.strip()
        mana_regen = mana_regen.strip()
        pa = pa.strip()
        pd = pd.strip()
        md = md.strip()
        atk_speed = atk_speed.strip()

        return f"""
                     Level 1 | Level 15 | Growth
HP                  : {hp}
Mana                : {mana}
HP Regen            : {hp_regen}
Mana Regen          : {mana_regen}
Physical Attack     : {pa}
Physical Defense    : {pd}
Magic Defense       : {md}
Attack Speed        : {atk_speed}
    """

dic_hero = {
    "Layla": "Marksman",
    "Kagura": "Mage",
    "Arlot": "Fighter/Assassin",
    "Ruby": "Fighter",
    "Fanny": "Assassin",
}

dic_stats = {
    "Layla": """2500    | 4369     | +133.5
424     | 1824     | +100
5.4     | 8.2      | +0.2
2.8     | 6.0      | +0.22857
125     | 230      | +7.5
15      | 71       | +4
15      | 50       | +2.5
1.06    | 1.37     | +0.0221429""",

    "Kagura": """2450    | 4220     | +120
450     | 1500     | +75
5.5     | 7.8      | +0.18
3.0     | 5.5      | +0.2
115     | 210      | +6.5
18      | 68       | +3.5
18      | 55       | +2.7
1.00    | 1.25     | +0.018""",

    "Arlot": """2600    | 4700     | +140
300     | 1200     | +80
6.0     | 9.0      | +0.25
2.5     | 5.0      | +0.15
130     | 240      | +8
20      | 75       | +4
20      | 60       | +3
1.08    | 1.35     | +0.020""",

    "Ruby": """2700    | 4850     | +145
350     | 1350     | +85
6.2     | 9.4      | +0.23
2.7     | 5.8      | +0.19
120     | 225      | +7.2
22      | 77       | +3.8
22      | 65       | +3
1.05    | 1.30     | +0.021""",

    "Fanny": """2400    | 4100     | +125
280     | 1250     | +85
4.8     | 7.5      | +0.20
3.2     | 5.4      | +0.22
140     | 250      | +8.5
16      | 70       | +3.8
16      | 55       | +2.8
1.07    | 1.40     | +0.025""",
}

dic_stor = {
    "Layla": ("Layla was born into a war-torn world where conflict never ceased. "
              "She grew up watching her homeland fall to invaders, but instead of succumbing to despair, "
              "she took up her father’s heavy energy cannon. With her keen eye and unmatched accuracy, "
              "Layla swore to protect her people, becoming a beacon of hope. Over time, her legend grew—"
              "she is now a marksman known for her precision and relentless spirit on the battlefield."),

    "Kagura": ("Kagura hails from a long line of Onmyouji masters, the keepers of ancient mystical arts. "
               "From a young age, she was fascinated by the Seimei Umbrella, an ancient artifact said to possess great power. "
               "Despite her innocence, Kagura's talents were unmatched, and she quickly became one of the youngest ever to master "
               "both the umbrella and the art of controlling spirits. As dark forces began to rise, Kagura took it upon herself "
               "to protect the balance between the mortal and spirit realms."),

    "Arlot": ("Arlot was raised in the Abyss, trained as a merciless warrior under the watchful eyes of demonic overseers. "
              "He knew only cruelty and destruction, leading armies of darkness across battlefields soaked in blood. "
              "But a moment of clarity struck him during a fateful battle when he witnessed the innocent lives destroyed by his hands. "
              "Seeking redemption, Arlot abandoned the Abyss, and now he fights to right the wrongs of his past, though his path to redemption is perilous."),

    "Ruby": ("Ruby was once a cheerful girl with dreams of a peaceful life. But fate had other plans. "
             "During a brutal attack on her village, she was gravely injured and would have perished if not for the intervention of a powerful mage. "
             "Saved, but forever changed, Ruby was gifted a massive scythe imbued with magical powers. Now, with her new weapon, "
             "she roams the land, helping the helpless and avenging those who cannot fight for themselves."),

    "Fanny": ("From a young age, Fanny dreamed of flight. Watching the majestic birds soar above her village, she longed to break free from the constraints of the earth. "
              "When her homeland was attacked, Fanny invented a pair of grappling hooks, allowing her to move swiftly through the air. "
              "Now an agile and deadly assassin, Fanny uses her incredible speed to strike from above, vanishing before the enemy even knows what hit them. "
              "She is driven by her desire to protect those she loves, and her unmatched aerial combat skills make her a terror on the battlefield."),
}


for name in dic_hero:
    hero = Hero(name, dic_hero[name], dic_stats[name], dic_stor[name])
    print(f"""
****************************

Name: {hero.name}

Role: {hero.role}
      {hero}

Stats:
{hero.stat_info()}

Story:
{hero.story()}


""")
print("****************************")

