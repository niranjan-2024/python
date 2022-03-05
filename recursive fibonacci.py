def recursive_fibonacci(n):
   if n<=1:
      return 1 
   else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
      
terms = 10

if terms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(terms):
       print(recursive_fibonacci(i))
