def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        rome = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
    else:
        return 0
    result = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and rome[roman_string[i]] < rome[roman_string[i + 1]]:
            result -= rome[roman_string[i]]
        else:
            result += rome[roman_string[i]]
    return result
