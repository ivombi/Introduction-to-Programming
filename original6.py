def monamix(input_list):
    if len(input_list) > 1:
        inhabitant, identifier = split_inhabitant(input_list)
        min_list = local_min(identifier, inhabitant)
        print(min_list)

        while len(min_list) > 1:
            inhabitant, identifier = split_inhabitant(min_list)
            max_list = local_max(identifier, inhabitant)
            print(max_list)
            if len(max_list) > 0:
                inhabitant, identifier = split_inhabitant(max_list)
                min_list = local_min(identifier, inhabitant)
                print(min_list)

    else:  # code to end
        return input_list


def split_inhabitant(input_list):
    identifier = []  # list to hold unique identifier
    inhabitant = []  # List to hold name of inhabitant

    for elem in input_list:
        slice_pos = 0
        num_colon = 0  # Determine the number of colons in each list element
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


list = ["A:1", "B:6", "C:5", "D:4", "E:7", "F:3", "G:10", "H:2", "I:9", "J:8", "K:11"]
monamix(list)