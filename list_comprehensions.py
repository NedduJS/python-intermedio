def run():
    squares = [i**2 for i in range(1, 120) if i % 2 != 0]
    print(squares)


if __name__ == '__main__':
    run()
