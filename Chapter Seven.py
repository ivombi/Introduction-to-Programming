#Turtle example

import turtle

def draw_square(t,sz):
    """Make turtle t draw a square of sz."""
    for t in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Alex meets a function")
alex = turtle.Turtle() #create alex
draw_square(alex,50)   #create alex
wn.mainloop()

#Multicolor turtle

import turtle

def draw_multicolor_square(t,sz):
    """Make turtle t draw a multi-color square of sz,"""
    for i in ["red","purple","hotpink","blue"]:
        t.color(i)
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()  #set up the window and its attributes
wn.bgcolor("lightgreen")

tess = turtle.Turtle()  #Create tess and set some attributes
tess.pensize(3)

size = 20
for i in range(15):
    draw_multicolor_square(tess,size)
    size = size + 10  #Increase the size for next time
    tess.forward(10)  #Move tess along a little
    tess.right(18)    #and give her a turn
wn.mainloop()

#Functon that return values

def circle_area(r):
    """Apply the area formula for a circle of radius r"""
    area = 3.14159 * r**2
    return area
radius = input("What is your radius?")
radius = float (radius)
result = circle_area(radius)
print("The area is",result)

def find_first_2_letter_word(xs):
    for wd in xs:
        if len(wd) == 2:
            return  wd
    return ""
find_first_2_letter_word(["This","is","a","dead","parrot"])

def is_divisible(x,y):
    return x%y == 0
print(is_divisible(6,4))

#Exercises
#4.1
x = 5

def f(g):
    h = g * x
    return  h

def g(x):
    x = 178

def h(f,x):
    return f-x

def square(y):
    for i in range(1,15):
        return  x * x;
print(square(15),f(13),h(12,3),square(0))

#4.7
#a)
def print_times(s,n):
    for i in range(n):
        print(s,end="")
print_times("How are you",6)

#b)
#version 1
def print_star_line(m,n):
    for i in range(m):
        print(" ",end="")
    for i in range(n):
        print("*",end="")
    for i in range(m):
        print(" ",end="")
print_star_line(5,10)

# version 2
def print_star_line(m,n):
        print(" "*m,end="")
        print("*"*n,end="")
        print(" " * m, end="")
print_star_line(5,10)

#c

def print_star_pyramid(h):
    m = 3
    n = 1
    for i in range(h):
        print_star_line(m,n)
        print()
        m = m -1
        n = n + 2


print_star_pyramid(4)

#4.8
def number_table(m,n):
    x = 1
    for i in range(m):
        y = 1
        result = 0
        for t in range(n):
          result= x**y
          y +=1
          print(result,end=" ")
        x += 1
        print()
number_table(6,4)

#4.9
def square_check(m):
    result = m**.5
    result = result*result
    return result == m
print(square_check(15))

#4.15
def throw_die():
    import random
    r = random.randint(1,6)
    return  r
def throw_dice(n):
    sum = 0
    for i in range(n):
        sum = sum + throw_die()
    return sum
def test_dice(n,m,val):
    count = 0
    for x in range(m):
        sumcheck = throw_dice(n)
        if sumcheck==val:
            count+=1
    return count
test_dice(throw_die(),throw_die(),10)

#4.16
def draw_turtle(n):
    import turtle
    wn = turtle.Screen()
    alex = turtle.Turtle
    alex.left(90)
    alex.forward(50)
    alex.right(90)
    alex.forward(10)
    alex.right(90)
    alex.forward(50)
    wn.mainloop()

def draw_histogram(a,b,c,d,e,f):
    for i in [a,b,c,d,e,f]:
        draw_turtle(i)
draw_histogram(10,15,25,20,35,5)

#4.17
def code_guess():
    m = int(input("How many times do you want try"))
    n = int(input("Specify the length of the code to guess"))
    code = ""
    for i in range(n):
        code = code + str(throw_die())
    for x in range(m):
        print("Hint: Your code must be ",n,"digits between 1 and 6")
        print("You have ",m-x,"trials")
        guess = input("What your guess")
        if guess == code:
            print("Congradulation! Your guess",guess,"is correct")
            break
        else:
            print("Try again")
    print("You did not succeed to guess the right code")
    print("The right code is ",code)

code_guess()

#Dodona Exercises
def is_even(a):
    print(a%2==0)

is_even(-2)


def substring(sentence, n, m):
    substring = ""
    for i in range(m):
        if int(i) + n < len(sentence):
            substring += sentence[int(i) + n]
    return substring


def find_pos(word, sentence):
    len_word = len(word)
    for i in range(len(sentence)):
        if sentence[i] == word[0]:
            extract_word = substring(sentence, int(i), len_word)
            # for x in range(len_word):
            # if int(x) +int(i)<len(sentence):
            # extract_word += sentence[int(i)+int(x)]
            if extract_word == word:
                return int(i)


def in_string(word, sentence):
    pos_word = find_pos(word, sentence)
    if type(pos_word) == int:
        return True
    else:
        return False


#4.11
def create_sequence(string, index, length):
    absindex = abs(index)
    string = string * absindex
    word = "'"

    for i in range(index,-(length+absindex)):
        word = word + string[i]

    print(word, end="")

create_sequence("word", -5, 15)

#4.12
def is_prime(x):
    count = 0
    i = 1
    if x > 1:
        while i <= x:
            if x % i == 0:
                count += 1
            i += 1
        if count == 2:
            return True
        else:
           return False
    return False

def all_primes_upto(n):
    if n >1:
        i = 2
        list = []
        index = 0
        while i <=n:
            result = is_prime(i)
            if result==True:
                print(i)
                list.insert(index,i)
                index+=1
            i += 1

def factorize(n):
    primenumbers = [2,3,5,7,11,13,17,19]
    i = 0
    while n >1:
        for i in primenumbers:
            while n % i == 0:
                print(i)
                n = n //i
            i +=1


def printerval(a,b,c):
    for i in range(a,b+1):
        x = 0
        sum = 0
        y = 0
        while x<=c:
            y = i **x
            x += 1
            sum = sum + y
            print(y,end=" ")
        print("sum",sum)

printerval(5,5,4)




