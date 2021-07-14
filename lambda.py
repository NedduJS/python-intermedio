def run():
    word = input("Escribe una palabra: ")

    def palindromo(string): return string == string[::-1]
    print(palindromo(word))


if __name__ == '__main__':
    run()
