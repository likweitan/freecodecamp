import re


def arithmetic_arranger(problems, is_answer=False):
    arranged_problems = ""
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    digits = []
    operands = []
    results = []
    spaces = []

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for equation in problems:
        find_word = re.findall(r'\w', equation)
        # print(find_digit)
        for find_result in find_word:
            try:
                val = int(find_result)
            except ValueError:
                return 'Error: Numbers must only contain digits.'

        x = re.findall('[0-9]+', equation)
        digits.append(x)
        find_x = equation.find('+')
        find_y = equation.find('-')
        if find_x == -1 and find_y == -1:
            return "Error: Operator must be '+' or '-'."
        elif find_x >= 0:
            operands.append('+')
        elif find_y >= 0:
            operands.append('-')

    for digit in digits:
        number_1 = int(digit[0])
        number_2 = int(digit[1])
        max_length = 2.

        if len(digit[0]) > 4 or len(digit[1]) > 4:
            return "Error: Numbers cannot be more than four digits."

        if number_1 > number_2:
            max_length = int(max_length + len(digit[0]))
        elif number_2 > number_1:
            max_length = int(max_length + len(digit[1]))
        spaces.append(max_length)

        # Calculations
        if operands[digits.index(digit)] == '+':
            result = number_1 + number_2
        elif operands[digits.index(digit)] == '-':
            result = number_1 - number_2
        results.append(result)

        leading_spaces_1 = int(max_length - len(digit[0]))
        leading_spaces_2 = int(max_length - len(digit[1]) - 1)
        leading_spaces_4 = int(max_length - len(str(result)))
        line_1 = line_1 + ' '*leading_spaces_1 + digit[0] + ' '*4
        line_2 = line_2 + \
            operands[digits.index(digit)] + ' ' * \
            leading_spaces_2 + digit[1] + ' '*4
        line_3 = line_3 + '-'*max_length + ' '*4
        line_4 = line_4 + ' '*leading_spaces_4 + str(result) + ' '*4

    arranged_problems = line_1[:-4] + '\n' + line_2[:-4] + '\n' + line_3[:-4]
    if is_answer == True:
        arranged_problems += '\n' + line_4[:-4]
    return arranged_problems
