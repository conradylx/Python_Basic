def display_month(data):
    months_dict = dict(data)

    for month, days in months_dict.items():
        print(month)
        for day in days:
            print('{:3}'.format(day), end=" ")
            if day == 6 or day == 13 or day == 20 or day == 27:
                print()
        print('\n')

data = [
    ('January', range(31)),
    ('February', range(28)),
    ('March', range(31)),
    ('April', range(30)),
    ('May', range(31)),
    ('June', range(30)),
    ('July', range(31)),
    ('August', range(31)),
    ('September', range(30)),
    ('October', range(31)),
    ('November', range(30)),
    ('December', range(31)),
]

display_month(data)