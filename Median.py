Lst = [12,434,56,23,64,4]
Lst.sort()
n = len(Lst)
Median = 0
x=0
if n%2==0:
    x = n//2
    a = Lst[x-1]
    b = Lst[x]
    Median = (a+b)/2
    print(Median)
else:
    x = n//2
    print(Lst[x])