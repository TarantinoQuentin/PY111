import operator


def calc_algorithm(example: str) -> int:
    """
    Функция-алгоритм для линейного решения
    математических примеров
    :param example: Передаваемый пример в виде строки
    :return: Число, результат решения
    """

    operand_priority = {'+': 1, '-': 1,
                        '*': 2, '/': 2,
                        '(': 3, ')': 3,
                        '^': 4}

    operands_translator = {"+": operator.add,
                           "-": operator.sub,
                           "*": operator.mul,
                           "/": operator.truediv,
                           "^": operator.pow}

    digits_stack = []
    operand_stack = []
    current_priority = 0
    priority_reduction = False
    brackets_case = False
    previous_index = -2

    for index, current_char in enumerate(example):
        if priority_reduction is True:
            if brackets_case is False:
                operand = operands_translator[operand_stack.pop(operand_stack[previous_index])]
                first_digit = digits_stack.pop(digits_stack[previous_index])
                second_digit = digits_stack.pop()
                term_result = operand(int(first_digit), int(second_digit))
                digits_stack.append(term_result)
                priority_reduction = False
        if current_char.isdigit():
            digits_stack.append(current_char)
        else:
            if current_char == '(':
                operand_stack.append(current_char)
                current_priority = 0
                brackets_case = True
                continue
            if current_char == ')':
                brackets_case = False

                operand_stack[::-1].remove('(')
                continue
            if operand_priority[current_char] > current_priority:
                current_priority = operand_priority[current_char]
                operand_stack.append(current_char)
            else:
                operand_stack.append(current_char)






            if current_char == '(':
                brackets_case = True
                continue
            elif current_char == ')':
                brackets_case = False
                continue