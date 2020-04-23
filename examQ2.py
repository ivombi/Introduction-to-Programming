#Done By: Kubam Ivo
#Date: 5/16/2019

import sys

A = [[6, 7, 3, 5], [9, 2, 1, 2], [3, 5, 4, 3], [2, 3, 7, 4]]
matrix = sys.argv[1:]
d = int(sys.argv[2])
result = []
elem = ""


def horizontal_min(x, y, d, matrix):
    """Function to check if a cell variable is
    is less than values to its left or right"""
    x = int(x)
    y = int(y)

    if y - d >= 0 and y + d < len(matrix[x]): # Testing for matrix elements that neither first or last in a row
        a = matrix[x][y]
        b = matrix[x][y - d]
        c = matrix[x][y + d]
        if a < b and a < c:
            return True
        else:
            return False
    elif y == 0: # Testing for first elements in a row
        a = matrix[x][y]
        c = matrix[x][y + d]
        if a < c:
            return True
        else:
            return False
    elif y == len(matrix[x]) - 1: # Testing for last elements in a row
        a = matrix[x][y]
        b = matrix[x][y - d]
        if a < b:
            return True
        else:
            return False


def vertical_min(x, y, d, matrix): #Testing if matrix element is less than elements immediately above or below
    """This function test if a particular matrix element is less than values directly above or below its position"""
    x = int(x)
    y = int(y)
    if (x - d) >= 0 and (x + d) < len(matrix): #Testing for elements not in the first row or last row
        a = matrix[x][y]
        b = matrix[x - d][y]
        c = matrix[x + d][y]
        if a < b and a < c:
            return True
        else:
            return False
    elif x == 0 and len(matrix) > 1:  # Testing for elements in the first row
        a = matrix[x][y]
        c = matrix[x + d][y]
        if a < c:
            return True
        else:
            return False

    elif x == len(matrix) - 1 and len(matrix) > 1: #Testing elements in the last row
        a = matrix[x][y]
        b = matrix[x - d][y]
        if a < b:
            return True
        else:
            return False


def diagonal_min(x, y, d, matrix):
    """Function test of diagonal criteria.If an element is less than values in its diagonal. both leading and lagging diagonal"""
    x = int(x)
    y = int(y)
    if len(matrix)>1: #Making sure matrix has atleast two elements
        if (x - d) >=0 and (x + d) < len(matrix) and y-d>=0 and y+d<len(matrix[x]): #Testing for elements not in first or last row and not the first element
            a = matrix[x][y]
            b = matrix[x - d][y - d] # leading diagonal
            c = matrix[x + d][y + d] # leading diagonal
            d = matrix[x - d][y + d] # lagging diagonal
            e = matrix[x + d][y - d] # lagging diagonal
            if a < b and a < c and a < d and a < e:
                return True
            else:
                return False
        elif x == len(matrix) - 1 and len(matrix)>1 and : #Testing elements in the last row
            a = matrix[x][y]
            b = matrix[x - d][y - d]  # leading diagonal
            d = matrix[x - d][y + d]  # lagging diagonal

            if a < d and a<b:
                return True
            else:
                return False
        elif x == 0 and y +d < len(matrix[x]) and y-d>=0 and len(matrix)>1: # Testing elements in the first row
            a = matrix[x][y]
            e = matrix[x + d][y - d] # lagging diagonal
            c = matrix[x + d][y + d]  # leading diagonal
            if a < e and a<e:
                return True
            else:
                return False
        elif x == 0 and y == 0:
            a = matrix[x][y]
            c = matrix[x + d][y + d]
            if a < c:
                return True
            else:
                return False


def local_mins(matrix, d):
    for x in range(len(matrix)):
        for y in range(len(matrix[int(x)])):
            if horizontal_min(x, y, d, matrix) == True:
                if vertical_min(x, y, d, matrix) == True:
                    if diagonal_min(x, y,d,matrix) == True:
                        elem = "(" + str(x) + "," + str(y) + ")"
                        result.append(elem)
                        elem = ""

local_mins(A, 2)









