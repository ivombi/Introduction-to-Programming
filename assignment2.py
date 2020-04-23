import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
for i in range(a,b+1):
    x = 0
    sum = 0
    y = 0
    while x<=c:
        y = i **x
        x += 1
        sum = sum + y
        print(y,end=" ")
    print("sum",sum)


