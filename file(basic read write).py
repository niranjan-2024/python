with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
f = open("test.txt",'r',encoding = 'utf-8')
print(f.read())
f.close
