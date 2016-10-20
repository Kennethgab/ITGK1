# oppgave a



def isSixAtEdge(list):
    if list[-1] == 6 or list[0] == 6:
        print('There is a 6 at the start or end of the list')
        return True
    else:
        print('There is not a 6 at the start or end of the list')
        return False

six_end_list = [1,2,6]
six_first_list = [6, 1, 2]
no_six_list = [2,3,4]

isSixAtEdge(six_end_list)
isSixAtEdge(six_first_list)
isSixAtEdge(no_six_list)


def Average(list):
    return  sum(list)/len(list)

print(Average(six_end_list))

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0