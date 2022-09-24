a = 0
b = 1
n = int(input("Enter the no of elements: "))
print("Fibonacci series: ")
print(a, end = " ")
print(b, end = " ")
for i in range(0,n-2):
    fibs = a + b
    print(fibs, end = " ")
    a = b
    b = fibs