"""
Palindrom to wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej
np.: Kobyła ma mały bok. Pozwól użytkownikowi wprowadzić dowolne zdanie.
Następnie sprawdź czy wprowadzone wyrażenie jest palindromem.
"""
text = input("Enter text ").replace(" ", "").lower()
print('Palindrome?',text[::] == text[::-1])