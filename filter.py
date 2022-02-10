my_list = [1, 3, 5, 1, 3, 5, 32, 124, 1, 5, 99]

# lambda function that receives a list and returns a list
add = list(filter(lambda x: x % 2 != 0, my_list))

print(add)
