# Utwórz słownik dla 10 krajów Europy zawierajacy listy 10 najpopularniejszych imion żeńskich.
# Zapisz imiona w wersji anglojęzycznej. Dodaj wszystki listy razem. Nowa lista powinna zawierać 100 elementów.
# Wyświetl tylko te imiona, które wystąpiły conajmniej w 3 krajach.

all_lists_together = []

countries = {
    'Poland': ("Sofie", "Anna2", "Anna3", "Anna4", "Anna5", "Anna6", "Anna7", "Anna8", "Ann9a", "Anna10",),
    'Germany': ("Brunhilde1", "Brunhilde2", "Brunhilde4", "Brunhilde6", "Brunhilde7", "Brunhilde8",
                "Sofie", "Brunhilde1", "Brunhilde3", "Brunhilde5",),
    'Norway': ("Helga1", "Helga2", "Helga3", "Helga4", "Helga5", "Helga6", "Helga7", "Helga8", "Helga9", "Helga10",),
    'England': ("Kate1", "Kate2", "Kate3", "Kate4", "Kate5", "Kate6", "Kate7", "Kate8", "Kate9", "Kate10",),
    'Portugal': ("Sofie", "Sofie18", "Sofie9", "Sofie0", "Sofie1", "Sofie2", "Sofie3", "Sofie4", "Sofie5", "Sofie6",),
    'Italy': ("Sofie", "Susan2", "Susan3", "Susan2", "Susan3", "Susan4", "Susan5", "Susan6", "Susan7", "Susan8",),
    'France': ("Zoe1", "Zoe2", "Zoe3", "Zoe3", "Zoe4", "Zoe5", "Zoe4", "Zoe3", "Zoe4", "Zoe5",),
    'Nederland': ("Barbara1", "Barbara2", "Barbara4", "Barbara5", "Barbara1", "Barbara3", "Barbara4", "Barbara5", "Barbara6", "Barbara7",),
    'Hungary': ("Anne1", "Anne2", "Anne3", "Anne42", "Anne41", "Anne24", "Anne2", "Anne3", "Anne54", "Anne5",),
    "Bulgaria": ("Katerine1", "Katerine2", "Katerine24", "Katerine34", "Katerine5", "Katerine4", "Katerine2", "Katerine44", "Katerine5", "Katerine6",),
}

for i in countries.values():
    all_lists_together.extend(i)

print(f"New list has {len(all_lists_together)} elements")

for index in all_lists_together:
    if all_lists_together.count(index) > 3:
        print(f'The most repeated word (more than 3 times) is {index}')
        break
