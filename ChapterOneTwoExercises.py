total_secs = int(input("How many seconds, in total?"))
hours = total_secs//3600
sec_still_remaining = total_secs % 3600
minutes = sec_still_remaining // 60
sec_finally_remaining = sec_still_remaining % 60
print("Hrs=", hours, " mins=", minutes, "secs=", sec_still_remaining)

#Exercise 1.10

i = 4
j= 5
product = i * j
som = i + j
print("prodcut =",product)
print("som =",som)

i = 4
j= 5
print("prodcut =",i*j)
print("som =",i+j)

51%24

print("This sentence is extremely long, for", sep="\n")
print("readability I wrappted in to two lines :")

response_name = input("What's your name")
print("Your name is ",response_name)
print("The first letter of your name is ",response_name[0])
print("The last letter of your name is ",
      response_name[len(response_name)-1])
#1.15
value = int(input("Give a number:"))
twice = 2 * value
print("Twice your number is " , twice)

#1.16
a = int(input("Give first number: "))
b = int(input("Give second number: "))
c = int(input("Give third number: "))
d = int(input("Give fourth number: "))
e = int(input("Give firth number: "))
print("The sum of your numbers is ",a+b+c+d+e)

#Using one variable
a = int(input("Give first number: "))
a = a+ int(input("Give second number: "))
a = a + int(input("Give third number: "))
a = a + int(input("Give fourth number: "))
a = a + int(input("Give firth number: "))
print("The sum of your numbers is ",a)

#Using no variable
print("The sum of your numbers is ",int(input("Give first number: "))
      +int(input("Give second number: "))
      + int(input("Give third number: "))
      + int(input("Give fourth number: "))
      + int(input("Give firth number: ")))

#Exercise 1.17
team_size = int(input("What is the size of each team? "))
participant = int(input("How many participants do you we have ?"))
number_team = participant//team_size
participant_left = participant%team_size
print("From the information, we can have ",number_team," team(s)",sep="",end="")
print(" and ",participant_left, "participants left with no team")

#Exercises on Dodona
a= 1*int(input())
b =2* int(input())
c = 5* int(input())
d = 10*int(input())
e = 20*int(input())
total = a+b+c+d+e
euro = total//100
cent = float(total%100)
if total==0: cent="00"
print("You have ", euro, ".", cent, " euro!", sep="")

#1.2
title = input()
len_title = len(title)
print(title)
print("x" * len_title)

#1.3
days = int(input())
hours = int(input())
min = (days*24*60) + hours*60
print(min)

print "\033[4mhello\033[0m"

#1.4
a = int(input())
a_twoeuro = a//200
a_twoeuro_left = a%200
a_1euro =a_twoeuro_left//100
a_1euro_left = a_twoeuro_left%100
a_50cent = a_1euro_left//50
a_50cent_left = a_1euro_left%50
a_20cent = a_50cent_left//20
a_20cent_left = a_50cent_left%20
a_10cent = a_20cent_left//10
a_10cent_left = a_20cent_left%10
a_5cent = a_10cent_left//5
a_5cent_left = a_10cent_left%5
a_2cent = a_5cent_left//2
a_2cent_left = a_5cent_left%2
a_1cent = a_2cent_left
print("2-euros:",a_twoeuro)
print("1-euros:",a_1euro)
print("50c-euros:",a_50cent)
print("20c-euros:",a_20cent)
print("10c-euros:",a_10cent)
print("5c-euros",a_5cent)
print("2c-euros:",a_2cent)
print("1c-euros:",a_1cent)
