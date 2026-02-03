from typing import List


# def replace_words(dictionary: List[str], sentence: str) -> str:
#
#     # Не смог решить до конца правильно, решение из интернета:
#     root_set = set(dictionary)
#     words = sentence.split()
#
#     for i in range(len(words)):
#         word = words[i]
#         for j in range(1, len(word) + 1):
#             prefix = word[:j]
#             if prefix in root_set:
#                 words[i] = prefix
#                 break
#
#     return " ".join(words)


# Решение преподавателя:
def replace_words(dictionary: List[str], sentence: str) -> str:
    trie = {}
    for word in dictionary:
        node = trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["#"] = word

    words = sentence.split()
    for i, word in enumerate(words):
        node = trie
        prefix = ""
        for char in word:
            if char not in node:
                break
            prefix += char
            node = node[char]
            if "#" in node:
                words[i] = node["#"]
                break

    return " ".join(words)
