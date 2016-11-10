def write_to_file(data):
    f = open('my_file.txt','w')
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename,'r')
    innhold = f.read()
    print(innhold)



def number_of_lines(filename):
    num_lines = sum(1 for line in open(filename))
    return num_lines

print(number_of_lines('numbers.txt'))

def number_frequency(filename):

    number_list = []
    f = open(filename,'r')
    innhold = f.read()
    number_freq = {x:innhold.count(x) for x in innhold}
    number_freq.pop('\n',None)
    return number_freq

number_freq = number_frequency('numbers.txt')
print(number_frequency('numbers.txt'))


for i in number_freq:
    print(i,':',number_freq[i])





