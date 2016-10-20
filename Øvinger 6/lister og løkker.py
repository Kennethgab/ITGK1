# oppgave a

number_list = list(range(0,100))
sum = 0

for i in number_list:
    if i % 3 == 0 or i % 10 == 0:
        sum+=i



print(sum)
a=-2
for n in range(0,50):
 a+= 2
 number_list[a],number_list[a+1] = number_list[a+1],number_list[a]
print(number_list)

a=-1
number_list_backwards = []
for i in range(0,100):
    number_list_backwards.append(number_list[a])
    a-=1

print(number_list_backwards)




