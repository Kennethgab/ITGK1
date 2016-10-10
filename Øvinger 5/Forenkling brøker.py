def gcd(a,b):
    k=a
    m=b
    c=0
    while m!=0:
        c=m
        m=k%m
        k=c
    return k



def reduce_fraction(teller,nevner):
    d=gcd(teller,nevner)
    r,t=teller/d,nevner/d
    return str(int(r))+"/"+str(int(t))


print(reduce_fraction(5,10))
print(reduce_fraction(4,2))