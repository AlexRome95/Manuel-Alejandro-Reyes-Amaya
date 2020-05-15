"""
nreinas
"""
#matrix  = [[0,0,0,0],[0,0,0,0,],[0,0,0,0],[0,0,0,0]]

#algoritmo de busqueda en profundidad para la solucion del
#problema de las N-Reinas con Fuerza Bruta

def soluciona(reinas,mat,numreinas):
    pila = []
    numreinas -= 1 
    print(numreinas)

def imprimematriz(matriz):
    a=""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a += str(matriz[i][j])+'\t'
        print(a)
        a=""

reinas = 4
numreinas = reinas
mat = []
for i in range(reinas):
    mat.append([])
    for j in range(reinas):
        mat[i].append(0)
imprimematriz(mat)
print("Reinas: "+str(reinas))
print("NR: "+str(numreinas))
soluciona(reinas, mat, numreinas)

"""
def nreinas(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            soluciona(matriz,i,j)


def verticalhorizontal(matriz,x,y):
    for i in range(len(matriz)):
        matriz[i][x]=2
    for i in range(len(matriz)):
        matriz[y][i]=2
    return matriz

def soluciona(matriz,x,y):
    busca
    
    print("X: "+str(x)+" Y: "+str(y))
    print("**************************")
    imprimematriz(matriz)
    print("**************************")
    matriz=verticalhorizontal(matriz,x,y)
    imprimematriz(matriz)



def imprimematriz(matriz):
    a=""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            a += str(matriz[i][j])+'\t'
        print(a)
        a=""

R = nreinas(matrix)
print(R)


    
def diagonales(matriz,posiciony,posicionx)
    for i in range(len(matriz)):




def check_legal(board):
    legal = True
    for i, ci in enumerate(board):
        for cj in board[(i + 1):]:
            if abs(ci - cj) == abs(board.index(ci) - board.index(cj)):
                legal = False
    return legal

imprimematriz(matrix)
matrizz = verticalhorizontal(matrix,0,0)
print("----------------------------")
imprimematriz(matrizz)
print("____________________________")

"""