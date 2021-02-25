# W podanym przez użytkownika ciągu wejściowym policz wszystkie małe litery, wielkie litery, cyfry i znaki specjalne.

text = input("Enter text: ")

lo_letters = 0
hi_letters = 0
sp_letters = 0
digits = 0

for i in range(len(text)):
    if text[i].isdigit():
        digits += 1
    elif text[i].islower():
        lo_letters += 1
    elif text[i].isupper():
        hi_letters += 1
    else:
        sp_letters += 1

print("Your word", text, "contains:")
print("Lower letters:", lo_letters)
print("Upper letters:", hi_letters)
print("Digits:", digits)
print("Special characters:", sp_letters)
