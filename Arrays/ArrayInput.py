from array import *

arr = array('i', [])

n = int(input("Enter a Number: "))
for i in range(0, n):
    arr.append(int(input("Enter Next input: ")))

for x in arr:
    print(x, end=' ')