def Tower_of_hanoi(n,source,destination,auxillary):
   if n==1:
      print("Move disk 1 form source",source,"to destination",destination)
      return
   Tower_of_hanoi(n-1,source,auxillary,destination)
   print("Move disk",n,"from source",source,"to destination",destination)
   Tower_of_hanoi(n-1,auxillary,destination,source)
   
n=4
Tower_of_hanoi(n,'A','B','C')
