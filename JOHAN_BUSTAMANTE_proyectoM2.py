#Longitud de frase

#Intentos para completar de manera correcta la frase
def solicitarPalabra (intentosMax):
    intentos = 0
    intentosMax = 3
    
    #Ciclo hasta que se complete la cantidad de intentos permitidos o hacerlo bien
    #Me base en el reto de la contraseña y reciclé un poco de codigo de la caluladora de IMC
    while intentos < intentosMax:
        palabra = input('Ingresa una palabra mayor a 4 caracteres y menor a 8: ')

        #len nos permite contar la cantidad de caracteres en una variable str o lista
        if len(palabra) < 4:
            print('Tu palabra tiene menos de 4 caracteres')
            print('Trata de nuevo')
        elif len(palabra) > 8:
            print('Tu palabra tiene más de 8 caracteres')
            print('Trata de nuevo')
        elif 4 < len(palabra) < 8:
            confirmarPalabra = input('Repita su palabra')

            if palabra == confirmarPalabra:
                print('Buena palabra')
                return
            else:
                print('Trate de nuevo')

        intentos = intentos + 1
    
    if intentos == 3:
        print('Demaciados intentos')
#Para resolver el problema llamar a la funsion
#Lo hice de esta manera para probar algo nuevo
#El codigo funciona perfectamente sin el la funcion comentando la linea 4 y 36
solicitarPalabra(intentosMax)




#Encuentra Los Cuadrantes

#Para ingresar varios valores a las cordenadas y no reiniciar el codigo
#Hacaerlo más practico e interactivo
cont = True
while cont == True:
    try:
        cantidadCoordenadas = int(input('Ingrese la cantidad de coordenadas a tratar '))
        if cantidadCoordenadas > 0:
            cont = False
        else:
            print('Ingresa un valor mayor a 0')
    
    except ValueError:
        print('Ingresa un número válido')

while cantidadCoordenadas > 0:
    #Pedier la cordenada
    aux = True
    while aux == True:
        try:
            #float es para trabajar con coordenadas con valores de num. Real
            x = float(input('Ingrese cordenada "X"'))

            if 0 >= x or x > 0:
                aux = False
        
        #Para reiniciar el while si no nos dan un numero y no marque error la consola
        except ValueError:
                print('Agregue un valor valido') 

    aux = True
    while aux == True:
        try:
            y = float(input('Ingrese cordenada "Y"'))

            if 0 >= y or y > 0:
                aux = False

        except ValueError:
                print('Agregue un valor valido') 

    #Resultados de en que cuadrante o eje se encuentra así como la coordenada dicha
    if x==0 and y==0:
        print('Origen (' + repr(x) + ', ' + repr(y) + ')')
    elif x == 0:
        print('Eje Y (' + repr(x) + ', ' + repr(y) + ')')
    elif y == 0:
        print('Eje X (' + repr(x) + ', ' + repr(y) + ')')
    elif x > 0 and y > 0:
        print('Cuadrante I (' + repr(x) + ', ' + repr(y) + ')')
    elif x < 0 and y > 0:
        print('Cuadrante II (' + repr(x) + ', ' + repr(y) + ')')
    elif x < 0 and y < 0:
        print('Cuadrante III (' + repr(x) + ', ' + repr(y) + ')')
    elif x > 0 and y < 0:
        print('Cuadrante IV (' + repr(x) + ', ' + repr(y) + ')')
    
    cantidadCoordenadas = cantidadCoordenadas - 1