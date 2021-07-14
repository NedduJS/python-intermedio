from functools import reduce


def run():
    # filter
    my_list = [1, 2, 3, 4, 5]

    odd = list(filter(lambda i: i % 2 != 0, my_list))
    squares = list(map(lambda i: i**2, my_list))
    all_sum = reduce(lambda a, b: a+b, my_list)

    print(odd)
    print(squares)
    print(all_sum)


if __name__ == '__main__':
    run()
