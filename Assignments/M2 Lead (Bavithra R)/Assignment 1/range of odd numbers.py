m = int(input("lower limit : "))
n = int(input("upper limit : "))
if((m==n and m%2==0) or m>n):
    print("No odd numbers found")
else:
    print("odd numbers are: ")
    while m < n+1:
        if(m%2)!=0:
            print(m, end=" ")
        m = m + 1