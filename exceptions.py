def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        else:
            print(string == string[::-1])
    except ValueError as ve:
        print(ve)
        return False
    finally:
        print("Programa ejecutado")


try:
    palindrome(12)
except TypeError:
    print("Solo se puede ingresar textos")
