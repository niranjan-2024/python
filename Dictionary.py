#unordered key/value
#mutable
#only keys are immutable and unique
my_dict = {}
my_dict = {1: 'apple', 2: 'ball'}
my_dict = {'name': 'John', 1: [2, 4, 3]}
my_dict = dict({1:'apple', 2:'ball'})
my_dict = dict([(1,'apple'), (2,'ball')])

my_dict = {'name': 'Jack', 'age': 26}
print(my_dict['name'])
print(my_dict.get('age'))
my_dict['age'] = 27
print(my_dict)
my_dict['address'] = 'Downtown'
print(my_dict)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)
print(squares.popitem())
print(squares)
squares.clear()
print(squares)
#del squares

marks = {}.fromkeys(['Math', 'English', 'Science'], 0)
print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks.keys())))

#comprehension
squares = {x: x*x for x in range(6)}
print(squares)

squares = {}
for x in range(6):
    squares[x] = x*x*x
print(squares)

odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(odd_squares)

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(1 in squares)
print(2 not in squares)
print(49 in squares)

squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
    
squares = {0: 0, 1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print(all(squares))
print(any(squares))
print(len(squares))
print(sorted(squares))

