# Program przechowujący danę kontaktowe znajomych/klientów.
#
# Program wyświetla menu wypisujące komendy jakie należy wpisać, aby program wykonał dane zadanie. Zadania to:
# Wyświetlenie wszystkich wpisów
# Stworzenie nowego wpisu (dane wczytywane z klawiatury)
# Usunięcie wpisu
# Zakończenie pracy programu
# Program powinien na starcie mieć już wprowadzone kilka wpisów.

def show_all_records(list):
    for key, value in list.items():
        print("Name:", key, "Phone no:", value)


def add_new_record(list):
    new_new = input("Please enter name of new record ")
    new_phone_no = int(input("Please enter new phone number of new record "))
    list[new_new] = new_phone_no
    print("Your new contact has been added")
    return list


def remove_record_from_contact(list):
    user_input = input("Please enter name of your contact to remove from dictionary ")
    if user_input in list:
        del list[user_input]
    else:
        print(f'{user_input} is not in your contacts')
    return list


data_list = {"Jan": 433122345, "Kamil": 333222111, "Anna": 999333884}
print("Type /show to show all the records, /add to add new record, /remove to remove contact")
user_input = ""

while user_input != "/end":
    user_input = input("Your input: ")

    if user_input == "/show":
        show_all_records(data_list)
    elif user_input == "/add":
        data_list = add_new_record(data_list)
    elif user_input == "/remove":
        data_list = remove_record_from_contact(data_list)