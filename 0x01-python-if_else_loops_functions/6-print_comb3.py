#!/usr/bin/python3
for number in range(10):
    for i in range(10):
        if number != i :
            print(f'{i:02}', end=' ,', flush=True)
