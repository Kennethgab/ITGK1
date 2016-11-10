def write_to_file(data):
    f = open('my_file.txt','w')
    f.write(data)
    f.close()

def read_from_file(filename):
    f = open(filename,'r')
    innhold = f.read()
    print(innhold)


def main():
    while(spm != 'done'):
        spm = str(input('Do you want to read of write?'))
        if(spm == 'write'):
            spm = str(input("what do you want to write to the file?"))
            write_to_file(spm)
            print(spm," Has been written to file.")
        elif(spm == 'read'):
            read_from_file('my_file.txt')


    print("You are done")