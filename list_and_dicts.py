def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Kevin", "lastname": "Ochoa"}

    super_list = [
        {"firstname": "Enrique", "lastname": "Perez"},
        {"firstname": "Erika", "lastname": "Orinecía"},
        {"firstname": "Luis", "lastname": "Garcia"},
        {"firstname": "Susana", "lastname": "Xopa"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-2, -1, 0, 1, 2],
        "floationg_nums": [1.1, 4.5, 8.2, 9.2],
    }

    for key, value in super_dict.items():
            print(f"{key}-{value}")


# entrypoint
# execute the function when we start our .py file
if __name__ == '__main__':
    run()
