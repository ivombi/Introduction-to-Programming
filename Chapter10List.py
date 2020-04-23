#List method
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
mylist

mylist.insert(1,12)
mylist.count(12)
mylist.extend([5,9,5,11])
mylist.index(9)

mylist.reverse()
mylist.sort()
mylist.remove(12)
mylist

def append_to_(element,to=[]):
    to.append(element)
    return to
my_list = append_to_(12)
print(my_list)

my_other_list = append_to_(42)
print(my_other_list)

#Pure functions
def double_stuff(a_list):
    """Return a new list which contains
    doubles of the elements in a_list:
    """
    new_list = []
    for value in a_list:
        new_elem = 2 * value
        new_list.append(new_elem)
    return new_list

things = [2,5,6]
xs = double_stuff(things)
things
xs

#Dodona Exercises
#7.1
def is_ordered(my_list):
    pre_elem = ""
    for i in my_list:
        if my_list[0]==i:
            pre_elem=i
        elif i >=pre_elem:
            pre_elem = i
        else:
            return False
    return True

#7.2


#7.3
def is_unique(my_list):
    start = 1
    for i in my_list:
        my_new_list = my_list[start:]
        for x in my_new_list:
            if x == i:
                return False
        start+=1
    return True


def shift_pos(l, n):
    list_len = len(l)
    n = n % (list_len - 1)
    new_list = []
    for elem in l:
        elem_pos = l.index(elem)
        new_pos = elem_pos + n + 1
        if new_pos > list_len - 1:
            new_pos -= list_len
            new_list.append(l[new_pos])
        else:
            new_list.append(l[new_pos])
    return new_list


def shift_neg(l, n):
    list_len = len(l)
    n = -(n % (list_len - 1))
    new_list = []
    for elem in l:
        elem_pos = l.index(elem)
        new_pos = elem_pos - (-n + 1)
        if new_pos < 0:
            new_pos = list_len + new_pos
            new_list.append(l[new_pos])
        else:
            new_list.append(l[new_pos])
    return new_list


def shift(l, n):
    if n > 0 and len(l) > 1:
        return shift_pos(l, n)
    elif n < 0 and len(l) > 1:
        return shift_neg(l, n)
    else:
        return l


#7.11
def is_magic_square(matrix):
    unique = is_unique(matrix)
    row_sum = matrix_row_sum(matrix)
    column_sum = matrix_col_sum(matrix)
    diagonal_sum = matrix_diag_sum(matrix)
    if unique == True and (row_sum == column_sum == diagonal_sum):
        return True
    else:
        return False


def matrix_row_sum(matrix):
    list_sum = []

    for list in matrix:
        row_sum = 0
        for elem in list:
            row_sum += int(elem)
        list_sum.append(row_sum)
    if list_sum.count(list_sum[0]) == len(list_sum):
        return list_sum[0]
    else:
        return False


def matrix_col_sum(matrix):
    list_sum = []
    list_len = len(matrix[0])
    for i in range(list_len):
        col_sum = 0
        for list in matrix:
            col_sum += int(list[i])
        list_sum.append(col_sum)
    if list_sum.count(list_sum[0]) == len(list_sum):
        return list_sum[0]
    else:
        return False


def is_unique(matrix):
    for list in matrix:
        for elem in list:
            count = 0
            for list in matrix:
                count += list.count(elem)
                if count > 1:
                    return False
    return True


def matrix_diag_sum(matrix):
    diag_sum = 0
    list_len = len(matrix[0])
    for i in range(list_len):
        if len(matrix) > 1:
            diag_sum += matrix[i][i]
        else:
            diag_sum += matrix[0][0]
    return diag_sum

#7.2
def fibonacci_values(i):
    fib_list = []
    x = 0
    while len(fib_list) < i and len(fib_list) < 2:
        fib_list.append(x)
        x += 1

    while len(fib_list) < i:
        len_fib = len(fib_list)
        x = 0
        x = fib_list[len_fib - 2] + fib_list[len_fib - 1]
        fib_list.append(x)
    return fib_list




