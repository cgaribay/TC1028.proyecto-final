#import datetime
import productos
import vendedores
import ventas

def print_matriz(matriz, nombre_columnas):
    bigger_size = []
    for nombre in nombre_columnas:
        bigger_size.append(len(nombre))
    
    for idx, columnas in enumerate(matriz):
        for element in columnas:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))

    for i in range(len(matriz[0])):
        for j in range(len(nombre_columnas)):
            print(str(matriz[j][i]).center(bigger_size[j] + 2), end = "")
        print()

def menu():
    print()
    print("  Elija una de las siguientes opciones:")
    print("    1. Registrar ventas")
    print("    2. Registrar artículos")
    print("    3. Consultar inventario")
    print("    4. Consultar ventas")
    print("    5. Reporte de ventas por vendedor")
    print("    6. Reporte de ventas por artículo")
    print("    0. Guardar y salir")
    return int(input(">> "))

def registrar_venta():
    print("Registra venta")

def registar_articulo():
    print("Registra artículo")

def consultar_inventario():
    print("Consulta inventario")

def consultar_ventas():
    print("Consulta venta")

def reporte_ventas_vendedor():
    print("Genera reporte")

def reporte_ventas_articulo():
    print("Genera reporte")

def main():

    lista_productos = [
        [1, 2, 3, 4, 5],                                                    #Producto ID
        ['Ford', 'Chevrolet', 'Honda', 'Toyota', 'VW'],                     #Marca
        ['Mustang', 'Camaro', 'Civic', 'Prius', 'Jetta'],                   #Sub Marca
        [2005, 2006, 2004, 2010, 2012],                                     #Modelo
        [50000, 60000, 30000, 60000, 70000],                                #Precio
        [2, 1, 0, 3, 2],                                                    #Existencia
        ["06/01/2020","06/01/2020","06/01/2020","06/01/2020", "06/01/2020"] #Fecha resurtido
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
        [50000, 120000, 60000, 70000]                          #Total
    ]

    print("-" * 30)
    print("| Bienvenido a El Auto Usado |")
    print("-" * 30)

    while True:
        selected = menu()
        if selected == 0:
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
            print(f"La opción {selected} no es válida")

main()