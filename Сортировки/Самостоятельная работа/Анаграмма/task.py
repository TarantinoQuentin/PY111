def is_anagram(s: str, t: str) -> bool:

    if len(s) != len(t):
        return False

    deconstructed_s_sting = {}
    for char in s:
        if char in deconstructed_s_sting:
            deconstructed_s_sting[char] += 1
        else:
            deconstructed_s_sting[char] = 1

    deconstructed_t_sting = {}
    for char in t:
        if char in deconstructed_t_sting:
            deconstructed_t_sting[char] += 1
        else:
            deconstructed_t_sting[char] = 1

    if deconstructed_s_sting == deconstructed_t_sting:
        return True
    return False

    # Решение учителя:
    # if len(s) != len(t):
    #     return False
    #
    # s_dict = {}
    # t_dict = {}
    # for i in range(len(s)):
    #     if s[i] in s_dict:
    #         s_dict[s[i]] += 1
    #     else:
    #         s_dict[s[i]] = 1
    #
    #     if t[i] in t_dict:
    #         t_dict[t[i]] += 1
    #     else:
    #         t_dict[t[i]] = 1
    #
    # return s_dict == t_dict
