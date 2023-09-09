#!/usr/bin/python3
"""prints text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """indents text

    Args:
        text (char): only argument

    Return:
        Prints texts with identation
    """
    tokens = []
    start = 0
    delim = ".?:"

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while start < len(text):
        end = len(text)

        for ch in delim:
            ch_idx = text.find(ch, start)
            if ch_idx != -1 and ch_idx < end:
                end = ch_idx + 1

        tokens.append(text[start:end].strip())
        start = end

    for idx in range(len(tokens)):
        if idx < len(tokens) - 1:
            print(tokens[idx])
            print()
        else:
            print(tokens[idx], end="")
