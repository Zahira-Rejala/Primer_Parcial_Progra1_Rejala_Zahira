from UTN_Heroes_Dataset.utn_pp import get_original_matrix, mostrar_matriz_texto_tabla
import os

matriz_concesionaria = get_original_matrix()

#Funciones
#Ejercicio 1
columnas = ["Marca", "Modelo", "Cantidades", "Precios", "Ganancias"]
#mostrar_matriz_texto_tabla(matriz_concesionaria, columnas)
lista_marca = [[] for _ in range(20)]
lista_modelo = [[] for _ in range(20)]
lista_cantidades = [[] for _ in range(20)]
lista_precios = [[] for _ in range(20)]
lista_ganancias = [[] for _ in range(20)]
matriz = [[] for _ in range(20)]


def cargar_datos(lista_marca:list[list], lista_modelo:list[list], lista_cantidades:list[list], lista_precios:list[list], lista_ganancias:list[list], matriz_concesionaria:list[list]) -> None:
    """Esta funcion lo que hace es cargar los datos en la lista que corresponde

    Args:
        lista_marca (list[list]): Recibe una lista de listas vacia
        lista_modelo (list[list]): Recibe una lista de listas vacia
        lista_cantidades (list[list]): Recibe una lista de listas vacia
        lista_precios (list[list]): Recibe una lista de listas vacia
        lista_ganancias (list[list]): Recibe una lista de listas vacia
        matriz_concesionaria (list[list]): Recibe una lista de listas vacia

    No retorna nada
    """
    for j in range(len(matriz_concesionaria[0])):
        lista_marca[j].append(matriz_concesionaria[0][j])
        lista_modelo[j].append(matriz_concesionaria[1][j])
        lista_cantidades[j].append(matriz_concesionaria[2][j])
        lista_precios[j].append(matriz_concesionaria[3][j])
        lista_ganancias[j].append(matriz_concesionaria[4][j])


def cargar_matriz(matriz:list[list]) -> list[list]:
    """Esta funcion lo que hace es cargar a una matriz vacia los datos de cada garage

    Args:
        matriz (list[list]): Recibe una lista de listas vacia

    Returns:
        list[list]: Retorna una matriz
    """
    for i in range(len(matriz_concesionaria)):
        for j in range(len(matriz_concesionaria[i])):
            matriz[j].append(matriz_concesionaria[i][j])
    return matriz

#Ejercicio 2
def cantidad_total_vehiculos(lista_cantidad: list[list]):
    """Lo que hace esta funcion es con un acumulador contar cuantos vehiculos hay en total

    Args:
        lista_cantidad (list[list]): recibe lista de listas

    Returns:
        _type_: Devuelve el acumulador
    """
    acumulador = 0 
    for i in range(len(lista_cantidad)):
        for j in range(len(lista_cantidad[i])):
            acumulador += lista_cantidad[i][j]
    print(f"La cantidad de vehiculos en todos los garage es de {acumulador}")
    return acumulador

#Ejercicio 3
def menos_unidades(lista_cantidades: list[list], lista_marca: list[list], lista_modelo: list[list], lista_precios: list[list]):
    """Lo que hace esta funcion es mostrar el garage con menor unidades

    Args:
        lista_cantidades (list[list]): Recibe una lista de listas 
        lista_marca (list[list]): Recibe una lista de listas 
        lista_modelo (list[list]): Recibe una lista de listas
        lista_precios (list[list]): Recibe una lista de listas 
    """
    minimo = 0 
    vehiculo_menor = None
    for i in range(len(lista_cantidades)):
        for j in range(len(lista_cantidades[i])):
            if minimo == 0 or minimo > lista_cantidades[i][j]:
                minimo = lista_cantidades[i][j]
                vehiculo_menor = lista_cantidades[i][j]
                garaje = i
                marca = lista_marca[i][j]
                modelo = lista_modelo[i][j]
                precio = lista_precios[i][j]


    print(f"El garaje que almacena menos unidades de vehiculos es el garaje {garaje + 1} con {vehiculo_menor} de la marca: {marca}, modelo: {modelo} y precio: ${precio}")


