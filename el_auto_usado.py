import datetime
import productos
import vendedores
import ventas

def print_matriz(matriz, nombre):
    bigger_size = []
    columnas_matriz = []
    
    if nombre == 'productos':
        columnas_matriz = productos.COLUMNAS
        for i in productos.COLUMNAS:
            bigger_size.append(len(i))
    elif nombre == 'vendedores':
        columnas_matriz = vendedores.COLUMNAS
        for i in vendedores.COLUMNAS:
            bigger_size.append(len(i))
    elif nombre == 'ventas':
        columnas_matriz = ventas.COLUMNAS
        for i in ventas.COLUMNAS:
            bigger_size.append(len(i))
    
    for idx, columnas in enumerate(matriz):
        for element in columnas:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))
        
    
    for idx, nombre_columna in enumerate(columnas_matriz):
        print(nombre_columna.center(bigger_size[idx] + 2), end = "")
    print()

    for i in range(len(matriz[0])): #0 - 4
        for j in range(len(columnas_matriz)): #0 - 5
            print(str(matriz[j][i]).center(bigger_size[j] + 2), end = "")
        print()

def main():

    lista_productos = [
        [1, 2, 3, 4, 5],                                  #Producto ID
        ['Ford', 'Chevrolet', 'Honda', 'Toyota', 'VW'],   #Marca
        ['Mustang', 'Camaro', 'Civic', 'Prius', 'Jetta'], #Sub Marca
        [2005, 2006, 2004, 2010, 2012],                   #Modelo
        [50000, 60000, 30000, 60000, 70000],              #Precio
        [2, 1, 0, 3, 2]                                   #Existencia
    ]

    lista_vendedores = [
        [1, 2, 3],                     #Vendedor ID
        ['Juan', 'Mariana', 'Pedro'],  #Nombre
        ['Perez', 'Lopez', 'Gonzalez'] #Apellido 
    ]

    lista_ventas = [
        [1, 1, 2, 3],                                          #Vendedor ID
        [1, 2, 3, 5],                                          #Producto ID
        ["01/01/2019","16/03/2019","21/09/2019","05/01/2020"], #Fecha
        [1, 2, 2, 1],                                          #Cantidad
        [50000, 120000, 60000, 70000],                         #Total
    ]

    print("*" * 100)
    print_matriz(lista_productos, 'productos')
    print("*" * 100)
    print_matriz(lista_vendedores, 'vendedores')
    print("*" * 100)
    print_matriz(lista_ventas, 'ventas')
    print("*" * 100)

main()