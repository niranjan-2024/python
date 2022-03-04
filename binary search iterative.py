def binarsearch(array, n, low, high):
   while low<=high:
      mid = low + (high - low)//2
      if array[mid] == x:
         return mid
      elif array[mid]<x:
         low = mid + 1 
      else:
         high = mid - 1 
   return -1
array = [1,2,3,4,5,6,7,8,9,10]
x = 1
result = binarsearch(array, x, 0,len(array)-1)
if result != -1:
   print("element found at index :",result)
else:
   print("element not found")
