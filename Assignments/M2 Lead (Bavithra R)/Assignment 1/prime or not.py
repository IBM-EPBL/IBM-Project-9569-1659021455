import math
a = int(input("Enter the num: "))
flag = 1
if a > 2:
    for i in range(2, math.ceil(math.sqrt(a))+1):
        if (a % i) == 0:
            print(a, " is not a prime number")
            flag = 0
            break
    if flag == 1:
        print(a, " is a prime number")
elif a > 1:
    print(a, " is a prime number")
else:
    print(a, " is neither prime nor composite")
