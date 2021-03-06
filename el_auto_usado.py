#import datetime
from pathlib import Path
import productos
import vendedores
import ventas

lista_productos = []

lista_vendedores = [
    ["1", "2", "3"],                                   #Vendedor ID
    ['juan perez', 'mariana lopez', 'pedro gonzalez']  #Nombre
]

lista_ventas = [
    ["1", "1", "2", "3"],                                  #Vendedor ID
    ["1", "2", "3", "5"],                                  #Producto ID
    ["01/01/2019","16/03/2019","21/09/2019","05/01/2020"], #Fecha
    ["1", "2", "2", "1"],                                  #Cantidad
    ["50000", "120000", "60000", "70000"]                  #Total
]

# print_matriz
# matriz: la matriz que quieres desplegar en la terminal
# nombre_columnas: una lista con los nombres de cada columna de la matriz
def print_matriz(matriz, nombre_columnas):
    bigger_size = []
    for nombre in nombre_columnas:
        bigger_size.append(len(nombre))
    
    for idx, fila in enumerate(matriz):
        for element in fila:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))

    for i in range(len(nombre_columnas)):
        print(nombre_columnas[i].center(bigger_size[i] + 2), end = "")
    print()
    
    for i in range(len(matriz[0])):
        for j in range(len(nombre_columnas)):
            print(str(matriz[j][i]).title().center(bigger_size[j] + 2), end = "")
        print()

# buscar_elemento
# matriz: la tabla en la que deseas buscar
# columna: la columna de la tabla en la que deseas buscar
# valor: el valor que deseas buscar
# return: el indice del valor en la tabla o -1 si no esta
#              lista_vendedores, 1, mariana lopez
def buscar_elemento(matriz, columna, valor):
    if valor in matriz[columna]:
        return matriz[columna].index(valor)
    else:
        return -1

# obtener_id
# matriz: la tabla en la que deseas encontrar el identificador
# indice: el indice del elemento del que deseas encontrar el identificador o -1 si el indice es incorrecto
def obtener_id(matriz, indice):
    if indice < len(matriz[0]) and indice >= -len(matriz[0]):
        return matriz[0][indice]
    else:
        return -1

# obtener_precio
# matriz: la tabla en la que deseas encontrar el precio
# indice: el indice del elemento del que deseas encontrar el precio o -1 si el indice es incorrecto
def obtener_precio(matriz, indice):
    if indice < len(matriz[productos.PRECIO]) and indice >= -len(matriz[productos.PRECIO]):
        return matriz[productos.PRECIO][indice]
    else:
        return -1

# Abrir el archivo de productos, leer su informacion y carga la informacion en lista_productos
def cargarProductos():
    ruta_productos = Path('archivos', 'productos.csv')
    archivo_productos = open(ruta_productos)
    content_productos = archivo_productos.readlines()
    for line in content_productos:
        lista_productos.append(line.strip().split(','))
    archivo_productos.close()

#Abrir el archivo de producto y guarda en el la informacion que hay en lista_productos
def guardarProductos():
    string_content = ""
    for lines in lista_productos:
        for idx, element in enumerate(lines):
            if idx == len(lines) - 1:
                string_content += element + "\n"
            else:
                string_content += element + ","

    string_content = string_content.strip()
    ruta_productos = Path('archivos', 'productos.csv')
    archivo_productos = open(ruta_productos, "w")
    archivo_productos.write(string_content)
    archivo_productos.close()

def menu():
    print()
    print("  Elija una de las siguientes opciones:")
    print("    1. Registrar ventas")
    print("    2. Registrar art??culos")
    print("    3. Consultar inventario")
    print("    4. Consultar ventas")
    print("    5. Reporte de ventas por vendedor")
    print("    6. Reporte de ventas por art??culo")
    print("    0. Guardar y salir")
    return int(input(">> "))

def registrar_venta():
    print("Registra venta")

def registar_articulo():
    print("Registra art??culo")

def consultar_inventario():
    print("Consulta inventario")

def consultar_ventas():
    print("Consulta venta")

def reporte_ventas_vendedor():
    print("Genera reporte")

def reporte_ventas_articulo():
    print("Genera reporte")

def main():

    print("-" * 30)
    print("| Bienvenido a El Auto Usado |")
    print("-" * 30)

    cargarProductos()

    while True:
        selected = menu()
        if selected == 0:
            guardarProductos()
            print("Gracias por su visita")
            break
        elif selected == 1:
            registrar_venta()
        elif selected == 2:
            registar_articulo()
        elif selected == 3:
            consultar_inventario()
        elif selected == 4:
            consultar_ventas()
        elif selected == 5:
            reporte_ventas_vendedor()
        elif selected == 6:
            reporte_ventas_articulo()
        else:
            print(f"La opci??n {selected} no es v??lida")

main()