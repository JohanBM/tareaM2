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
            x = float(input('Ingrese cordenada "X"'))

            if 0 >= x or x > 0:
                aux = False

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