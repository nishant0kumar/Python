list =[2,7,11,15]
target = 9
for i in range(len(list)):
    x = list[i]
    for j in range(len(list)):
        y = list[-j]
        k = x+y
        if k==target:
            break
        else:
            print("nothing happened")
print(x,",",y)
        
