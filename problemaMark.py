# Este algoritmo se hizo para Simular la creación de carpetas y unos directorios hijos
# Se lee la cantidad de instrucciones
cantidad_instrucciones = int(input())
# Se define el arreglo de carpetas
diccionario_carpetas = {}
# Se define el arreglo de Mark
diccionario_carpetas["Mark"] = {}
# Se define la ubicación Actual al arranque
ubicacion_actual = "/Mark"
# Se define el proceso para imprimir, recibiendo el directorio padre, el arreglo de directorios y si es un nivel o un subnivel
def imprimir(directorio_padre, directorios, nivel):
    #Se imprime cual es el directorio padre
    print(directorio_padre+":")
    #ciclo para recorrer los objetos en la variable directorios y estos se guardan en la variable directorio_hijo
    for directorio_hijo in directorios:
        # Se imprime el doble guión y si esta en hijos entonces imprime doble
        print("--"*(nivel+1),end="")
        # Se concatena el directorio
        imprimir(directorio_hijo, directorios[directorio_hijo],nivel+1)

# Se define el metodo insertar que recibe la ubicación y el nombre de la nueva carpeta
def insertar(ubicacion, nueva_carpeta):
    # en la variable navegación se guarda lo que esta en diccionario de carpetas
    navegacion = diccionario_carpetas
    # Se divide lo que viene en la ubicación ejemplo padre/hijo/nieto y se guarda en un arreglo
    directorios = ubicacion.split("/")[1:]
    # Ciclo para recorrer los directorios y se guarda en la variable directorio
    for directorio in directorios:
        navegacion = navegacion[directorio]
    # Se define como un arreglo vacío
    navegacion[nueva_carpeta] = {}

for _ in range(cantidad_instrucciones):
    # Se cicla la cantidad de instrucciones
    instruccion, argumento = input().split(" ")
    # Se compara si es cd 
    if instruccion == "cd":
        #procesar instruccion cd
        if argumento == "..":
            #argumento regreso
            #borramos el ultimo directorio
            ubicacion_actual = "/".join(ubicacion_actual.split("/")[:-1])
        else:
            #ingresar a una carpeta
            ubicacion_actual = ubicacion_actual + "/" + argumento
    else:
        #procesar mkdir
        insertar(ubicacion_actual, argumento)
# Se llama la funcion imprimir con el diccionario de carpetas
imprimir("Mark", diccionario_carpetas["Mark"], 0)
