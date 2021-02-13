# Zadanie 7
# Napisz konwerter walut.
# Program poprosi użytkownika o kwotę pieniędzy, jaką wezmą na wakacje
# a następnie przeliczy tę kwotę w euro oraz w dolarach.
# Zignoruj wszelkie centy, które mogą wyniknąć z konwersji.
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

amount = float(input("Enter amount of cash to withdraw "))
euro = int(amount/4.20)
dollar = int(amount/4.60)

print("Amount converted to euro is {0} EUR and converted to dollars {1} USD".format(euro, dollar))