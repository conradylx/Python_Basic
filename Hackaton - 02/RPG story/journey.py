import json
import random
from RacesClass import Elf, Dwarf, Human, Ork

from hero_actions import *


def json_to_list():
    locations = dict()
    actions = dict()
    items = dict()
    try:
        with open("story_data.json", mode='r', encoding='utf-8') as location:
            data = json.load(location)
            for key, value in data.items():
                if key == "Locations":
                    locations[key] = value
                if key == "Actions":
                    actions[key] = value
                if key == "Items":
                    items[key] = value
            locations = list(*locations.values())
            actions = list(*actions.values())
            items = list(*items.values())
            return locations, actions, items
    except (FileExistsError, FileNotFoundError):
        print("JSON file not found.")
        quit()


def is_found_item(items, hero):
    score = random.randint(0, 100)
    if 20 < score < 90:
        item = random.choice(items)
        print(hero.name, "found", item + '!')
        hero.inventory.append(item)


def go_on_journey(hero):
    locations, actions, items = json_to_list()

    location = random.choice(locations)
    action = random.choice(actions)
    if "HERO" in action:
        action = action.replace("HERO", hero.name)

    if "attacked" in action:
        ork = Ork()
        print("You have been attacked by Ork")
        print("His skills are:\n", f'Health: {ork.health}, Attack: {ork.offence}, Defence: {ork.defence}')
        print("Your skills are:\n", f'Health: {hero.health}, Attack: {hero.offence}, Defence: {hero.defence}')
        choice = 0

        while choice != 1 or choice != 2:
            choice = int(
                input("Your hero is attacked! If you wanna fight - press 1, if you wanna flee - press 2: "))
            if choice == 1:
                hero_battle_choices(hero, ork)
            elif choice == 2:
                flee(hero)
                break
            else:
                print("Wrong choice")
    print(action + location)
    is_found_item(items, hero)


if __name__ == '__main__':
    hero = Elf("Edward")
    go_on_journey(hero)
