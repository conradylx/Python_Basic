# Stwórz listę składającą się z kilku elementów różnego typu np. [13, ‘string’, 2.45] itp.
# W pętli spróbuj wykonać dzielenie 10 przez wartość z listy.
# Złap wyjątki jakie mogą się przy tej okazji wydarzyć.

example_list = [13, 'string', 2.45, False, True, [], {'key': 4}]

for iteration in range(len(example_list)):
    try:
        result = 10 / example_list[iteration]
        print(result)
    except ZeroDivisionError:
        print("Can't divide by zero.")
    except TypeError:
        print("You can divide only numeric types.")