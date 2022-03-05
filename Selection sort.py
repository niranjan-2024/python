def selection_sort(array, size):
   for step in range(size):
      min_idx = step
      for i in range(step+1,size):
         if array[i]<array[min_idx]:
            min_idx = i 
      (array[min_idx],array[step]) = (array[step],array[min_idx])
      
array = [9,8,7,6,5,4,3,2,1,-5]
size = len(array)
selection_sort(array, size)
print(array)
