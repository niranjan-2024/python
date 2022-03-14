row = int(input("Enter no. of rows:"))

for i in range(row):
   for j in range(i+1):
      print("*",end ="")
   print()
print()

for i in range(row):
   for j in range(i+1):
      print(j+1,end="")
   print()
print()

assci_val = 65
for i in range(row):
   for j in range(i+1):
      alphabet = chr(assci_val)
      print(alphabet, end="")
   assci_val+=1
   print()
print()

for i in range(row,0,-1):
   for j in range(0,i):
      print("*",end="")
   print()
print()

for i in range(row,0,-1):
   for j in range(1,i+1):
      print(j,end="")
   print()
print()

k = 0
for i in range(1, row+1):
    for space in range(1, (row-i)+1):
        print(end=" ")
    while k!=(2*i-1):
        print("*", end="")
        k += 1
    k = 0
    print()
print()  

k = 0
count=0
count1=0
for i in range(1, row+1):
    for space in range(1, (row-i)+1):
        print(" ", end="")
        count+=1
    while k!=((2*i)-1):
        if count<=row-1:
            print(i+k, end="")
            count+=1
        else:
            count1+=1
            print(i+k-(2*count1), end="")
        k += 1
    count1 = count = k = 0
    print()
print()

for i in range(row, 1, -1):
    for space in range(0, row-i):
        print(" ", end="")
    for j in range(i, 2*i-1):
        print("*", end="")
    for j in range(1, i-1):
        print("*", end="")
    print()
print()

#pascal triangle
coef = 1
for i in range(1, row+1):
    for space in range(1, row-i+1):
        print(" ",end="")
    for j in range(0, i):
        if j==0 or i==0:
            coef = 1
        else:
            coef = coef * (i - j)//j
        print(coef, end = " ")
    print()
print()

#floyds triangle
number = 1
for i in range(1, row):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()
