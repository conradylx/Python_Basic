from RacesClass import Human, Elf, Dwarf
from journey import go_on_journey
from hero_actions import check_inventory


def introduce_hero(hero):
    print(f"You're {hero.race} named {hero.name} and your skills are:")
    print(f"Health: {hero.health}\nAttack: {hero.offence}\nDefence: {hero.defence}")


def main_Function():
    counter = 1

    hero_name = input("What's your name? ")

    while True:
        hero_race = input("You're... [Pick your race: Human/Elf/Dwarf ").capitalize()
        if hero_race == "Human":
            hero = Human(hero_name)
            break
        elif hero_race == "Elf":
            hero = Elf(hero_name)
            break
        elif hero_race == "Dwarf":
            hero = Dwarf(hero_name)
            break

    introduce_hero(hero)

    while counter != 6:
        journey_choice = int(input("What are you want to do?\n1-Check your inventory\n2-Go for next journey\n3-Quit\n"))
        print(journey_choice)
        if journey_choice == 1:
            check_inventory(hero)
        if journey_choice == 2:
            go_on_journey(hero)
        if journey_choice == 3:
            quit()
        counter += 1
    print("Story is over. To play launch the game again.")


if __name__ == '__main__':
    main_Function()
