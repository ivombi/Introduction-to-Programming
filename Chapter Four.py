import turtle #Importing turtle
wn = turtle.Screen() # creates a playground for turtle
wn.bgcolor("lightgreen") # changing the windows backgroound color
wn.title("Hello, Tess!") # set the window title


alex = turtle.Turtle() #creates a turtle assign to alex
alex.forward(50) # tell alex to move forward by 50 units
alex.left(90) # Tell alex to turn by 90 degrees
alex.forward(30) # complete the second side of a rectangle
alex.color("red")
alex.pensize(3) #Tell alex to set her pen width

wn.mainloop() #waiting for user to close window

##Extending the turtle program

import  turtle
wn = turtle.Screen()
wn_color = input("What your background color") # requesting users background color
wn.bgcolor(wn_color) # setting bacground color
wn.title("Turtle game") # setting the title of the window

tess = turtle.Turtle() # creating tess
tess_color = input("Which color do you want for turtle")  # requesting tess color
tess.color(tess_color) # setting up tess color
tess_pen_width = int(input("What size do you want for your turtle")) # requesting pen width
tess.pensize(tess_pen_width)  # setting up tess pen width

#Moving tess around
tess.forward(50) # tell alex to move forward by 50 units
tess.left(90) # Tell alex to turn by 90 degrees
tess.forward(30) # complete the second side of a rectangle

wn.mainloop()

## Instances - a herd of turtles
import turtle #Importing turtle
wn = turtle.Screen() # creates a playground for turtle
wn.bgcolor("lightgreen") # changing the windows backgroound color
wn.title("Tess & Alex") # set the window title

tess = turtle.Turtle()
tess.forward(110) # tell alex to move forward by 50 units
tess.left(120) # Tell alex to turn by 120 degrees
tess.forward(80) #
tess.left(120)
tess.forward(80)
tess.left(120)
tess.right(180) # turn tess around
tess.forward(80) # Move tess away from the oriing)

wn.mainloop() #waiting for user to close window


##4.3 The For loop
for f in["Joe","Zoe","Brad","Angelina","Zuki","Thandi","Paris"]:
    invite = "Hi " + f + ". Please come to my party on saturday!"
    print(invite)

## The loop turtle

for i in[0,1,2,3]:
    alex.forward(50)
    alex.left(90)


## Strings
s = "desserts"
for i in range(len(s)):
    print(s[i],end="")

#Printing in reverse order
s = "desserts"
for i in range(len(s)):
    print(s[len(s)-1-i],end="")

##Turle final example
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle() # creating an instance of the Turtle class
tess.shape("turtle")
tess.color("blue")


size = 20
for i in range(30):#0,1,2...29
    tess.stamp() # Leave an impression on  the canvas
    size = size + 3 #Increase the size on every iteration
    tess.forward(size)
    tess.right(24)
wn.mainloop()

##Exercises
 #2.1
 for value in [1,9]:
     print("step")

 for x in range(2):
     print("step")

for y in range(5,8):
    print("step")

for i in range(1,3):
    for j in ["a","b","c"]:
        print("step")
#2.2
x = int(input())
for i in range(x):
    print(i+1)

#2.3

for x in [12,10,32,3,66,17,42,99,20]:
    print(x)


sum = 0
sumsquare = 0
product = 1
for x in  [12,10,32,3,66,17,42,99,20]:
    print(x)
    print(x*x)
    product = product *x
    sum = sum + x
    sumsquare = sumsquare +(x*x)
print("Total for numbers = ",sum)
print("Total for squre of numbers = ",sumsquare)
print("Product of numbers = ",product)

#2.4
x = input()
lenx = len(x)
lenxdiff = 9-lenx
if lenxdiff>0: print("0"*lenxdiff+x)
    else: print(x)

#2.5
import turtle
wn = turtle.Screen()  # creates a playground for turtle
alex = turtle.Turtle()  # creates a turtle assign to alex
alex.color("red")

n=int(input())

for x in range(n):
    alex.forward(80) # tell alex to move forward by 50 units
    alex.left(360/n) # Tell alex to turn by 90 degrees

wn.mainloop() #waiting for user to close window

#2.6
import turtle
wn = turtle.Screen()
alex = turtle.Turtle

n = int(input())
for x in range(n):
    alex.forward(80)  # tell alex to move forward by 50 units
    alex.left(360/n)  # Tell alex to turn by 90 degrees
wn.mainloop()


#2.7
x = int(input())
for i in range(11):
    result = x * i
    print(x , " times " , i , " = " , result)

for x in ["A","C","G","T"]:
    for y in ["A","C","G","T"]:
        for z in ["A","C","G","T"]:
            print(x,y,z)

import turtle
wn = turtle.Screen()
alex = turtle.Turtle

n = int(input())
for x in range(n):
    alex.left(360/n)  # Tell alex to turn by 90 degrees
    alex.forward(10)  # tell alex to move forward by 50 units

wn.mainloop()


###Dodona Exercises
#1
x = int(input())
y = int(input())
z = 0
for r in range(x):
    for c in range(y):
        z = z +1
        print(z,end=" ")
    print()

#2
x = int(input())
sum=0
for i in range(x+1):
    sum = sum +i
print(sum)

#3
x = int(input())
pdt=1
for i in range(x):
    pdt = pdt*x
print(pdt)

#factorial
x = int(input())
factorial = 1
for i in range(x):
    factorial = factorial*x
    x = x -1
print(factorial)

#2.12 factorial coef
x = int(input())
y = int(input())
factorialx = 1
factorialy = 1
z = x -y
factorialz = 1
for i in range(x):
    factorialx = factorialx * x
    x -= 1
for i in range(y):
    factorialy = factorialy * y
    y -= 1
for i in range(z):
    factorialz = factorialz * z
    z -= 1
total = int(factorialx/(factorialz*factorialy))
print(total)

#2.12b factorial sum
a = 1
factorial_total = 0
factorial = 1
x = int(input())
y = x
z = x
while a <=z:
    x = y
    for i in range(y):
        factorial = factorial * x
        x = x - 1
    a += 1
    factorial_total +=factorial
    factorial = 1
    y -= 1
print(factorial_total)

#2.12c
n = int(input())
m = n = z
while m <= z:
    for i in range (n)