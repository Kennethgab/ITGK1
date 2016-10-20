# bubblesort

def bubble_sort(list):
    for num in range(len(list)-1,0,-1):
            for i in range(num):
                 if list[i] > list[i+1]:
                    list[i],list[i+1] = list[i+1],list[i]
    return list

a = [0,3,1,2,3,4,6,3,1,3,5,3,1,3,5,7,6,3,2,3,4,5,6,7,4,2,1]

print(bubble_sort(a))

def selection_sort(list):
    for slot in range(len(list)-1,0,-1):
        maxPos = 0
        for position in range(1,slot+1):
            if list[position]>list[maxPos]:
                maxPos = position

        list[slot],list[maxPos] = list[maxPos],list[slot]
    return list

liste = [ 23, 26, 60, 76, 182, 1223, 23, 42, 12]

print(selection_sort(liste))
