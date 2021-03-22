# Stwórz listę pomysłów na prezent dla swoich bliskich.
# Kiedy nadarzy się okazja, aby dać im prezent (święta, urodziny, rocznicę),
# program losowo wybierze jeden (i być może miejsca, w których możesz go zdobyć).

def check_if_ocasion_exist(ocasion: str):
    while ocasion not in dict_of_ocasions.keys():
        print('Im sorry, but your occasion is not in the database.\nAvailable ocasions: ')
        for key in dict_of_ocasions:
            print(key, end=" ")
        ocasion = input("\n Try again: ").capitalize()


dict_of_ocasions = {
    'Birthdays': (('Tshirt', ' Mug', 'Keyboard', 'PC mouse', 'Clothes'), ("Jerry&Tom's store", "The Pink", "ABC")),
    'Namedays': (('Jack Daniels', 'Jim Bean', 'Vodka', 'Alcohol'), ("Monopolowy", "Drunken Russian", "Indian Store")),
    'Christmas': (('Socks', 'Tshirt', 'Blouse', 'Toys'), ("Jerry&Tom's store", "Amazon", "eBay"))
}

ocasion = input("What's the ocasion? Type: ").capitalize()
check_if_ocasion_exist(ocasion)
gifts_for_ocasions = dict_of_ocasions[ocasion]

print(f'For {ocasion} you can buy: ')
for item in gifts_for_ocasions[0]:
    print(item)
print('\nAnd you can buy it in this places:')
for place in gifts_for_ocasions[1]:
    print(place)
