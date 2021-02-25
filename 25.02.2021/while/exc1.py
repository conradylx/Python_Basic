#Napisz program zmieniający skalę w stopniach Fahrenheita na naszą w Celcjuszach.
#     Program powinen wykonać się w pętli od 0 do 200 stopni Fahrenheit, co 20 stopni.
#     C = 5/9 * (F - 32) # wzór Celsjusz → Fahrenheit
# Napisz rozwiązanie zarówno z użyciem pętli while jak i for.

farenheit = 0

while farenheit <= 200:
    celcius = 5/9 * (farenheit - 32)
    farenheit += 20
    print(farenheit, "stopni Farenheita =", round(celcius, 2), "stopni Celsjusza")