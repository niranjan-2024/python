list1 = ["niranjan",1,2,3,4,[7,8,["nonu",9,0]]]
print(list1[1],list1[0],list1[5][2][2],list1[-1])

list2 = [1,2,3,4,5,6,7,8,9]
print(list2[2:6])
print(list2[:6])
print(list2[2:])
print(list2[:])

odd = [2, 4, 6, 8]
odd[0] = 1            
print(odd)
odd[1:4] = [3, 5, 7]  
print(odd) 
odd.append(9)
print(odd)
odd.extend([10, 11, 13])
print(odd)

odd1 = [1, 3, 5]
print(odd1 + [9, 7, 5])
print(["re"] * 3)

odd2 = [1, 9]
odd2.insert(1,3)
print(odd2)
odd2[2:2] = [5, 7,8]
print(odd2)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
del my_list[2]
print(my_list)
del my_list[1:5]
print(my_list)
#del my_list
print(my_list)

my_list2 = ['p','r','o','b','l','e','m']
my_list2.remove('p')
print(my_list2.pop(1))
print(my_list2)
print(my_list2.pop())
print(my_list2)
my_list2.clear()
print(my_list2)

# Example on Python list methods

my_list3 = [3, 8, 1, 6, 8, 8, 4]
my_list3.append('a')
print(my_list3)
print(my_list3.index(8))   
print(my_list3.count(8)) 

pow2 = [2 ** x for x in range(20)]
print(pow2)

pow23 = []
for x in range(10):
   pow23.append(3 ** x)
print(pow23)

my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
print('p' in my_list)
print('a' in my_list)
print('c' not in my_list)

for fruit in ['apple','banana','mango']:
    print("I like",fruit)
    
h_letters = []
for letter in 'human':
    h_letters.append(letter)
print(h_letters)

i_letters = [ letter for letter in 'human' ]
print( i_letters)

letters = list(map(lambda x: x, 'human'))
print(letters)

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

