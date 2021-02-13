# print("*")
# print("**")
# print("***")
# print(" ")
# for i in range(1,4):
#     print("*"*i)

mass = int( input('Podaj swoją wagę w kg:') )
height = float(input('Podaj swój wzrost:'))
BMI = mass / (height ** 2)
BMI_rounded = round(BMI, 2)
print('Moje BMI ', BMI_rounded)
