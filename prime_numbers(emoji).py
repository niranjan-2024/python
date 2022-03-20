j=5
while j>0:
   num = int(input("Enter a number: "))
   flag = False
   if num > 1:
       for i in range(2, num):
          if (num % i) == 0:
             flag = True
             break
   if flag:
       print(b' \xF0\x9F\x91\x8E'.decode("utf-8"))
   else:
       print(b' \xf0\x9f\x91\x8d'.decode("utf-8"))
   j -= 1
