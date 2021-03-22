# Ogrodnik. Utwórz program - udający poradnik ogrodnika.
# Powinien zawierać dowolny słownik przypominający o obowiązkach ogrodniczych w zależności od miesiąca.
# np. styczeń - bielenie pni drzew, październik - czas posadzić wiosenne krzewy.
# Użytkownik może podać skróconą, 3 literową nazwę miesiąca i otrzymać poradę.
# Użytkownik kończy korzystanie z programu naciśnięciem przycisku - Q.

def ask_for_tips(months_duties):
    user_ask = input("Give me month to show tip for you: ")
    for month, tip in months_duties.items():
        if month.startswith(user_ask[:3]):
            return  tip

months_duties = {
    'January': 'Whitewashing of tree trunks ',
    'February': 'Buy vegetable seeds',
    'March': 'Re-fertilize the soil',
    'April': 'Buy garden fertilizer',
    'May': 'Check the greenhouse',
    'June': 'Harvest the crops',
    'July': 'Collect the strawberries',
    'August': 'Plow the field',
    'September': 'Collect the apples',
    'October': 'Plant spring shrubs',
    'November': 'Prepare the greenhouse for the winter',
    'December': 'Secure the trees',
}


tip = ask_for_tips(months_duties)
if tip == None:
    print("Nothing to show, because you typed wrong month's name. Try again!")
else:
    print(tip)