# Pozwól użytkownikowi wprowadzić dowolną liczbę imion ciągiem 
# (np.jako jeden string rozdzielonych przecinkiem lub białym znakiem). 
# Następnie powitaj każdą osobę na liście.

names = "Ruby, Ada,   Julia, Anna"

names = names.replace(' ', '').split(',')

for name in names:
    print("Hello", name)
