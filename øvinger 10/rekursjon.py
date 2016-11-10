def recursive_sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)


numberlist = [ 32, 57 , 69 , 31 , 4 , 122 , 156 , 322]

def find_smallest_element(numbers, min=None):
    if not numbers:
        return min
    tall = numbers.pop()
    if min == None or tall<min:
        return find_smallest_element(numbers,tall)
    return find_smallest_element(numbers,min)


print(find_smallest_element(numberlist))

liste = [2,4,6,8,10,12,14,16]


def binary_search(numbers, element, offset=0):
    if not numbers:
        return (-float('inf'))  # element ikke i listen
    elif numbers[len(numbers)//2] == element:
        return offset + len(numbers)//2
    elif numbers[len(numbers)//2] > element:
        return binary_search(numbers[:len(numbers)//2], element, offset)
    else:
        return binary_search(numbers[(len(numbers)//2)+1:], element, offset+(len(numbers)//2)+1)


print(binary_search(liste, 16))



