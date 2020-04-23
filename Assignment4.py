import sys

type = sys.argv[1]
n = int(sys.argv[2])
m = int(sys.argv[3])
word = sys.argv[4]

import string
def encode(n, m, word):
    alphabet = list(string.ascii_lowercase)
    first = "Yes"
    shift = 0
    encode_word = ""
    for letter in word:
        let_pos = 0
        if letter in alphabet and first == "Yes":
            first = "No"
            shift = n + m
            let_pos = alphabet.index(letter)
            new_position = int(let_pos) + int(shift)
            if new_position > 25:
                new_position = new_position - 26
                encode_word += alphabet[new_position]
            else:
                encode_word += alphabet[new_position]
        elif letter in alphabet and first == "No":
            shift = n + new_position
            let_pos = alphabet.index(letter)
            new_position = int(let_pos) + int(shift)
            if new_position > 25:
                new_position = new_position - 26
                encode_word += alphabet[new_position]
            else:
                encode_word += alphabet[new_position]
        else:
            encode_word += letter
    return encode_word


def decode(n, m, word):
    alphabet = list(string.ascii_lowercase)
    first = "Yes"
    shift = 0
    decode_word = ""
    for letter in word:
        let_pos = 0
        if letter in alphabet and first == "Yes":
            first = "No"
            shift = n + m
            new_position = alphabet.index(letter)
            original_pos = new_position - int(shift)
            if original_pos < 0:
                original_pos = original_pos + 26
                decode_word += alphabet[original_pos]
            else:
                decode_word += alphabet[original_pos]
        elif letter in alphabet and first == "No":
            shift = new_position + n
            new_position = alphabet.index(letter)
            original_pos = new_position - shift
            if original_pos < 0:
                original_pos = original_pos + 26
                decode_word += alphabet[original_pos]
            else:
                decode_word += alphabet[original_pos]
        else:
            decode_word += letter

    return decode_word

def sapher(type,n,m,word):
    result = ""
    if type=="encode":
        result = encode(n,m,word)
        print(result)
    elif type== "decode":
        result = decode(n,m,word)
        print(result)

sapher(type,n,m,word)






