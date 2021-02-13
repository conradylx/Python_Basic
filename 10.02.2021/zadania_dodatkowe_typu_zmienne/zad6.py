# Zadanie 6
# Zarówno lodówka, jak i winda mają wysokość, szerokość i głębokość. 
# Dowiedz się, ile miejsca pozostało w windzie, gdy lodówka jest w środku.
# Załóżmy, że wymiary lodówki zawsze będą mniejsze niż windy (jest to prawdopodobne)
# Wejście i wyjście powinny być zrozumiałe dla użytkownika.

venX = 100
venY = 80
venZ = 50

fridgeX = int(input("Please enter height of your fridge "))
fridgeY = int(input("Please enter width of your fridge "))
fridgeZ = int(input("Please enter length of your fridge "))

calcX = venX - fridgeX
calcY = venY - fridgeY
calcZ = venZ - fridgeZ

print("The remaining space in the elevator: {0} {1} {2}".format(calcX,calcY,calcZ))