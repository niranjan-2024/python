first_list = [1, 2, 2, 5]
second_list = [2, 5, 7, 9]

in_first = set(first_list)
in_second = set(second_list)

in_second_but_not_in_first = in_second - in_first

result = first_list + list(in_second_but_not_in_first)
print(result) 
