import math
x = -2
if x < 0 :
    print("The negative number ", x , " is not valid here.")
    x=42
    print("I've decided to use the number 42 instead.")
print("The square root of ", x, "is", math.sqrt(x))

n = 1001
running_total = 0
for x in range(n):
    running_total = running_total + x
print(running_total)

#The collatz 3n + 1 sequence
n = int(input())
while n != 1:
    print(n, end=", ")
    if n%2 == 0: # n is even
        n = n // 2
    else:
        n = n * 3 +1 #n is odd
print(n,end=".\n")


###Exercises
#3.4
s = input("Give a word: ")
if (len(s)>0 and "A" <=s[0] and s[0]<="Z"):
    print("Starts with capital letter")

#3.5
i = int(input("Give a number: "))
if(i<4):
  print(i, "is smaller that 4")
elif(i==4):
  print(i,"is equal to 4")
else:
  print(i, "is larger than 4")

# 3.6
mark = int(input("Enter exam mark: "))
if (mark<40):
    grade = "F3"
    print("Your grade is :", grade)
elif (mark>=40 and mark<45):
    grade = "F2"
    print("Your grade is :", grade)
elif (mark>=45 and mark<50):
    grade = "F1 Supp"
    print("Your grade is :", grade)
elif (mark>=50 and mark<60):
    grade = "Third"
    print("Your grade is :", grade)
elif (mark>=60 and mark<70):
    grade = "Second"
    print("Your grade is :", grade)
elif (mark>=70 and mark<75):
    grade = "Upper Second"
    print("Your grade is :", grade)
elif (mark>=75):
    grade = "First"
    print("Your grade is :", grade)
else: pass

#3.8
n = 0
while n<90:
    print(n,end=" ")
    n += 1

#3.8b

for i in range(20):
    if ((i%2 !=1)): # odd number
        i = i +2
        if(i>10):
            print("Large")
            break
        else:
            print("small")
            continue
    else:
        pass

#3.8c
i = int(input("Give number: "))
while i <1000:
    if i < 50:
         print("small")
         i = int(input("Give number: "))
print("Large!")
print("Retry")

#3.9f
i = 5
cont = True
while (not (i > 10 and cont)):
    print("step")
    cont = i % 5 == 0
    print("step")
    i = i + 1
print("step")

#3.10
sum = 0
response = int(input("Enter first number"))
while sum <= 12987:
    sum += response
    response = int(input("Enter next number"))
    print("Your current total is ", sum)
print("The total of all your is ",sum)

#3.14
s = input("Enter a palindrome word")
len(s)
s[0 + 0]
s[len(s)-0]

print(s, " is a palindrome word")



#3.17
import random
x = int(input("choose your mininum number"))
y = int(input("Choose a maximum number"))

guesses = 0
msg = ""
n = random.randrange(x,y)

while True:
    guess = int(input(msg + "\n""What your guess"))
    guesses += 1
    if guess > n:
        msg += str(guess) + " is too high. \n"
    elif guess < n:
        msg += str(guess) + " is too low. \n"
    else:
        break
print("\n\nGreat, you got it",guesses, "guessess")

# Dodona exercises
#3.7
x = int(input())
if ((x%4==0 and x%100!=0) or (x%100==0 and x%400==0)):
    print(x," is a leap year")
else:
    print(x, " is not a leap year")

#3.11a
word = input()
for i in range(len(word)):
    print(word[len(word)-1-i],end="")
print()

3.11b
word = input()
output=""
for i in range(len(word)):
    output+=word[len(word)-1-i]
if word == output:
    print(word,"is a palindrome")
else:
    print(word,"is not a palindrome")

#3.12a
word = input()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in alphabet:
    count=0
    for a in range(len(word)):
        if i==word[a]:
            count+=1
    print(i+":",count)

#3.12b
word1 = input()
word2 = input()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in alphabet:
    count1=0
    count2=0
    for a in range(len(word1)):
        if i==word1[a]:
            count1+=1
    for b in range(len(word2)):
        if i==word2[a]:
            count2+=1



#3.13
number = int(input())
count = 0
for i in range(len(str(number))):
    a = number%10
    if a%2==0:
        count+=1
    number = number//10
print(count)

#3.15
day1 = int(input())
month1 = int(input())
year1 = int(input())
day2 = int(input())
month2 = int(input())
year2 = int(input())
if month1<month2:
    age = year2-year1
elif month1>month2:
    age = (year2 - year1) -1
elif month1==month2 and (day1<day2):
    age = (year2 - year1) - 1
elif month1==month2 and (day1>day2):
    age = (year2 - year1)
elif month1==month2 and (day1==day2):
    age = (year2 - year1)
print(age)
