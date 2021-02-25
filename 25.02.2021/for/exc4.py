# Napisz program, który wyświetli kolejne wyniki dla silni liczby naturalnej N
# (N podane przez użytkownika, ale nie większe niż 8).

number = int(input("Enter number: "))
result = 1

while number > 8:
    number = int(input("Enter number lower than 8: "))

'''number+1, because it's counting from 1 and stops after given number'''
for factorial in range(1, number + 1):
    result = result * factorial

print(result)
