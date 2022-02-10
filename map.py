my_list = [1, 2, 3, 4, 5]

# lambda function that receives a list and returns a list
add = list(map(lambda x: x**x, my_list))

print(add)
