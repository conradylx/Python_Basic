"""
Jak sprawdzić czy ciąg znaków składa się tylko z cyfr?
"""
text = "323"
print(text.isdigit())
"""
Jak wyświetlić wyśrodkowany tekst o zadanej
szerokości i dodatkowo puste miejsca wypełnić np.
gwaizdką - '***mata***"""

sec_text = "mata"
print(sec_text.center(10, "*"))

"""
Jaka metoda usunie znaki po prawej stronie?
"""

third_text = "jakiś_text"
print(third_text.rstrip("_text"))

"""
Jak sprawdzić czy ciąg posiada jedną wielką literę?
"""

fourth_text = "IsUpper?"
print(fourth_text.isupper())

"""
Policzy ile razy zadany ciąg znaków np.('na') wystąpił w ciągu znaków ('banana' = 2)
"""

fifth_text = "banana"
print(fifth_text.count("na"))
