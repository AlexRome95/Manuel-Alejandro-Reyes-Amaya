import json
import random
with open('camino.json', 'r') as f:
    archivo = json.load(f)
    #print(archivo['CAMINOS'])
    print("THIS IS THE REMIX DEL CODIGO")
INICIO = "I"
DESTINO = "Z"

PILAVIAJE = ["I"]
PILADONDEVENGO = ["I"]

def next(donde,fin):
    if donde == fin:
        print("********* ESTE ES EL CAMINO MÁS CORTO *********")
        print(PILAVIAJE)
    else:
        print("Busco camino de "+donde+" a "+fin)
        opc = [[e[1],e[2]] for e in archivo['CAMINOS'] if e[0] == donde]
        print("Mis opciones son: ")
        print(opc)
        print("Ordena mis opciones de menor a mayor")
        op = sorted(opc, key = lambda e: int(e[1]))
        print(op)
        prueba = [e[0] for e in PILAVIAJE if e[0] == op[0][0]]
        print("¿EXISTE ESTE ELEMENTO ANTERIOREMENTE?")
        print(prueba)
        if prueba == []:
            print("NO, entonces camino por aqui")
            PILAVIAJE.append(op[0][0])
            print(PILAVIAJE)
            next(op[0][0],fin)
        else:
            print("SI, entonces compruebo: ")
            print(op[1][0])
            print(" esta en esta lista")
            print(PILAVIAJE)
            prueba2 =  [e[0] for e in PILAVIAJE if e[0] == op[1][0]]
            print("¿EXISTE ESTE ELEMENTO ANTERIOREMENTE?")
            print(prueba2)
            if prueba2 == []:
                print("NO, entonces camino por aqui")
                PILAVIAJE.append(op[1][0])
                print(PILAVIAJE)
                next(op[1][0],fin)
            else:
                print("SI, entonces compruebo: ")
                print(op[2][0])
                print(" esta en esta lista")
                print(PILAVIAJE)
                prueba3 =  [e[0] for e in PILAVIAJE if e[0] == op[2][0]]
                print("¿EXISTE ESTE ELEMENTO ANTERIOREMENTE?")
                print(prueba3)
                if prueba3 == []:
                    print("NO, entonces camino por aqui")
                    PILAVIAJE.append(op[2][0])
                    print(PILAVIAJE)
                    next(op[2][0],fin)

            
next(INICIO,DESTINO)
    