def palidrome(string):
    assert len(string) > 0, "Ingrese un texto :)"
    assert not string.isnumeric(), "Debes ingresar un texto"
    return string == string[::-1]


def run():
    user_input = input("Ingrese un texto: ")
    print(palidrome(user_input))


if __name__ == "__main__":
    run()
