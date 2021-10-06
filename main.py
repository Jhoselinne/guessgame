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

#humanguess()

def computerguess():
    number=random.randrange(0,1000)
    bandera=False
    
    while(bandera==False):
        print(number)
        print("Este es tu numero")
        opc=input("Si | No:  ").lower()
        if(opc=="no"):
            print("Tu numero es mayor o menor al mio")
            opc2=input("Mayor | Menor: ").lower()
            if(opc2 == "menor"):
                newnumber=random.randrange(0,number)
                number=newnumber
            else: 
                newnumber=random.randrange(number,1000)
                number=newnumber
        else:
            bandera= True
computerguess()




    

