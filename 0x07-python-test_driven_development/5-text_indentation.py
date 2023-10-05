#!/usr/bin/python3
"""function
    this function breaks text
"""


def text_indentation(text="empty"):
    """text_indentation
        this function breaks text to next line
    """
    in_sentence = False
    result = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for character in text:
        if character == '.' or character == '?' or character == ':':
            in_sentence = False
            if result and result[-1] != "\n":
                result += "\n\n"
        elif character == ' ' and not in_sentence:
            continue
        else:
            result += character
            in_sentence = True
    print(result)
