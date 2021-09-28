def again():
    play_again = input('Do you want to convert another number? (y/n): ')
    if play_again == 'y':
        converter()
    else:
        exit()


def converter():
    hex_table = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10,
                 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    input_number = input('Please enter a number that you want to convert: ').split()
    output_base = int(input('In which base you would like to convert: '))

    decimal = 0
    result_list = []

    # indicating whether the user input hex or not
    if '0x' in ''.join(input_number):
        figures = [i for i in ''.join(input_number)]
        del figures[:2]

        power = len(figures) - 1

        for digit in figures:  # converting hex to decimals
            decimal += hex_table[digit] * 16 ** power
            power -= 1

    # indicating whether the user input binary or not
    if '0b' in ''.join(input_number):
        figures = [i for i in ''.join(input_number)]
        del figures[:2]
        figures = list(map(int, figures))  # converting str list to int
        figures = figures[::-1]  # reversing the list

        for i in range(len(figures)):
            decimal += figures[i] * 2 ** i

    else:
        decimal = int(''.join(input_number))

    # here we converting decimal to base which user inputted in output_base
    while decimal != 0:
        remainder = int(decimal % output_base)
        decimal = int(decimal / output_base)
        result_list.append(str(remainder))

    if output_base == 16:  # blat ia ebal
        key_list = [key for key in hex_table.keys()]
        result_list = list(map(int, result_list))

        indexes = []

        # Using iteration
        for x in key_list:
            for y in key_list:
                if x == y:
                    indexes.append(key_list.index(y))

        for i, val in enumerate(result_list):
            result_list[i] = key_list[indexes.index(val)]

    final_result = ''.join(result_list[::-1])
    print(f'Result: {final_result}')
    again()


converter()