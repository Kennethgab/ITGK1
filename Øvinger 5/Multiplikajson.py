def multiply(tol):
    a=1
    s=1
    while True:
        if abs(s-s*(1+1/a**2))<tol: break
        s*=(1+1/a**2)
        a+=1
    return s,a

print(multiply(0.01))


