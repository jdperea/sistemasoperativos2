cantidad_instrucciones = int(input())

diccionario_carpetas = {}
diccionario_carpetas["Mark"] = {}

ubicacion_actual = "/Mark"

def imprimir(directorio_padre, directorios, nivel):
    print(directorio_padre+":")
    for directorio_hijo in directorios:
        print("--"*(nivel+1),end="")
        imprimir(directorio_hijo, directorios[directorio_hijo],nivel+1)

def insertar(ubicacion, nueva_carpeta):
    navegacion = diccionario_carpetas

    directorios = ubicacion.split("/")[1:]

    for directorio in directorios:
        navegacion = navegacion[directorio]

    navegacion[nueva_carpeta] = {}

for _ in range(cantidad_instrucciones):
    instruccion, argumento = input().split(" ")

    if instruccion == "cd":
        #procesar instruccion cd
        if argumento == "..":
            #argumento regreso
            #borramos el ultimo directorio
            ubicacion_actual = "/".join(ubicacion_actual.split("/")[:-1])
        else:
            #ingresar a una carpeta
            #in
            ubicacion_actual = ubicacion_actual + "/" + argumento
    else:
        #procesar mkdir
        insertar(ubicacion_actual, argumento)

imprimir("Mark", diccionario_carpetas["Mark"], 0)