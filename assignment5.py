import string
import sys



alphabet = list(string.ascii_lowercase)
alphabet.append(" ")


def base_27_converter(word):
    word_len = len(word)
    letter_index = ""
    base_27_number = 0

    for letter in word:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            word_len = word_len - 1
            base_27_number += letter_index * (27 ** word_len)
    return base_27_number


def base_2_converter(base_27_number):
    remainder = ""
    base_2_number = ""
    while base_27_number > 0:
        remainder += str(base_27_number % 2)
        base_27_number = base_27_number // 2
    for i in range(len(remainder)):
        base_2_number += remainder[len(remainder) - 1 - i]
    return base_2_number


def base_2_integer_root(base_2_number):
    len_base_integer = len(str(base_2_number))

    while (len_base_integer ** 0.5 - int(len_base_integer ** 0.5)) > 0:
        base_2_number = str(0) + str(base_2_number)
        len_base_integer = len(str(base_2_number))

    return base_2_number


def bisqode(word):
    base_27_number = base_27_converter(word)
    base_2_number = base_2_converter(base_27_number)
    base_2_root = base_2_integer_root(base_2_number)
    perfect_square = int(len(base_2_root) ** 0.5)

    print_index = 0
    while print_index < len(base_2_root):
        for i in range(perfect_square):
            print(base_2_root[print_index], end="")
            print_index += 1
        print()


word = sys.argv[1]
bisqode(word)



