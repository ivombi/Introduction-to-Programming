# Author: Kubam Ivo Mbi
# Student number: 1850637
# I have done task 1,2,3 and 4

import sys
dataset= sys.argv[1]
airport = sys.argv[2]
tfield = sys.argv[3]
dfield = sys.argv[4]
if len(sys.argv)>5:
    filter=sys.argv[5]
else:
    filter=None

#This program assumes that the 2017_1.csv and L_AIRPORT.csv are both in same directory as the big_assignment python file

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

    #Creating a list to hold cities in united states
    cities_US=[]
    split_word=""
    for elem in airport_list_new:
       if len(elem)>2:
           split_word=elem[2].split(":")
       if split_word[0].isupper() and len(split_word[0])==3:
           if len(elem)>2:
               cities_US.append(elem)



    #creating list to hold time interals
    time_interval=["0:00-1:59:","2:00-3:59:","4:00-5:59:","6:00-7:59:","8:00-9:59:","10:00-11:59:","12:00-13:59:","14:00-15:59:","16:00-17:59:","18:00-19:59:","20:00-21:59:","22:00-23:59:"]
    dataset_list_new2=[]

    #dataset to hold filtered records
    if filter==None:
        dataset_list_new2 = dataset_filtering(dataset_list_new,filter) #Calling the filtereing function
    else:
        if len(filter)>1:
            if ";" in filter:
                filter = filter.split(";")  #splitting filter argument into sub filters
                for i in range(len(filter)): #Iteralting the filters to filter the dataset
                    dataset_list_new2=dataset_filtering(dataset_list_new,filter[i],cities_US)
                    dataset_list_new=dataset_list_new2[:]

            else:
                dataset_list_new2=dataset_filtering(dataset_list_new,filter,cities_US)


    interval_stats=[] #variable to hold interval statistics
    bar_length=[]
    interval_stats=statistics(dataset_list_new2,dfield,tfield) #Calling the statistics function
    if max(interval_stats)>1:
        bar_value =max(interval_stats)/20
        for elem in interval_stats:
            bar_length.append(int(int(elem)/bar_value))

        for i in range(12): #Printing Out the results
            print(" " * (12 - len(time_interval[i])), time_interval[i],"|" + "*" * bar_length[i] + " " * (20 - bar_length[i]) + "|"," " * (len(str(sum(interval_stats))) -(2+len(str(int((interval_stats[i]))))))+str(int(interval_stats[i])))
        print(" " + "-" *(35+len(str(max(interval_stats)))))
        print(" " * 36, int(sum(interval_stats)))
    else:
        print("No data collected.")

def dataset_filtering(dataset,filter,cities_US=None): #function to hold filtered records

    dataset_list_new2 = []  # empty list to hold all filtered dataset

    if filter==None:
        for elem in dataset:
            if (elem[9]=="0.00" and elem[10]=="0.00"):  # Filtering records to remove cancelled and deviated flights)
                dataset_list_new2.append(elem)
            else:
                 continue
    else:

        filter_value=filter.split("=")
        filter_value=filter_value[1]

        if "airline" in filter:
            for elem in dataset:
                if filter_value in elem[1]:
                    dataset_list_new2.append(elem)

        elif "plane" in filter:
            for elem in dataset:
                if filter_value in elem[2]:
                    dataset_list_new2.append(elem)

        elif "d_city" in filter:

            city_code=[]
            for elem in cities_US:
                if filter_value in elem[1]:
                    city_code.append(elem[0])
            for elem in city_code:
                for x in dataset:
                    if elem in x[3]:
                        dataset_list_new2.append(x)

        elif "a_city" in filter:

            city_code=[]
            for elem in cities_US:
                if filter_value in elem[1]:
                    city_code.append(elem[0])
            for elem in city_code:
                for x in dataset:
                    if elem in x[4]:
                        dataset_list_new2.append(x)

    return dataset_list_new2

