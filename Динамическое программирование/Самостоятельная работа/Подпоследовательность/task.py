def is_subsequence(s: str, t: str) -> bool:

    previous_target_index = -1
    for current_char in s:
        if not current_char in t:
            return False
        elif t.index(current_char) > previous_target_index:
            previous_target_index = t.index(current_char)
        else:
            return False

    return True

    # Решение учителя:
    # i, j = 0, 0
    # while i < len(s) and j < len(t):
    #     if s[i] == t[j]:
    #         i += 1
    #     j += 1
    # return i == len(s)

    # Решение из интернета:
    # it = iter(t)
    # return all(char in it for char in s)