#Ejercicio 4
def mas_unidades(lista_cantidades: list[list], lista_marca: list[list], lista_modelo: list[list], lista_precios: list[list]):
    """Lo que hace esta funcion es mostrar el garage con menor unidades

    Args:
        lista_cantidades (list[list]): Recibe una lista de listas 
        lista_marca (list[list]): Recibe una lista de listas 
        lista_modelo (list[list]): Recibe una lista de listas
        lista_precios (list[list]): Recibe una lista de listas 
    """
    maximo = 0 
    vehiculo_menor = None
    for i in range(len(lista_cantidades)):
        for j in range(len(lista_cantidades[i])):
            if maximo == 0 or maximo < lista_cantidades[i][j]:
                maximo = lista_cantidades[i][j]
                vehiculo_menor = lista_cantidades[i][j]
                garaje = i
                marca = lista_marca[i][j]
                modelo = lista_modelo[i][j]
                precio = lista_precios[i][j]


    print(f"El garaje que almacena mas unidades de vehiculos es el garaje {garaje + 1} con {vehiculo_menor} de la marca: {marca}, modelo: {modelo} y precio: ${precio}")






#Ejercicio 5
def ganancia(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            ganancia = matriz[2][j] * matriz[3][j]
            matriz[4][j] = ganancia




#Ejercicio 6
def garaje_con_seis_o_mas(lista_cantidades):
    """Esta funcion lo que hace es contar cuando garajes tienen 6 o mas vehiculos

    Args:
        lista_cantidades (_type_):  Recibe una lista de listas 
    """
    contador = 0
    for i in range(len(lista_cantidades)):
        for j in range(len(lista_cantidades[i])):
            if lista_cantidades[i][j] >= 6:
                contador += 1
    print(f"La cantidad de garajes que almacenaron 6 o mas unidades de vehiculos son {contador}")

#Ejercicio 7

def marcas(lista_marca: list[list], lista_cantidades: list[list], marca: str):
    """Lo que hace esta funcion es acumular por marca la cantidad

    Args:
        lista_marca (list[list]):Recibe una lista de listas 
        lista_cantidades (list[list]): Recibe una lista de listas 
        marca (str): Recibe una marca

    Returns:
        _type_: Retorna el acumulador
    """
    acumulador = 0
    for i in range(len(lista_cantidades)):
        for j in range(len(lista_cantidades[i])):
            if lista_marca[i][j] == marca:
                acumulador += lista_cantidades[i][j]
    return acumulador


def porcentajes(lista_cantidades: list[list]):
    """Lo que hace esta funcion es sacar el totald de vehiculos y con eso el porcentaje de cada marca

    Args:
        lista_cantidades (list[list]): Recibe una lista de listas 
    """
    total_vehiculos = 0 
    for i in range(len(lista_cantidades)):
        for j in range(len(lista_cantidades[i])):
            total_vehiculos += lista_cantidades[i][j]
    marca_chevrolet = marcas(lista_marca, lista_cantidades, marca="Chevrolet")
    marca_toyota = marcas(lista_marca, lista_cantidades, marca="Toyota") 
    marca_fiat = marcas(lista_marca, lista_cantidades, marca="Fiat")
    marca_renault = marcas(lista_marca, lista_cantidades, marca="Renault")
    marca_volkswagen = marcas(lista_marca, lista_cantidades, marca="Volkswagen")
    marca_ford = marcas(lista_marca, lista_cantidades, marca="Ford")
    marca_audi = marcas(lista_marca, lista_cantidades, marca="Audi")
    marca_honda = marcas(lista_marca, lista_cantidades, marca="Honda")
    marca_nissan = marcas(lista_marca, lista_cantidades, marca="Nissan")
    marca_peugeot = marcas(lista_marca, lista_cantidades, marca="Peugeot")

    porcentaje_chevrolet = (marca_chevrolet / total_vehiculos) * 100
    porcentaje_toyota = (marca_toyota / total_vehiculos) * 100
    porcentaje_fiat = (marca_fiat / total_vehiculos) * 100
    porcentaje_renault = (marca_renault / total_vehiculos) * 100
    porcentaje_volkswagen = (marca_volkswagen / total_vehiculos) * 100
    porcentaje_ford = (marca_ford / total_vehiculos) * 100
    porcentaje_audi = (marca_audi / total_vehiculos) * 100
    porcentaje_honda = (marca_honda / total_vehiculos) * 100
    porcentaje_nissan = (marca_nissan / total_vehiculos) * 100
    porcentaje_peugeot = (marca_peugeot / total_vehiculos) * 100

    print(f"El porcentaje de la marca Chevrolet es %{porcentaje_chevrolet}")
    print(f"El porcentaje de la marca Toyota es %{porcentaje_toyota}")
    print(f"El porcentaje de la marca fiat es %{porcentaje_fiat}")
    print(f"El porcentaje de la marca Renault es %{porcentaje_renault}")
    print(f"El porcentaje de la marca volkswagen es %{porcentaje_volkswagen}")
    print(f"El porcentaje de la marca ford es %{porcentaje_ford}")
    print(f"El porcentaje de la marca audi es %{porcentaje_audi}")
    print(f"El porcentaje de la marca honda es %{porcentaje_honda}")
    print(f"El porcentaje de la marca nissan es %{porcentaje_nissan}")
    print(f"El porcentaje de la marca peugeot es %{porcentaje_peugeot}")

    lista_porcentaje = []
    lista_porcentaje.append(porcentaje_chevrolet)
    lista_porcentaje.append(porcentaje_toyota)
    lista_porcentaje.append(porcentaje_fiat)
    lista_porcentaje.append(porcentaje_renault)
    lista_porcentaje.append(porcentaje_volkswagen)
    lista_porcentaje.append(porcentaje_ford)
    lista_porcentaje.append(porcentaje_audi)
    lista_porcentaje.append(porcentaje_honda)
    lista_porcentaje.append(porcentaje_nissan)
    lista_porcentaje.append(porcentaje_peugeot)

    maximo = 0
    for i in range(len(lista_porcentaje)):
        if maximo == 0 or maximo < lista_porcentaje[i]:
            maximo = lista_porcentaje[i]
    print(f"La marca con mayor porcentaje es Chevrolet con {maximo}")

#Ejercicio 8
def selection(matriz, fila_elegida):
    cantidad_columnas = len(matriz[0])
    for i in range(cantidad_columnas - 1):
        indice_maximo = i
        for j in range(i + 1, cantidad_columnas):
            if matriz[fila_elegida][j] > matriz[fila_elegida][indice_maximo]:
                indice_maximo = j
            if indice_maximo != i:
                for indice_fila in range(len(matriz)):
                    matriz[indice_fila][i], matriz[indice_fila][indice_maximo] = matriz[indice_fila][indice_maximo], matriz[indice_fila][i]
    return matriz


#MENU
def menu_opciones():
    menu = """
    1-Obtener existencias: para ello deberá crear una función que cargue la existencia de 
    cada vehículo en todos los garajes y mostrarlos.
    2-Calcular por cada garaje la cantidad total de unidades almacenadas entre todos 
    los vehículos de la concesionaria.
    3-Datos completos del garaje que almacena menos unidades de vehículos.
    4-Máxima cantidad de unidades almacenadas entre todos los garajes.
    5-Obtener recaudación: para ello deberás crear una función que calcule la recaudación de cada garaje, 
    teniendo en cuenta su precio unitario y cantidad de unidades almacenadas en cada garaje.
    6-Cantidad de garajes que hayan almacenado 6 o más unidades de vehículos.
    7-Porcentaje de unidades de cada marca de vehículo sobre el total de vehículos almacenados 
    entre todos los garajes de la sede matriz. Además mostrar todos los datos del garaje con el máximo porcentaje de vehículos almacenados.
    8-Generar un informe con la recaudación de cada garaje, ordenada de mayor a menor.
    9-Salir de la consola
"""
    print(menu)

def validar_opcion(num_min: int, num_max:int) -> int:
    """Esta funcion lo que hace es validar que la opcion que ingresa el usuario este entre el rango de 
    opciones

    Args:
        num_min (int): Recibe el minimo el cual es un numero entero
        num_max (int): Recime el maximo el cual es un numero entero

    Returns:
        int: Va a retornar la opcion que el usuario va a escribir en el input
    """
    opcion = input(f"Ingrese una opcion [{num_min} - {num_max}]: ")

    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)
    return int(opcion)

