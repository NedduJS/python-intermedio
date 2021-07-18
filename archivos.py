def read():
    numbers = []
    with open("./files/numbers.txt", "r") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Nestor", "Eduardo", "Marta", "Susana", "Jose"]
    with open("./files/names.txt", "w") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def run():
    read()


if __name__ == '__main__':
    run()
