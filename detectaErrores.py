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

def generaError(lista):

	cambiarEnLista = random.randrange(3)
	cambiarEnBinario = random.randrange(7)
	valor = lista[cambiarEnLista]
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
		
	lista[cambiarEnLista] = valor

	return lista

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
	n = "N"*(salto-1)
	cadenaTemporal += n 
 
	n = "N"*salto
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
	return filasDeParidad
 
def buscarErrores(filasDeParidad):
	''' Buscamos las filas que las suma de sus bits sea impar. '''
	filasErroneas = list()
	for llave, contenido in filasDeParidad.items():
		sumatoria = 0
		for elemento in contenido:
			for caracter in elemento:
				if caracter != "*" and caracter != "N":
					sumatoria += int(caracter)
		if sumatoria % 2 != 0: 
			error = True
			# significa que es impar
			filasErroneas.append(llave)
		else:
			error = False
	return filasErroneas, error
 
def buscamosRelacionErrores(bitsFilasErroneas):
	columnasRelacionadas = list()
	for indice, elementosFilas in enumerate(bitsFilasErroneas):
		centinela = False
		for bit in elementosFilas:
			try:
				# si los numeros se pueden convertir a enteros
				# significa que las columnas estan relacionadas
				int(bit)
				centinela = True
			except:
				centinela = False
				break
		if centinela:
			columnasRelacionadas.append(indice)
	return columnasRelacionadas
 
def buscarColumnasRelacionadas(filas, filasErroneas):
	longitud = len(filas.values()[0])
	
	bitsFilasErroneas = list()
	for i in range(longitud):
		bits = ""
		copyFilasErroneas = list(filasErroneas)
		while len(copyFilasErroneas) > 0:
			# asignamos la fila a buscar
			filaObjetivo = copyFilasErroneas.pop(0)
			for j in filasErroneas:
				if j == filaObjetivo:
					# ... y guardamos su elemento
					bits += filas[j][i]
		bitsFilasErroneas.append(bits)
 
	''' Ahora que tenemos los bits que se forman con cada fila erronea,
	tenemos que encontrar cuales columanas estan relacionadas.
	'''
	columnasRelacionadas = buscamosRelacionErrores(bitsFilasErroneas)
	return columnasRelacionadas
 
def quitarEspaciosParidad(cadenaAuto):
	return cadenaAuto.replace("*", "")


import random
def main():
	lista = []
	listaError = []
	caracter = raw_input('ingrese palabra de 4 caracteres: ')
	print "-----------------"
	if len(caracter) == 4:
		caracter = list(caracter)

		for i in caracter:
			lista.append(ascii_to_bin(i))
		
		print "Cadena de entrada binario: 	", lista

		listaError = generaError(lista)

		print "Cadena de entrada con error 	",listaError
		
		print "-----------------"
		
	else:
		print "solo palabra de 4 caracteres"	
 
 
main()