def menu(lista_marca, lista_modelo, lista_cantidades, lista_precios, lista_ganancias, matriz_concesionaria, matriz, columnas):
    while True:
        menu_opciones()
        opcion = validar_opcion(1, 9)
        match opcion:
            case 1:
                cargar_datos(lista_marca, lista_modelo, lista_cantidades, lista_precios, lista_ganancias, matriz_concesionaria)
                cargar_matriz(matriz)
                mostrar_matriz_texto_tabla(matriz, columnas)
            case 2:
                cantidad_total_vehiculos(lista_cantidades)
            case 3:
                menos_unidades(lista_cantidades, lista_marca, lista_modelo, lista_precios)
            case 4:
                mas_unidades(lista_cantidades, lista_marca, lista_modelo, lista_precios)
            case 5:
                ganancia(matriz= matriz_concesionaria)
                mostrar_matriz_texto_tabla(matriz, columnas)
            case 6:
                garaje_con_seis_o_mas(lista_cantidades)
            case 7:
                porcentajes(lista_cantidades)
            case 8:
                selection(matriz, 4)
                mostrar_matriz_texto_tabla(matriz, columnas)
            case 9:
                break
        os.system("Pause")
        os.system("cls")

menu(lista_marca, lista_modelo, lista_cantidades, lista_precios, lista_ganancias, matriz_concesionaria, matriz, columnas)