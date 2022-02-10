from re import S


def run():
    # dictionary that saves 1 to 3, fulfilling the condition that i is not a multiple of 3
    my_dict = {i: i ** 3 for i in range(1, 101) if i % 3 != 0}
    print(my_dict)

if __name__ == '__main__':
    run()
