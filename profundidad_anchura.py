"""
Cada funcion recibe la Carteta donde
empezara a buscar y el archivo a buscar

La funcion retorna True si encuentra 
el archivo, e imprime la ruta

en caso contrario retorna falso

def primeroProfundidad(Carpeta,Archivo):
	pass
def primeroAnchura(Carpeta,Archivo):
	pass
"""

"""
Manuel Alejandro Reyes Amaya
"""

import json
with open('base.json') as disco_duro:
	bd = json.load(disco_duro)

auxiliar=[]
recorrido=[]

def primeroProfundidad(Carpeta,Archivo):
	auxiliar.append(Carpeta)
	if Carpeta == Archivo:
		return Carpeta
	for k,v in bd:
		if k==Carpeta:
			resultado=primeroProfundidad(v,Archivo)
			if resultado:
				#print(resultado)
				recorrido.append(resultado)
				return k
	auxiliar.pop
	

def primeroAnchura(Carpeta,Archivo):
	opc=[[e[1]] for e in bd if e[0]==Carpeta]
	opc=list(opc)
	if opc == []:
		return
	print("Carpeta: "+Carpeta)
	print("Se buscara el archivo en la siguientes opciones")
	print(opc)
	for opcion in range(len(opc)):
		recorrido.append(opc[opcion][0])
		print("El archivo :"+opc[opcion][0]+" es "+Archivo)
		if Archivo == opc[opcion][0]:
			print("Aqui esta")
			auxiliar.append(opc[opcion][0])
			return opc[opcion][0]
		else:
			print("No, no lo es")
	print("Como no lo encontre en ese nivel, lo buscare en el siguiente nivel de la opcion de las opciones anteriores")
	for opcion in range(len(opc)):
		busca = primeroAnchura(opc[opcion][0],Archivo)
		if busca:
			auxiliar.append(opc[opcion][0])
			return busca

"""
Primero en profundidad

"""
print("*************Primero Profundidad*************")

busca=primeroProfundidad("C:","Steam.exe")
recorrido.append("C:")
if busca:
	recorrido.reverse()
	print("Archivo encontrado en:")
	#Se llama recorrido por que primero lo ocupe en anchura y despues agrege esto en profundida xD
	print(recorrido)
	#Auxiliar imprime por donde fue
	print("Tube que buscar en: ")
	print(auxiliar)
else:
	print("No encontrado")
print("*************Primero Profundidad*************")
print("")
auxiliar=[]
recorrido=[]
print("************** Primero Anchura **************")
resultado = primeroAnchura("C:","Steam.exe")
if resultado:
	print("************** Primero Anchura **************")
	print("Tube que buscar en: ")
	print(recorrido)
	auxiliar.append("C:")
	auxiliar.reverse()
	print("Archivo encontrado en:")
	print(auxiliar)
	print("************** Primero Anchura **************")
else:
	print("************** Primero Anchura **************")
	print("No encontrado")
	print("************** Primero Anchura **************")
