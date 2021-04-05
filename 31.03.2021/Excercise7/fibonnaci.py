def calc_fibonnaci_numbers(number: int) -> list:
    sum = 0
    latest = 1
    final_list = [0]
    for i in range(number):
        temp = sum
        sum += latest
        latest = temp
        final_list.append(sum)
    return final_list


if __name__ == '__main__':
    print(calc_fibonnaci_numbers(20))
