# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

distance = float(input("Enter distance "))
burning = float(input("Enter burning "))
price = float(input("Enter price "))

result = (distance * burning) / 100 * price
print(result)
