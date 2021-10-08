from random import *

def humanguess():
    number=randrange(0,10)
    numero= -1

    while numero!=number:
        numero=int(input(f"JUEGO 1 'Human guess': #{number} \nIngrese un número:"))
        if number==numero:
            print(f"¡ F E L I C I D A D E S !, le atinaste al número, que es: {numero}")
        elif numero>number:
            print(f"El número que escogiste es mayor que el número a adivinar {numero}")
        else:
            print(f"El número que escogiste es menor que el número a adivinar  {numero}")

humanguess()

def computerguess():
    bandera=False
    min=0
    max=1000
    number=randint(min,max)
    
    while(bandera==False):
        print(f"\nJUEGO 2: 'Computer guess'\n¿Esté es tu número? {number}")
        opc=input("Si | No:  ").lower()
        if(opc=="no"):
            print("¿Tu número es mayor o menor al mío?")
            opc2=input("Mayor | Menor: ").lower()
            if(opc2 == "menor"):
                max=number
                number=randint(min,max)
            else: 
                min=number
                number=randint(min,max)
        else:
            print("¡ F E L I C I D A D E S !, le has atinado al número y era: #"+str(number))
            bandera= True        
computerguess()




    

