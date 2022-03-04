def linearsearch(array, n, x):
   for i in range(0,n):
      if array[i] == x:
         return i
   return -1
   
array = [1,2,3,4,5]
x = 5
n = len(array)
result = linearsearch(array, n, x)
if(result == -1):
   print("element not found")
else:
   print("element found at index :",result)
