from journey import *


def decorator(show_items):
    def wrapper(hero):
        print('-------------------------------------------')
        show_items(hero)
        print('-------------------------------------------')

    return wrapper


@decorator
def show_items(hero):
    print(f'Your inventory: {", ".join(hero.inventory)}')


def check_inventory(hero):
    item = None
    choice = None

    while choice != 3:
        show_items(hero)
        choice = int(input(
            'If you want remove something from your inventory press 1,\n'
            'if you have potion and you want to use it press 2,\n'
            'if you want to quit inventory press 3.\n'))

        if choice == 2 and "Potion" in hero.inventory:
            hero.inventory.remove("Potion")
            hero.health += 40
            print(f"You healed yourself by 40 healthpoints.\nYour actual health is {hero.health}")
        elif choice == 2 and "Potion" not in hero.inventory:
            print("You have no potion in your inventory")
        elif len(hero.inventory) == 0:
            print('Your inventory is empty')
            break
        elif choice == 1:
            item = input("Enter item's name: ")
            if item in hero.inventory:
                hero.inventory.remove(item)
                if len(hero.inventory) == 0:
                    print(f'You removed {item} from your inventory.\nYour inventory is empty.')
                else:
                    print(f'You removed {item} from your inventory.\nYour inventory is {hero.inventory}.')
            else:
                print(f'{item} is not in your inventory.')


def enemy_attack(hero, enemy):
    print('--------------------------------------------------------------------')
    print(f"It's Ork's turn to attack!")
    enemy.attack(hero)
    if hero.defence < enemy.offence:
        print(f'Ork attacked you with {abs(hero.defence - enemy.offence)} points. Your health is {hero.health} left.')
    print('--------------------------------------------------------------------')


def hero_battle_choices(hero, enemy):
    while hero.health > 0 and enemy.health > 0:
        decision = int(input('If you want to attack, press 1, if you want to flee press 2'))

        if decision == 1:
            hero.attack(enemy)
            print(
                f'You attacked enemy with {abs(enemy.defence - hero.offence)} points.'
                f'Orks health is {enemy.health} left.')
            if enemy.health <= 0:
                print("Victory! Ork is dead.")
                break

        enemy_attack(hero, enemy)
        if hero.health <= 0:
            print('Game over. You are dead.')
            quit()

        if decision == 2:
            flee(hero)
            break


def flee(hero):
    print("You flee, but you take -5 healthpoints")
    hero.health -= 5


if __name__ == '__main__':
    hero = Elf("Alen")
    ork = Ork()
    hero.inventory.append("Sword")
    check_inventory(hero)
    hero_battle_choices(hero, ork)
