def check_brackets(brackets_row: str) -> bool:
    """
    Проверьте, является ли входная строка допустимой последовательностью скобок

    :param brackets_row: Входная строка для проверки
    :return: True, если последовательность корректна, False в противном случае
    """

    if not brackets_row:
        return True
    elif brackets_row[0] == ')':
        return False

    test_row = []
    for bracket in brackets_row:

        if bracket == '(':
            test_row.append(bracket)
        else:
            if test_row:
                test_row.pop()
            else:
                return False

    return not bool(test_row)


if __name__ == '__main__':
    print(check_brackets("()()"))  # True
    print(check_brackets(")("))  # False
