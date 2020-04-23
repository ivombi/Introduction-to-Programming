# Author: Kubam Ivo Mbi
# Student number: 1850637

import sys
dataset= sys.argv[1]
airport = sys.argv[2]
tfield = sys.argv[3]
filter=sys.argv[4]

#Task One
#Function assumes that the 2017_1.csv and L_AIRPORT.csv are both in same directory as the python file

def graph_flight(dataset, airport, tfield, dfield, filter=None):
    dataset = open(dataset,"r")
    airport = open(airport, "r")
    dataset_list = dataset.readlines() # elemeemts of the list are list of strings

    del dataset_list[0]  # deleting the first row which is a header

    #Creating a dataset where elements of the list are lists of lists
    dataset_list_new = []

    for i in range(len(dataset_list)):
        dataset_list_new.append(dataset_list[i].split(','))
    dataset.close()

    airport_list = airport.readlines()
    del airport_list[0]  # deleting the first row which is a header

    # Creating a dataset where elements of the list are lists of lists
    airport_list_new = []
    for i in range(len(airport_list)):
        airport_list_new.append(airport_list[i].split(','))
    airport.close()

    #creating list to hold time interals
    time_interval=["0:00-1:59:","2:00-3:59","4:00-5:59","6:00-7:59","8:00-9:59","10:00-11:59","12:00-13:59","14:00-15:59","16:00-17:59","18:00-19:59","20:00-21:59","22:00-23:59"]

    #dataset to hold filtered records
    dataset_list_new2 = dataset_filtering(dataset_list_new)

    #dataset to analyse with respect to departure or arrival time
    print(len(dataset_list_new2))


def dataset_filtering(dataset,filter=None): #function to hold filtered records

    dataset_list_new2 = []  # empty list to hold all flights except those cancelled or deviated

    for elem in dataset:
        if elem[5]!='""' or elem[7]!='""'  :  # Filtering records to remove cancelled and deviated flights)
            dataset_list_new2.append(elem)
        else:
             continue
    return dataset_list_new2



#graph_flight("2017_1.csv", "L_AIRPORT.csv-","a","flights")




