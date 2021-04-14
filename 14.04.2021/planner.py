def party_planner(cookies, people):
    leftovers = None
    num_each = None
    try:
        num_each = cookies // people
        leftovers = cookies % people
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        quit()

    return (num_each, leftovers)

if __name__ == '__main__':
    print(party_planner(10, 2))