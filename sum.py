Lst = [1,2,3,4,5,7,6,8,9]
sum = 0
for x in Lst:
    if x%2!=0:
        sum += x
    else:
        continue
print(sum)