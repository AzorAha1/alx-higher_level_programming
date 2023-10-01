#!/usr/bin/python3
def text_indentation(text):
    for i in range(len(text)):
        if text[i] == '.':
            print('\n')
        print(text[i], end="") 