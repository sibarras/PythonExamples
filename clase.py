# Listas de cada nivel
nivel1 = []
nivel2 = []
nivel3 = []

menucompleto = """       MENU
1. registrar puntajes obtenidos en la prueba de fin de nivel
2. Listar estudiantes que lograron hacer dos pruebas en un ano
3. Listar los estudiantes que aprobaron la prueba en cada nivel
4. Obtener el promedio del puntaje por nivel
5. Listar todos los estudiantes que realizaron la prueba sin repetirlos

6. Finalizar programa


"""


def menu():
    while True:
        print(menucompleto)
        opcion = int(input('ingresa el numero de la opcion elegida: '))
        print('\n\n')
        if opcion == 1:
            ide = input('Ingresa tu id: ')
            nombre = input('Ingresa tu nombre: ')
            nota = int(input('Ingresa tu nota: '))
            ingresarNotas(ide, nombre, nota)
        elif opcion == 2:
            listaEstudiantesDosNiveles()
        elif opcion == 3:
            estudiantesAprobadosPorNivel()
        elif opcion == 4:
            promPuntajePorNivel()
        elif opcion == 5:
            todosLosEstudiantes()
        elif opcion == 6:
            break
        else:
            print('Opcion incorrecta, vuelva a elegir. \n\n')


def ingresarNotas(ide, nombre, nota):
    datos = [ide, nombre, nota]
    if datos not in nivel1:
        nivel1.append(datos)
    elif datos not in nivel2:
        nivel2.append(datos)
    elif datos not in nivel3:
        nivel3.append(datos)
    else:
        print('El estudiante ya realizo todos los examenes')
    del datos


def listaEstudiantesDosNiveles():
    estudiantesDosNiveles = []
    for datos in nivel1:
        if datos[0] in [nivel2[i][0] for i in range(len(nivel2))]:
            estudiantesDosNiveles.append[datos[:2]]
    for datos in nivel2:
        if datos[0] in [nivel3[i][0] for i in range(len(nivel3))]\
                    and datos[:2] not in estudiantesDosNiveles:
            estudiantesDosNiveles.append[datos[:2]]

    for estudiante in estudiantesDosNiveles:
        print('id: ', estudiante[0], '\tNombre: ', estudiante[1], sep='')
    print('\n\n')
    del estudiantesDosNiveles


def estudiantesAprobadosPorNivel():
    print("Aprobados del nivel 1:")
    for estudiante in nivel1:
        if estudiante[2] > 90:
            print('id: ', estudiante[0], '\tNombre: ', estudiante[1], sep='')

    print("\nAprobados del nivel 2:")
    for estudiante in nivel2:
        if estudiante[2] > 90:
            print('id: ', estudiante[0], '\tNombre: ', estudiante[1], sep='')

    print("\nAprobados del nivel 3:")
    for estudiante in nivel3:
        if estudiante[2] > 90:
            print('id: ', estudiante[0], '\tNombre: ', estudiante[1], sep='')
    print('\n\n')


def promPuntajePorNivel():
    suma = 0
    print("Promedio de puntajes nivel 1: ", end='')
    for puntaje in nivel1:
        suma += puntaje[2]
    print(suma/len(nivel1))

    suma = 0
    print("\nPromedio de puntajes nivel 2: ", end='')
    for puntaje in nivel2:
        suma += puntaje[2]
    print(suma/len(nivel2))

    suma = 0
    print("\nPromedio de puntajes nivel 3: ", end='')
    for puntaje in nivel3:
        suma += puntaje[2]
    print(suma/len(nivel3))
    print('\n\n')
    del suma


def todosLosEstudiantes():
    listadeestudiantes = []
    for estudiante in nivel1:
        listadeestudiantes.append(estudiante[:2])
    for estudiante in nivel2 and estudiante not in listadeestudiantes:
        listadeestudiantes.append(estudiante[:2])
    for estudiante in nivel3 and estudiante not in listadeestudiantes:
        listadeestudiantes.append(estudiante[:2])

    for estudiante in listadeestudiantes:
        print('Id: ', estudiante[0], '\tNombre: ', estudiante[1], sep='')
    del listadeestudiantes
    print('\n\n')

# ======================================= FIN DE FUNCIONES, INICIO DEL PROGRAMA ==============================================

menu()
