def seperate(numbers, threshold):
    thresholdAndOver = []
    thresholdUnder = []
    for i in range(len(numbers)):
        if numbers[i] >= threshold:  thresholdAndOver.append(numbers[i])
        else: thresholdUnder.append(numbers[i])
    return thresholdAndOver,thresholdUnder


a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

over,under = seperate(a,5)

print(over,under)


def multiplication_table(n):
    a=[]
    for i in range(1,n+1):
        for j in range(1,n+1):
            mul = i * j
            a.append(mul)
        print(a)
        for k in range(1,n+1):
            a.pop()
    return a

print(multiplication_table(4))