import random
def humanguess():
    number=random.randrange(0,10)
    numero= -1
    print(number)

    while numero!=number:
        numero=int(input("Ingrese un número:"))
        if number==numero:
            print(f"Felicidades le atino, el numero era {numero}")
        elif numero>number:
            print(f"El numero que escogio es mayor {numero}")
        else:
            print(f"El numero es menor {numero}")

humanguess()
    