def statistics(dataset,dfield,tfield):

    time_column=0;cal_column=0
    interval_stats=[]
    if dfield=="flights":
        if tfield=="departure":
            cal_column=5; time_column=5
        elif tfield=="arrival":
            cal_column = 7; time_column = 7
        interval_stats = interval_stats_sub(dataset, time_column, cal_column,dfield)

    elif dfield=="departure_delays" or dfield=="arrival_delays":
        if dfield=="departure_delays" and tfield=="departure":
            cal_column=6; time_column=5
        elif dfield=="arrival_delays" and tfield=="arrival":
            cal_column = 8; time_column = 7
        elif dfield=="departure_delays" and tfield=="arrival":
            cal_column=6; time_column=7
        elif dfield=="arrival_delays" and tfield=="departure":
            cal_column = 8; time_column = 5
        interval_stats=interval_stats_sub(dataset,time_column,cal_column,dfield)

    elif ("carrier" in dfield) or ("weather" in dfield) or ("nas" in dfield) or ("security" in dfield) or ("late_aircraft" in dfield):

        dfield=dfield[3:]

        if dfield=="carrier" and tfield=="arrival":
            cal_column=11; time_column=7
        elif dfield=="carrier" and tfield=="departure":
            cal_column = 11; time_column = 5
        elif dfield=="weather" and tfield=="arrival":
            cal_column=12; time_column=7
        elif dfield=="weather" and tfield=="departure":
            cal_column = 12; time_column = 5
        elif dfield=="nas" and tfield=="arrival":
            cal_column=13; time_column=7
        elif dfield=="nas" and tfield=="departure":
            cal_column = 13; time_column = 5
        elif dfield=="security" and tfield=="arrival":
            cal_column=14; time_column=7
        elif dfield=="security" and tfield=="departure":
            cal_column = 14; time_column = 5
        elif dfield=="late aircraft" and tfield=="arrival":
            cal_column=15; time_column=7
        elif dfield=="late aircraft" and tfield=="departure":
            cal_column = 14; time_column = 5

        interval_stats = interval_stats_sub(dataset, time_column, cal_column,dfield)

    return interval_stats

def interval_stats_sub(dataset,time_column,cal_column,dfield):

    interval_stats = []
    if dfield=="flights":
        count = 0
        for elem in dataset:
            if elem[time_column] < '"0200"':
                count += 1
            if elem[time_column] == '"2400"':
                count += 1
        interval_stats.append(count)

        count = 0
        for elem in dataset:
            if elem[time_column] >= '"0200"' and elem[time_column] < '"0400"':
                count += 1
        interval_stats.append(count)

        count = 0
        for elem in dataset:
            if elem[time_column] >= '"0400"' and elem[time_column] < '"0600"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"0600"' and elem[time_column] < '"0800"':
                count += 1
        interval_stats.append(count)

        count = 0
        for elem in dataset:
            if elem[time_column] >= '"0800"' and elem[time_column] < '"1000"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"1000"' and elem[time_column] < '"1200"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"1200"' and elem[time_column] < '"1400"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"1400"' and elem[time_column] < '"1600"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"1600"' and elem[time_column] < '"1800"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"1800"' and elem[time_column] < '"2000"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"2000"' and elem[time_column] < '"2200"':
                count += 1
        interval_stats.append(count)
        count = 0
        for elem in dataset:
            if elem[time_column] >= '"2200"' and elem[time_column] < '"2400"':
                count += 1
        interval_stats.append(count)

    else:
        sum = 0
        for elem in dataset:
            if elem[time_column] < '"0200"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
            if elem[time_column] == '"2400"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"0200"' and elem[time_column] < '"0400"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"0400"' and elem[time_column] < '"0600"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"0600"' and elem[time_column] < '"0800"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"0800"' and elem[time_column] < '"1000"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"1000"' and elem[time_column] < '"1200"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"1200"' and elem[time_column] < '"1400"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"1400"' and elem[time_column] < '"1600"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"1600"' and elem[time_column] < '"1800"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"1800"' and elem[time_column] < '"2000"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"2000"' and elem[time_column] < '"2200"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

        sum = 0
        for elem in dataset:
            if elem[time_column] >= '"2200"' and elem[time_column] < '"2400"' and elem[cal_column] > "0":
                sum += float(elem[cal_column])
        interval_stats.append(sum)

    return interval_stats


graph_flight(dataset,airport,tfield,dfield,filter)






