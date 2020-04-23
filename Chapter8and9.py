#Dodona
#5.1
import string

numberlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]


def checknumber(c):
    number = 0
    for letter in c:
        if letter in numberlist:
            number += 1
    if number > 0:
        return True
    else:
        return False


def count_words(input):
    count = 0
    word_no_punct = ""
    for letter in input:
        if letter not in string.punctuation and letter not in numberlist:
            word_no_punct += letter
        elif letter in string.punctuation or letter in numberlist:
            word_no_punct += " "

    words = word_no_punct.split()
    for c in words:
        i = checknumber(c)
        if len(c) > 1 and i == False:
            count += 1
    return count

#5.3
string = input()
word = ""
count = 0

punctuation_list = "!\"#$%&'()*+,/:;<=>?@[\\]^_{|}~"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in string:
    if letter not in punctuation_list and letter in alphabet:
        word += letter
        count += 1

    else:
        if len(word) > 0 and count > 0:
            print(word, count)
            word = ""
            count = 0
if len(word) > 0 and count > 0:
    print(word, count)
    word = ""
    count = 0

#5.6
ddef replace(pattern, replacement, corpus):
    length = len(pattern)
    while pattern in corpus:
        position = corpus.find(pattern)
        newword1 = corpus[:position]
        newword2 = corpus[position+length:]
        corpus = newword1 + replacement + newword2
    return corpus

#5.7
def cleanup_spaces(string):
    newword = ""
    lenght = len(string)
    for i in range(len(string)):
        if string[i] != " ":
            newword = newword + string[i]
        elif string[i] == " " and len(newword) == 0:
            pass
        elif string[i] == " " and len(newword) != 0 and i < len(string) - 1:
            if string[i - 1] != " " and string[i + 1] == " ":
                pass
            elif string[i - 1] == " " and string[i + 1] == " ":
                pass
            elif string[i - 1] != " " and string[i + 1] != " ":
                newword += " "
            elif string[i - 1] == " " and string[i + 1] != " ":
                newword += " "

    return newword

#5.8
def convert_to_uppercase(string):
    newstring=""
    for letter in string:
        if ord(letter)>=97 and ord(letter)<=122:
            newstring = newstring +chr(ord(letter)-32)
        else:
            newstring += letter
    return newstring

#5.9
def encode(message, n):
    coded_message = ""
    for letter in message:
        if n >=0:
            if (ord(letter) + n) <= 122 and ord(letter) >= 97 and ord(letter) <= 122:
                coded_message += chr(ord(letter) + n)
            elif (ord(letter) + n) > 122 and ord(letter) >= 97 and ord(letter) <= 122:
                new_n = (ord(letter) + n) - 123
                if 97 +new_n<=122:
                    coded_message += chr(97 + new_n)
                else:
                    new_n = 97 + (123-(97+new_n))
                    coded_message += chr(new_n)
            elif ord(letter) > 122 or ord(letter) < 97:
                coded_message += letter
        elif n <0:
            new_n= 26+n
            if (ord(letter) + new_n) <= 122 and ord(letter) >= 97 and ord(letter) <= 122:
                coded_message += chr(ord(letter) + new_n)
            elif (ord(letter) + new_n) > 122 and ord(letter) >= 97 and ord(letter) <= 122:
                new_n2 = 96+((ord(letter) + new_n) - 122)
                coded_message += chr(new_n2)
            elif ord(letter) > 122 or ord(letter) < 97:
                coded_message += letter
    return coded_message

def decode(message, n):
    decode_message = ""
    for letter in message:
        if n >=0:
            if (ord(letter) - n) >= 97 and ord(letter) >= 97 and ord(letter) <= 122:
                decode_message += chr(ord(letter) - n)
            elif (ord(letter) - n) < 97 and ord(letter) >= 97 and ord(letter) <= 122:
                new_n = 97-(ord(letter)-n)
                decode_message += chr(123 - new_n)
            elif ord(letter) > 122 or ord(letter) < 97:
                decode_message += letter
        elif n <0:
            new_n= 26+n
            if (ord(letter) - new_n) >= 97 and ord(letter) >= 97 and ord(letter) <= 122:
                decode_message += chr(ord(letter) - new_n)
            elif (ord(letter) - new_n) <96 and ord(letter) >= 97 and ord(letter) <= 122:
                new_n = 97-(ord(letter)-new_n)
                decode_message += chr(123-new_n)
            elif ord(letter) > 122 or ord(letter) < 97:
                decode_message += letter
    return decode_message
encode("alphabet: from a to z", 33)


def is_palindrome_sentence(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    length = 0
    newsentence = ""
    result = ""
    for letter in sentence:
        if letter in alphabet:
            length += 1
            newsentence += letter
    midpoint = length // 2
    if len(newsentence)>0:
        for i in range(midpoint):
            if newsentence[i].lower() == newsentence[len(newsentence) - 1 - i].lower():
                result = True
            else:
                result = False
                return result
        return result
    return True


is_palindrome_sentence("A man, a plan, not a canal: Panama.")





