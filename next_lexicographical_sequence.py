"""
Given a string of lowercase English letters,
rearrange the characters to form a new string representing the next immediate sequence in lexicographical
(alphabetical) order. If the given string is already last in lexicographical order among all possible arrangements,
return the arrangement that's first in lexicographical order.
"""


def next_lexicographical_sequence(s: str) -> str:
    chars = list(s)
    n = len(chars)

    if n == 0:
        return ''

    i = n - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1

    if i == -1:
        return ''.join(chars[::-1])

    j = n - 1
    while chars[j] <= chars[i]:
        j -= 1

    chars[i], chars[j] = chars[j], chars[i]

    chars[i + 1:] = reversed(chars[i + 1:])

    return ''.join(chars)
