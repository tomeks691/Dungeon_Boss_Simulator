import json
import random

with open("special_effect.json") as f:
    special_effect_from_file = json.load(f)


class DungeonCreator:
    def __init__(self, room):
        self.cost = random.randint(1, 5)
        self.damage = random.randint(0, 3)
        self.special_effect = special_effect_from_file[str(random.randint(1, 3))]
        self.name_room = room
        # self.background_room = f"|¯¯¯¯¯¯¯¯¯¯|\n|  {self.name_room}  |\n[__________|"
        # self.background_room = self.update()

    def update(self):
        background_room = f"|¯¯¯¯¯¯¯¯¯¯|\n|  {self.name_room}  |\n[__________|"
        return background_room
