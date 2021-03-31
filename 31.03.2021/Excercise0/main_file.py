from math_formulas import calculate_circle_area, calculate_rectangle_area

a, b, r = 2, 4, 6

rectangle_result = calculate_rectangle_area(a, b)
circle_result = calculate_circle_area(r)
print(f'Rectangle field: {rectangle_result}\nCircle field: {round(circle_result, 2)}')
