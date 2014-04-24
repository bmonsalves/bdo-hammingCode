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

def autocompletar(cadena):
	cadena = list(cadena)
 
	x = posicion = 0	
	while posicion < len(cadena):
		posicion = 2 ** x
		if posicion < len(cadena):
			cadena.insert(posicion-1, "*")
		else:
			break
		x += 1
 
	cadena = "".join(cadena)
	return cadena
 
def calcularFila(cadenaAuto, salto, cadenaTemporal=""):

	originalCadenaAuto = cadenaAuto

	cadenaAuto = cadenaAuto[salto-1:]

	n = "-"*(salto-1)
	cadenaTemporal += n 
 
	n = "-"*salto
	nsalto = salto * 2
	while len(cadenaAuto) > 0:

		cadenaTemporal += cadenaAuto[:salto]

		cadenaAuto = cadenaAuto[nsalto:]

		cadenaTemporal += n
		
	cadenaTemporal = cadenaTemporal[:len(originalCadenaAuto)]
 
	return cadenaTemporal
 
def obtenerFilas(cadenaAuto):
	filasDeParidad = dict()
 
	totalFilas = cadenaAuto.count("*")
	filaActual = 0

	while totalFilas > filaActual:
		salto = 2 ** filaActual
		filasDeParidad[salto] = calcularFila(cadenaAuto, salto) 
		filaActual += 1
	return filasDeParidad
 

def main():
	caracter = raw_input('ingrese un caracter: ')
	print "-----------------"
	if len(caracter) < 2:
		cadena = ascii_to_bin(caracter)
		print "Cadena de entrada:", cadena
		cadenaAuto = autocompletar(cadena)
		originalCadenaAuto = cadenaAuto
		print "-----------------"
		print "Cadena a analizar: 	", cadenaAuto
		filas = obtenerFilas(cadenaAuto)
		print "paridad 1 		", filas[1]
	 	print "paridad 2 		", filas[2]
	 	print "paridad 4 		", filas[4]
	 	print "paridad 8 		", filas[8]
		
		print "-----------------"
		
	else:
		print "ingrese solo un caracter"	
 
 
main()