def solicitarPalabra (intentosMax):
    intentos = 0
    intentosMax = 3

    while intentos < intentosMax:
        palabra = input('Ingresa una palabra mayor a 4 caracteres y menor a 8: ')

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

solicitarPalabra(intentosMax)