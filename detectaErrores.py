def ascii_to_bin(char):
	ascii = ord(char)
	bin = []
	while (ascii > 0):
		if (ascii & 1) == 1:
			bin.append("1")
		else:
			bin.append("0")
		ascii = ascii >> 1
	bin.reverse()
	binary = "".join(bin)
	zerofix = (8 - len(binary)) * '0'
	return zerofix + binary

def bin_to_ascii(cadena):
	caracter= chr(int(cadena, 2))
	return caracter

def generaError(listaError):

	cambiarEnLista = random.randrange(3)
	cambiarEnBinario = random.randrange(7)
	valor = listaError[cambiarEnLista]
	caracter = list(valor)

	print "posicion del error: ",cambiarEnLista
	if caracter[cambiarEnBinario] == '1':
		#print "a cambiar", caracter[cambiarEnBinario]
		caracter[cambiarEnBinario] = '0'
		valor = ''.join(map(str, caracter))
	else:
		#print "a cambiar", caracter[cambiarEnBinario]
		caracter[cambiarEnBinario] = '1'
		valor = ''.join(map(str, caracter))
		
	listaError[cambiarEnLista] = valor

	return listaError, cambiarEnLista

def autocompletar(cadena):
	''' Buscamos las posiciones de los datos de paridad '''
	# convertimos la cadena en lista
	cadena = list(cadena)
 
	x = posicion = 0	
	while posicion < len(cadena):
		posicion = 2 ** x
		# insertamos el valor de paridad
		if posicion < len(cadena):
			cadena.insert(posicion-1, "*")
		else:
			break
		x += 1
 
	cadena = "".join(cadena)
	return cadena
 
def calcularFila(cadenaAuto, salto, cadenaTemporal=""):
	'''Este metodo es para calcular paridades individuales '''
	originalCadenaAuto = cadenaAuto
 
	# recortamos la cadena para que empiece en ese elemento
	cadenaAuto = cadenaAuto[salto-1:]
	# agregamos una varible apoyo para conservar las "coordenadas"
	n = "-"*(salto-1)
	cadenaTemporal += n 
 
	n = "-"*salto

	nsalto = salto * 2
	while len(cadenaAuto) > 0:
		# tomamos los elementos segun la paridad
		cadenaTemporal += cadenaAuto[:salto]
		# brincamos los elementos segun la paridad
		cadenaAuto = cadenaAuto[nsalto:]
		# agregamos una varible apoyo para conservar las coordenadas
		cadenaTemporal += n
		
	# truncamos hasta el largo de la cadena con paridad
	cadenaTemporal = cadenaTemporal[:len(originalCadenaAuto)]
	return cadenaTemporal
 
def obtenerFilas(cadenaAuto):

	filasDeParidad = dict()
 		
	totalFilas = cadenaAuto.count("*")
	filaActual = 0
	# hacemos una fila por cada elemento de paridad
	while totalFilas > filaActual:
		salto = 2 ** filaActual
		filasDeParidad[salto] = calcularFila(cadenaAuto, salto) 
		
		filaActual += 1

	for i in [1,2,4,8]:
		if filasDeParidad[i].count('1') % 2 == 0:
			filasDeParidad[i] = filasDeParidad[i].replace("*","0")
		else:
			filasDeParidad[i] = filasDeParidad[i].replace("*","1")

	return filasDeParidad

def oFilas(cadenaAuto):

	filasDeParidad = dict()
 		
	totalFilas = cadenaAuto.count("*")
	filaActual = 0
	# hacemos una fila por cada elemento de paridad
	while totalFilas > filaActual:
		salto = 2 ** filaActual
		filasDeParidad[salto] = calcularFila(cadenaAuto, salto) 
		
		filaActual += 1

	return filasDeParidad

def obtenerFilasErr(cadenaAuto,paridades1):
	x=0
	filasDeParidad = dict()
 		
	totalFilas = cadenaAuto.count("*")
	filaActual = 0
	# hacemos una fila por cada elemento de paridad
	while totalFilas > filaActual:
		salto = 2 ** filaActual
		filasDeParidad[salto] = calcularFila(cadenaAuto, salto) 
		
		filaActual += 1

	for i in [1,2,4,8]:
		if filasDeParidad[i].count('1') == paridades1[x] :
			if filasDeParidad[i].count('1') % 2 == 0:
				filasDeParidad[i] = filasDeParidad[i].replace("*","0")
			else:
				filasDeParidad[i] = filasDeParidad[i].replace("*","1")
		else:
			if filasDeParidad[i].count('1') % 2 != 0:
				filasDeParidad[i] = filasDeParidad[i].replace("*","0")
			else:
				filasDeParidad[i] = filasDeParidad[i].replace("*","1")

		x=x+1

	return filasDeParidad

def detectarError(filas):
	filasConErrores = []
	for i in [1,2,4,8]:
		if filas[i].count('1') % 2 != 0:
		 	filasConErrores.append(i)

	print "paridades con errores",filasConErrores
	return filasConErrores

def corregirError(cadenaAuto, errores):
	cadena = list(cadenaAuto)
	control = 0
	for i in errores:
		control = control + i

	if cadena[control-1] =="1":
		cadena[control-1] = "0"
	else:
		cadena[control-1] = "1"

	cadenaFinal = "".join(cadena)

	return cadenaFinal

import random, sys, copy
def main():
	
	caracter = raw_input('ingrese palabra de 4 caracteres: ')
	print "-----------------"
	if len(caracter) == 4:

		print "GENERAR ERROR"
		caracter = list(caracter)

		lista = []
		paridades1 = []
		cadenaCorregida = []
		
		for i in caracter:
			lista.append(ascii_to_bin(i))
		
		print "Cadena de entrada binario: 	", lista

		listaError= copy.copy(lista)

		(listError, posError) = generaError(listaError)
		print "Cadena de entrada con errores: 	",listaError

		print "-----------------"

		print "PALABRA CON ERROR"
		
		for i in listaError:
			carac = bin_to_ascii(i)
			sys.stdout.write(carac)

		print "\n-----------------"
		i = 0
		for x in lista:
			if x == listaError[i]:
				#meter a lista cadena a analizar
				cadenaAuto = autocompletar(x)
				print "-----------------"
				print "Cadena a analizar: 	", cadenaAuto
				filas = obtenerFilas(cadenaAuto)
				print "paridad 1 		", filas[1]
			 	print "paridad 2 		", filas[2]
			 	print "paridad 4 		", filas[4]
			 	print "paridad 8 		", filas[8]
				
				cadenaCorregida.append(cadenaAuto)
				
			else:
				cadenaAuto1 = autocompletar(x)
				cadenaAuto = autocompletar(listaError[i])
				print "-----------------"
				print "Cadena a analizar: 	",cadenaAuto
				filas1 = oFilas(cadenaAuto1)

				for x in [1,2,4,8]:
					paridades1.append(filas1[x].count("1"))

				filas = obtenerFilasErr(cadenaAuto,paridades1)
				print "paridad 1 		", filas[1]
			 	print "paridad 2 		", filas[2]
			 	print "paridad 4 		", filas[4]
			 	print "paridad 8 		", filas[8]
				
				errores = detectarError(filas)

				cadenaNueva = corregirError(cadenaAuto,errores)

				cadenaCorregida.append(cadenaNueva)

			i = i+1
		print "-----------------"
		print "CADENA CORREGIDA"
		for x in cadenaCorregida:
			x=x.replace("*","")
			carac = bin_to_ascii(x)
			sys.stdout.write(carac)
			
		print "\n-----------------"
	else:
		print "solo palabra de 4 caracteres"	
 
 
main()