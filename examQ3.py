#Author: Kubam Ivo
#Date: 06/16/2019

list_word = []

def possiblewords(string,m,letter):
    letter = int(letter)
     m = int(m)
    """Produce all possible words from a given word of length m"""
    word = ""
    for i in range(len(string)):
        if len(word)<=m and int(i)!=letter:
            word += string[i]

    return word

def comparing_word (list):



def all_palindromes(string, m):
    """Creating The main function"""
    if m >= len(string):
        for i in range(len(string)):
            list_word.append(possiblewords(string,m,i))
    for elem in list_word:
        if


for i in  range (2001,3200):
    if int(i)%7==0 and int(i)%5!=0:
        print(i,",",end="")

number = int(input())

def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
print(factorial(number))

number = 9
def sum_numbers(number):
    if number == 1:
        return 1
    else:
        return number + sum_numbers(number-1)
print(sum_numbers(number))

number = 6
def sum_numbers(number):
    if number == 0:
        return 0
    else:
        return number + sum_numbers(number-2)
print(sum_numbers(number))


def time_table(number):
    for i in range(1,11):
        result = int(i)*number
        print(str(i) , "x" , str(number),"=",result)

time_table(12)

def common_char(string1, string2):
    """"Function get common unique characters from both strings"""
    char_list = []
    for char in string1:
        if char not in char_list:
            if char in string2:
                char_list.append(char)
    return len(char_list)
print(common_char("bee","peer"))





