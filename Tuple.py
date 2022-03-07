my_tuple = ()#immutable
print(my_tuple)
my_tuple = (1, 2, 3)
print(my_tuple)
my_tuple = (1, "Hello", 3.4)
print(my_tuple)
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)
my_tuple = 3, 4.6, "dog"
print(my_tuple)
a, b, c = my_tuple#tuple unpacking
print(a)      
print(b)      
print(c)  

my_tuple = ("hello")
print(type(my_tuple))  
my_tuple = ("hello",)
print(type(my_tuple))  
my_tuple = "hello",
print(type(my_tuple))  

my_tuple = ('p','e','r','m','i','t')
print(my_tuple[0])   
print(my_tuple[5])
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])       
print(n_tuple[1][1]) 

my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[-1])
print(my_tuple[-6])

my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[1:4])
print(my_tuple[:-7])
print(my_tuple[7:])
print(my_tuple[:])

my_tuple = (4, 2, 3, [6, 5])
my_tuple[3][0] = 9    
print(my_tuple)
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print(my_tuple)


print((1, 2, 3) + (4, 5, 6))
print(("Repeat",) * 3)

#del my_tuple

my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  
print(my_tuple.index('l')) 


my_tuple = ('a', 'p', 'p', 'l', 'e',)
print('a' in my_tuple)
print('b' in my_tuple)
print('g' not in my_tuple)

for name in ('John', 'Kate'):
    print("Hello", name)

#tuple heterogenenous, list homo data types:
 
 

