# import reduce
from functools import reduce

my_list = [2, 2, 2, 2, 2]

# lambda function that receives a list and returns an int
all_multiplied = reduce(lambda a, b: a * b, my_list)

print(all_multiplied)
