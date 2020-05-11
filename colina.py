import json
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
        print(PILAVIAJE)
    else:
        print("Busco camino de "+donde+" a "+fin)
        opc = [e[1] for e in archivo['CAMINOS'] if e[0] == donde]
        print("Mis opciones son: ")
        print(opc)
        prueba = [e[0] for e in PILAVIAJE if e[0] == opc[0]]
        print("¿EXISTE ESTE ELEMENTO ANTERIOREMENTE?")
        print(prueba)
        if prueba == []:
            print("NO, entonces camino por aqui")
            PILAVIAJE.append(opc[0])
            print(PILAVIAJE)
            next(opc[0],fin)
        else:
            print("SI, entonces compruebo: ")
            print(opc[1])
            print(" esta en esta lista")
            print(PILAVIAJE)
            prueba2 =  [e[0] for e in PILAVIAJE if e[0] == opc[1]]
            print("¿EXISTE ESTE ELEMENTO ANTERIOREMENTE?")
            print(prueba2)
            if prueba2 == []:
                print("NO, entonces camino por aqui")
                PILAVIAJE.append(opc[1])
                print(PILAVIAJE)
                next(opc[1],fin)
            else:
                print("SI, entonces compruebo: ")
                print(opc[2])
                print(" esta en esta lista")
                print(PILAVIAJE)
                prueba3 =  [e[0] for e in PILAVIAJE if e[0] == opc[2]]
                print("¿EXISTE ESTE ELEMENTO ANTERIOREMENTE?")
                print(prueba3)
                if prueba3 == []:
                    print("NO, entonces camino por aqui")
                    PILAVIAJE.append(opc[2])
                    print(PILAVIAJE)
                    next(opc[2],fin)

            
next(INICIO,DESTINO)
    