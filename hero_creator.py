import random


class HeroCreator:
    def __init__(self):
        self.hp = random.randint(1, 4)
        self.damage = random.randint(1, 3)
        self.hero_name = random.choice(["Adam", "Eve", "Johnny"])
        self.class_hero = random.choice(["Knight", "Mage", "Archer", "Rogue"])
        self.hero_background = ""
        if self.class_hero == "Knight":
            self.hero_background = "K"
        elif self.class_hero == "Mage":
            self.hero_background = "M"
        elif self.class_hero == "Archer":
            self.hero_background = "A"
        elif self.class_hero == "Rogue":
            self.hero_background = "R"
