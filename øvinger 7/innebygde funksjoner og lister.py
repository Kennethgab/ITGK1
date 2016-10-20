import random

# oppgave a

random_numbers = []

for i in range(0,100):

    number = random.randint(0,9)
    random_numbers.append(number)

print(random_numbers.count(2))

print(sum(random_numbers))

print(random_numbers)
sorted_random_numbers = sorted(random_numbers)
print(sorted_random_numbers)


def typetall(liste):
 temp_max = 0
 for tall in range(0,10):
     count = random_numbers.count(tall)
     if count > temp_max:
         temp_max = count
         temp_tall = tall
 return temp_tall,temp_max

typetallet,mengde = typetall(random_numbers)

print("Typetallet er {}, og mengden av den er {}" . format(typetallet,mengde))

reversed_sorted_random_numbers = sorted_random_numbers[:: -1] # [start: stop:step ]
# alternativt list(reversed(sorted_random_numbers))

print(reversed_sorted_random_numbers)


