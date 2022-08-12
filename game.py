import os
import time

from dungeon_creator import *
from hero_creator import *

coins = 5
rooms = []
heroes = []
player_rooms = []
coins += 1


def use_special_effect(special_effect):
    if special_effect.special_effect["Type"] == "Ekonomia":
        return 1
    elif special_effect.special_effect["Type"] == "Autodestrukcja":
        return "delete"
    elif special_effect["Type"] == "Obrazenia":
        special_effect.damage += 1
        return "Dodano obrażenia +1"


game_on = True
while game_on:
    with open("tutorial.json") as f:
        tutorial = json.load(f)

    print(tutorial["1"], tutorial["2"])
    if len(rooms) == 0:
        while len(rooms) < 3:
            rooms.append(DungeonCreator(f"room_{len(rooms) + 1}"))
    else:
        room_number = rooms[-1].name_room[5:]
        rooms.append(DungeonCreator(f"room_{int(room_number) + 1}"))
    for room in rooms:
        print("Komnaty do zakupu:\n\n")
        print(room.update())
        print(f"Koszt lochu {room.cost}")
        print(f"Obrażenia lochu {room.damage}")
        print("Efekt Specjalny lochu:")
        print(room.special_effect["Description"], room.special_effect["Type"], room.special_effect["Stat"], sep="\n")
        print("Gdy będziesz gotowy zobaczyć kolejne komnaty wciśnij którykolwiek z klawiszy")
        input("Wciśnij klawisz")
        time.sleep(0.35)
        os.system("clear")
    while True:
        print(
            "Jeśli wybrałeś swój nowy loch wpisz odpowiedni numer pokoju (room_1 etc.) jeśli chcesz podejrzeć pokój jeszcze raz wpisz p_NumerPokoju:")
        for i in rooms:
            print(i.name_room)
        choice = input()
        if len(choice) > 0:
            if choice[0] == "p":
                preview_room = rooms[int(choice[-1])-1]
                print("Komnaty do zakupu:\n\n")
                print(preview_room.update())
                print(f"Koszt lochu {preview_room.cost}")
                print(f"Obrażenia lochu {preview_room.damage}")
                print("Efekt Specjalny lochu:")
                print(preview_room.special_effect["Description"], preview_room.special_effect["Type"], preview_room.special_effect["Stat"], sep="\n")
                print("Jeśli chcesz wrócić do wcześniejszego menu wpisz \'back\'")
                for i in rooms:
                    print(i.name_room)
                choice = input()
                if choice == "back":
                    os.system("clear")
                    continue

                os.system("clear")
            elif choice[:5] == "room_":
                if rooms[int(choice[5:]) - 1].cost <= coins:
                    player_rooms.append(rooms[int(choice[5:]) - 1])
                    rooms.pop(int(choice[5:]) - 1)
                    for room in rooms:
                        room.name_room = f"room_{int(room.name_room[5:])-1}"
                    print(f"Zakupiłeś {choice}")
                    print(f"Pozostały do zakupu {rooms[0].name_room}, {rooms[1].name_room}")
                    print(player_rooms[0].update(), player_rooms[0].special_effect, player_rooms[0].damage)
                    break
                else:
                    print("Nie stać cię na ten pokój!")
                print("Wprowadziłeś numer pokoju który nie istnieje.")
                time.sleep(1)
                os.system("clear")
                continue
            else:
                print("Wprowadziłeś nie poprawne dane.")
                time.sleep(1)
                os.system("clear")
                continue
        else:
            print("Wprowadz jakis znak!")
            time.sleep(1)
            os.system("clear")
            continue



    # while len(heroes) < len(rooms) // 2:
    #     heroes.append(HeroCreator())
    # game_on = False
