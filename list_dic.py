def run():
    my_list = [1, "Hello", True, 4.35]
    my_dict = {"firstName": "Nestor", "lastName": "Mamani"}

    super_list = [
        {"firstName": "Nestor", "lastName": "Mamani"},
        {"firstName": "Miguel", "lastName": "Torres"},
        {"firstName": "Pepe", "lastName": "Rodelo"},
        {"firstName": "Susana", "lastName": "Martinez"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, values in super_dict.items():
        print(key, "-", values)


if __name__ == '__main__':
    run()
