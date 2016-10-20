# oppgave a

import random

def randList(size, lower_bound, upper_bound):
    list = []
    for i in range(0,size):
       number =   random.randint(lower_bound,upper_bound)
       list.append(number)
    return list

#oppgave b

a = [1,2,3]
b = [4,3,1]

def compareLists(list1,list2):
    comparisonlist = []
    if len(list1) > len(list2):
        biggest_list = len(list1)
        list = list1
        small_list = list2
    elif len(list2) > len(list1):
        biggest_list = len(list2)
        list = list2
        small_list = list1
    elif len(list2) == len(list1):
        biggest_list=len(list1)
        list = list1
        small_list = list2

    for i in range(0,biggest_list):
        if list[i]  in small_list and list[i] not in  comparisonlist:
            comparisonlist.append(list[i])
    return comparisonlist

print(compareLists(a,b))



def multiCompLists(lists):  # ikke ferdig
    comparisonlist = []


