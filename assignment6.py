#Author:Kubam Ivo
#Course: Introduction to Algorithm and Programming
#Assignment Six
#Date:4/22/2019

import sys

input_list=sys.argv[1:]

def monamix(input_list):
    if len(input_list) > 1:
        inhabitant, identifier = split_inhabitant(input_list)
        min_list = local_min(identifier, inhabitant)
        print("min", end=" ")
        for elem in min_list:
            print(elem, end=" ")
        print()

        while len(min_list) > 1:
            inhabitant, identifier = split_inhabitant(min_list)
            max_list = local_max(identifier, inhabitant)
            print("max", end=" ")
            for elem in max_list:
                print(elem, end=" ")
            print()
            if len(max_list) > 1:
                inhabitant, identifier = split_inhabitant(max_list)
                min_list = local_min(identifier, inhabitant)

            else:
                min_list = max_list[:]
        inhabitant, identifier = split_inhabitant(min_list)
        print("Inhabitant", inhabitant[0], "(id:", str(identifier[0]) + ")", "is the new Monarch")

    else:  # code to end
        inhabitant, identifier = split_inhabitant(input_list)
        print("Inhabitant", inhabitant[0], "(id:", str(identifier[0]) + ")", "is the new Monarch")


def split_inhabitant(input_list):
    identifier = []  # list to hold unique identifier
    inhabitant = []  # List to hold name of inhabitant

    for elem in input_list:
        slice_pos = 0

        for i in range(len(elem)):
            if elem[i] == ":":
                slice_pos = int(i)
        inhabitant.append(elem[0:slice_pos])
        identifier.append(int(elem[slice_pos + 1:]))
    return inhabitant, identifier


def local_min(identifier, inhabitant):
    min = []  # list to hold local minimum values
    for i in range(len(identifier)):
        if int(i) == 0:
            if identifier[i] < identifier[int(i) + 1]:
                min.append(inhabitant[i] + ":" + str(identifier[i]))
        elif int(i) == len(identifier) - 1:
            if identifier[i] < identifier[int(i) - 1]:
                min.append(inhabitant[i] + ":" + str(identifier[i]))

        elif identifier[i] < identifier[int(i) - 1] and identifier[i] < identifier[int(i) + 1]:
            min.append(inhabitant[i] + ":" + str(identifier[i]))
    return min


def local_max(identifier, inhabitant):
    max = []  # list to hold local minimum values
    for i in range(len(identifier)):
        if int(i) == 0:
            if identifier[i] > identifier[int(i) + 1]:
                max.append(inhabitant[i] + ":" + str(identifier[i]))
        elif int(i) == len(identifier) - 1:
            if identifier[i] > identifier[int(i) - 1]:
                max.append(inhabitant[i] + ":" + str(identifier[i]))

        elif identifier[i] > identifier[int(i) - 1] and identifier[i] > identifier[int(i) + 1]:
            max.append(inhabitant[i] + ":" + str(identifier[i]))
    return max

monamix(input_list)