#python unicode
my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

str1 = 'programiz'
print('str = ', str1)
print('str[0] = ', str1[0])
print('str[-1] = ', str1[-1])
print('str[1:5] = ', str1[1:5])
print('str[5:-2] = ', str1[5:-2])

str1 = 'Hello'
str2 ='World!'
print('str1 + str2 = ', str1 + str2)
print('str1 * 3 =', str1 * 3)

count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

str3 = 'cold'
list_enumerate = list(enumerate(str3))
print('list(enumerate(str3) = ', list_enumerate)
print('len(str) = ', len(str3))

print('''He said, "What's there?"''')
print('He said, "What\'s there?"')
print("He said, \"What's there?\"")

default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)

