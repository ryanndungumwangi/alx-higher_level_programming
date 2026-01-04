#!/usr/bin/python3
for letter in 'abcdefghiklmnopqrstuvwxyz':
    if letter == 'e' or letter == 'q':
        continue
    print("{}".format(letter), end="")
