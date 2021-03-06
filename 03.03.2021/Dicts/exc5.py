# W wierszu policz wystąpienie każdego wyrazu, zignoruj wielkość liter.
#
# """Szybko, zbudź się, szybko, wstawaj
# Szybko, szybko, stygnie kawa
# Szybko, zęby myj i ręce"""
#
# Zadbaj o sposób wyświetlania np.:
#
#     szybko : 5
#
#     zbudź : 1

text = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""

text = text.replace(",", "")
text = text.split()
text_to_dict = {}

for word in text:
    if word in text_to_dict.keys():
        text_to_dict[word] = text_to_dict[word] + 1
    else:
        text_to_dict[word] = 1

for key, value in text_to_dict.items():
    print(key, value)
