# Pobierz od użytkownika dowolny tekst i wyświetl tylko te znaki, które są na pozycjach parzystych. 
# Wykonaj na dwa sposoby - za pomocą pętli oraz przez sting slicing ( ‘abrakadabra’ -> ‘baaar’).

text = input("Enter text: ")

'''Using For loop'''
for i in range(0, len(text), 2):
    print(text[i], end="")

'''Using slicing'''
print(text[0::2])
