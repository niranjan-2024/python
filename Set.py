#unordered,unique,immutable
my_set = {1, 2, 3}
print(my_set)
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)
my_set = {1, 2, 3, 4, 3, 2}
print(my_set)
my_set = set([1, 2, 3, 2])
print(my_set)
#cannot have mutable items
#no indexing
a = {}
print(type(a))
a = set()
print(type(a))

my_set = {1, 3}
print(my_set)
my_set.add(2)
print(my_set)
my_set.update([2, 3, 4])
print(my_set)
my_set.update([4, 5], {1, 6, 8})
print(my_set)

my_set = {1, 3, 4, 5, 6}
print(my_set)
my_set.discard(4)
print(my_set)
my_set.remove(6)
print(my_set)
my_set.discard(2)
print(my_set)
#my_set.remove(2) error

my_set = set("HelloWorld")
print(my_set)
print(my_set.pop())
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

#union
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A | B)

# use union function   in shell python
#>>> A.union(B)
#{1, 2, 3, 4, 5, 6, 7, 8}

#intersection
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A & B)

#difference
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A - B)

#symeetric difference ony in A or B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print(A ^ B)

#>>> A.symmetric_difference(B) in shell

my_set = set("apple")
print('a' in my_set)
print('p' not in my_set)

for letter in set("apple"):
  print(letter)
  
#frozen sets are immutable sets




