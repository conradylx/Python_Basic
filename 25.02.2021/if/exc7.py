# Rozwiń kod bmi.py z pierwszych zajęć dodając teraz instrukcję warunkową,
# która wyświetli w zależności od wyniku: niedowaga / waga normalna / nadwaga / otyłość.

mass = int(input('Podaj swoją wagę w kg:'))
height = float(input('Podaj swój wzrost:'))
BMI = mass / (height ** 2)
BMI_rounded = round(BMI, 2)
print('Moje BMI ', BMI_rounded)

if BMI_rounded < 16:
    print("Niedowaga")
elif BMI_rounded >= 16 and BMI_rounded < 25:
    print("Waga normalna")
elif BMI_rounded >= 25 and BMI_rounded < 30:
    print("Nadwaga")
elif BMI_rounded >= 30:
    print("Otyłość")
