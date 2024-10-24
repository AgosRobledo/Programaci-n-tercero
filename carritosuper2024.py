import os
import decimal
import re
salir=False
datos=0
cod=0
total=0
cantidad=0
producto_carro=0
carrito={}
productos={}

productos= {
    "001" : {
        "código" : "001",
        "nombre" : "Iphone 13 mini",
        "marca": "Apple",
        "color": "Verde Alpino ",
        "precio": 700000.50,
        "stock": 100,
        "pantalla": "5.4 pulgadas ",
        "almacenamiento": "256 GB",

    },
    "002" : {
        "código" : "002",
        "nombre" : "Iphone 14 plus ",
        "marca": "Apple ",
        "color": "Azul",
        "precio": 720000.50,
        "stock": 120,
        "pantalla": "6.7 pulgadas ",
        "almacenamiento": "512 GB ",
    },
    "003" : {
        "código" : "003",
        "nombre" : "Samsung Galaxy S2 2",
        "marca": "Samsung ",
        "color": "Blanco",
        "precio": 300000.50,
        "stock": 100,
        "pantalla": "6.1 pulgadas ",
        "almacenamiento": "256 GB",

    },
    "004" : {
        "código" : "004",
        "nombre" : "Samsung Galaxy A24 ",
        "marca": "Samsung ",
        "color": "Verde Lima ",
        "precio": 230000.50,
        "stock": 250,
        "pantalla": "6.5 pulgadas ",
        "almacenamiento": "128 GB ",

    },
    "005" : {
        "código" : "005",
        "nombre" : "Xiaomi 13T Pro ",
        "marca": "Xiaomi ",
        "color": "Azul Claro ",
        "precio": 120000.50,
        "stock": 330,
        "pantalla": " 6.67 pulgadas ",
        "almacenamiento": "256 GB",

},
    "006" : {
        "código" : "006",
        "nombre" : "Xiaomi 13 Ultra ",
        "marca": "Xiaomi ",
        "color": "Verde Oliva ",
        "precio": 200000.50,
        "stock": 300,
        "pantalla": " 6.73 pulgadas ",
        "almacenamiento": "256 GB",

    },
}
carrito={}
precio_envio= 1000.00

def mostrar_productos(productos):
    print ("Los productos que ofrecemos son: ")
    for key, value in productos.items():
        print()
        print("Código:", productos[key]["código"])
        print("Nombre:", productos[key]["nombre"])
        print("Marca:", productos[key]["marca"])
        print("Color:", productos[key]["color"])
        print("Precio: $", productos[key]["precio"])
        print("Stock:", productos[key]["stock"])
        print("Pantalla:", productos[key]["pantalla"])
        print("Almacenamiento:", productos[key]["almacenamiento"])
        print()

def mostrar_productos_breve(productos):
    print ("Información breve: ")
    for key, value in productos.items():
        
        print("Código:", productos[key]["código"])
        print("Nombre:", productos[key]["nombre"])
        print("Precio: $", productos[key]["precio"])
        print("Stock:", productos[key]["stock"])
        print()

def buscarProducto(cod, productos):
    while(True):
        for key, value in productos.items():

            if cod==key:
                
                print("")
                print ("Producto encontrado:")
                print("Nombre:", productos[key]["nombre"])
                print("Marca:", productos[key]["marca"])
                print("Precio: $", productos[key]["precio"])
                print("Stock:", productos[key]["stock"])
                print("Pantalla:", productos[key]["pantalla"])
                print("Almacenamiento:", productos[key]["almacenamiento"])
                print("")

                return
        cod = input("El producto que desea buscar no existe, vuelva a introducir otro código: ")

def validar_opcion(opcion):
    while(True):
        if opcion.isnumeric():
            opcion =int(opcion)
            if opcion<5 and opcion>0:
                return opcion
            else:
                opcion= input("La opción ingresada no es correcta, vuelva a ingresar otra opción: ")   
        else:
            opcion= input("La opción ingresada no es un número, vuelva a ingresar otra opción: ")

def agregar_al_carrito(carrito):
        cod=input("Ingrese el código del producto que desea añadir a su carrito: ")
        if cod in productos:       
            producto=productos[cod]
            cantidad=int(input("Ingrese la cantidad que desea de este producto: "))
            if 0 < cantidad <= producto["stock"]:
                if cod in carrito:
                    carrito[cod]["cantidad"]+= cantidad
                    carrito[cod]["costo_total"] += cantidad * producto["precio"]
                else:
                    carrito[cod]={
                        "nombre" : producto["nombre"],
                        "cantidad" : cantidad,
                        "precio_unitario" : producto["precio"],
                        "costo_total" : cantidad * producto["precio"]
                    }
                producto["stock"] -= cantidad
                print("Producto agregado al carrito ")
            else: 
                print("La cantidad que usted solicita no esta disponible ")
        else:
            print("No se encontró un producto con ese código ")

#funcion para mostrar el carrito armado por los clientes
def ver_carrito():
    if len(carrito)>0:
        print("Productos de  tu carrito: ")
        total=0
        for código, producto in carrito.items():
            nombre_producto= producto ["nombre"]
            cantidad=producto ["cantidad"]
            precio_unitario= producto ["precio_unitario"] 
            costo_total = producto ["costo_total"]
            print("")
            print("-"*25)
            print("Código del Producto:", código)
            print("Nombre del Producto:", nombre_producto)
            print("Cantidad: ", cantidad )
            print("Precio Unitario: $", precio_unitario)
            print("Costo Total: $", costo_total)
            print("-"*25)
            total += costo_total

        print("Costo de Envío: $", precio_envio)
        total_con_envio = total + precio_envio
        print("El costo total de su compra es: $", total_con_envio)
        modificar_carrito()
    else:
        print("Su carrito se encuentra vacio") 


def pedir_direccion():
    print("Por favor, ingrese los siguientes datos para el envío:")

    nombre = validar_nombre()
    calle = validar_calle()
    ciudad = validar_ciudad()
    codigo_postal = validar_codigo_postal()
    provincia = validar_provincia()
    pais = validar_pais()

    print("\nResumen de la dirección:")
    print(f"Nombre: {nombre}")
    print(f"Dirección: {calle}, {ciudad}, {provincia}, {pais}")
    print(f"Código Postal: {codigo_postal}")

    confirmar = validar_opcion_1_2("""
¿Está bien la información de la dirección? 
1) SI
2) NO 
    """)
    if confirmar == '1':
        print("¡Sus datos se guardaron correctamente! ")
        #poner aqui el metodo de pago
        os.system("cls")
        elegir_medio_pago()
    elif confirmar == '2':        
        os.system("cls")
        print("Volvamos a ingresar los datos.")
        return pedir_direccion()
    else:
        print ("Opción inválida")



# Funciones de validación
def validar_nombre():
    while True:
        nombre = input("Nombre completo: ")
        if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$", nombre):
            return nombre.title()
        print("Error: El nombre solo puede contener letras.")

def validar_calle():
    while True:
        calle = input("Calle y número: ")
        if re.match("^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]+$", calle):
            return calle.capitalize()
        print("Error: La dirección debe contener solo letras y números.")

def validar_ciudad():
    while True:
        ciudad = input("Ciudad: ").strip()
        if all(palabra.isalpha() for palabra in ciudad.split()):
            return ciudad.title()  # Capitaliza cada palabra
        print("Ingreso inválido, vuelva a intentarlo.")

def validar_codigo_postal():
    while True:
        codigo_postal = input("Código postal: ")
        if re.match("^\d{4}$", codigo_postal):
            return codigo_postal
        print("Error: El código postal debe ser de 4 dígitos.")

def validar_provincia():
    while True:
        provincia = input("Provincia: ")
        if provincia.isalpha():
            return provincia.capitalize()
        print("Error: La provincia solo puede contener letras.")

def validar_pais():
    while True:
        pais = input("País: ")
        if pais.isalpha():
            return pais.capitalize()
        print("Error: El país solo puede contener letras.")

def elegir_medio_pago():
    print("""
Seleccione el medio de pago:
1) Efectivo
2) Tarjeta
    """)
    while True:
        opcion = input("Ingrese el número de la opción elegida: ").strip()
        if opcion == "1":
            os.system("cls")
            print("Muchas gracias por su compra, el pago se realizará en efectivo cuando le entreguen el pedido ")
            carrito.clear()
            return "Efectivo"
        elif opcion == "2":
            procesar_pago_tarjeta()
            return "Tarjeta"
        else:
            print("Opción inválida. Intente nuevamente.")

def procesar_pago_tarjeta():
    while True:  # Bucle para repetir el proceso si el usuario dice "n"
        print("\n--- Pago con Tarjeta ---")

        # Validación del nombre del titular
        while True:
            nombre_titular = input("Ingrese el nombre del titular de la tarjeta: ").strip()
            if nombre_titular:  # Asegurarse de que no esté vacío
                nombre_titular = nombre_titular.title()  # Formatear con mayúsculas al inicio
                break
            else:
                print("Error: El nombre no puede estar vacío. Por favor, ingrese un nombre válido.")

        # Validación del número de tarjeta
        while True:
            numero_tarjeta = input("Ingrese el número de la tarjeta (16 dígitos): ").strip()
            if numero_tarjeta.isdigit() and len(numero_tarjeta) == 16:
                break
            else:
                print("Error: Debe ingresar un número de tarjeta válido (16 dígitos).")

        # Validación de la fecha de vencimiento
        while True:
            fecha_vencimiento = input("Ingrese la fecha de vencimiento (MM/AA): ").strip()
            if re.match(r'^\d{2}/\d{2}$', fecha_vencimiento):  # Formato MM/AA
                break
            else:
                print("Error: Debe ingresar una fecha válida en el formato MM/AA.")

        # Validación del CVV
        while True:
            cvv = input("Ingrese el CVV (3 dígitos): ").strip()
            if cvv.isdigit() and len(cvv) == 3:
                break
            else:
                print("Error: Debe ingresar un CVV válido (3 dígitos).")

        print("\nInformación ingresada:")
        print(f"Nombre del titular: {nombre_titular}")
        print(f"Número de tarjeta: {numero_tarjeta}")
        print(f"Fecha de vencimiento: {fecha_vencimiento}")
        print(f"CVV: {cvv}")

        confirmar = validar_opcion_1_2("""
¿Está bien la información de la tarjeta? 
1) SI
2) NO 
    """)
        if confirmar == '1':
            os.system("cls")
            print("Pago exitoso. Gracias por su compra.")
            carrito.clear()
            break 
        else:
            print("Volvamos a ingresar los datos de la tarjeta.")
            
def validar_opcion_1_2(pregunta):
    while True:
        opcion = input(pregunta).strip()
        if opcion in ['1', '2']:
            return opcion
        else:
            print("Opción inválida. Por favor, ingrese '1' o '2'.")

def resumen_final(direccion, medio_pago):
    print("\n--- Resumen de la Compra ---")
    ver_carrito()  # Mostrar los productos en el carrito
    print("Dirección de Envío:")
    print(f"{direccion['nombre']}, {direccion['calle']}, {direccion['ciudad']}, {direccion['provincia']}, {direccion['pais']}")
    print(f"Código Postal: {direccion['codigo_postal']}")
    print(f"Método de Pago: {medio_pago}")
    print("\n¡Gracias por su compra!")

def validar_confirmar_compra():
    while True:
        opcion = input("""
¿Desea seguir con la compra? (Ingrese números no letras)
1) Sí
2) No
""").strip()
        if opcion.isdigit() and opcion in ['1', '2']:
            return int(opcion)
        else:
            print("ERROR: Ingreso inválido. Intenta de nuevo.")

def elegir_medio_pago():
    print("""
Seleccione el medio de pago:
1) Efectivo
2) Tarjeta
    """)
    while True:
        opcion = input("Ingrese el número de la opción elegida: ").strip()
        if opcion == "1":
            os.system("cls")
            print("Muchas gracias por su compra, el pago se realizará en efectivo cuando le entreguen el pedido ")
            carrito.clear()
            return "Efectivo"
        elif opcion == "2":
            procesar_pago_tarjeta()
            return "Tarjeta"
        else:
            print("Opción inválida. Intente nuevamente.")


def modificar_carrito():
    print("""
¿Desea modificar el carrito? (Ingrese números, no letras)
1) Si
2) No
    """)
    opcion1=validar_opciones_modificar_carrito(input("Ingrese la opción: "))
    if opcion1==1:
        print (""" 
1) Aumentar cantidad
2) Disminuir cantidad/Eliminar producto
3) Agregar un nuevo producto al carrito
    """)
        opcion2=int(input("Ingrese el número de la acción que desea realizar: "))

        if opcion2 == 1:  # Modificar cantidad
            código = input("Ingrese el código del producto que quiere modificar: ")

            if código in carrito:
                producto_carrito = carrito[código]
                stock_inicial = productos[código]["stock"] + producto_carrito["cantidad"]
                cantidad_actual = producto_carrito["cantidad"]

                # Calcular el stock disponible a partir del stock inicial y la cantidad en el carrito
                stock_disponible = stock_inicial - cantidad_actual
                print(f"Stock disponible para agregar: {stock_disponible} unidades")

                nueva_cantidad = int(input("Ingrese cuántas unidades más desea agregar: "))

                if nueva_cantidad > stock_disponible:
                    print(f"No puede agregar más de {stock_disponible} unidades.")
                elif nueva_cantidad > 0:
                    # Actualizamos la cantidad en el carrito y el stock disponible
                    producto_carrito["cantidad"] += nueva_cantidad
                    producto_carrito["costo_total"] = producto_carrito["precio_unitario"] * producto_carrito["cantidad"]
                    productos[código]["stock"] -= nueva_cantidad

                    print(f"Cantidad actualizada correctamente. Ahora tiene {producto_carrito['cantidad']} unidades en el carrito.")
                else:
                    print("Debe ingresar una cantidad mayor a 0.")
            else:
                print("El producto no existe en el carrito.")

        elif opcion2 == 2:  # Eliminar producto
            while True:
                código = input("Ingrese el código del producto que desea eliminar: ")
                if código in carrito:
                    cantidad_a_eliminar = int(input(f"Ingrese cuántas unidades desea eliminar del producto {carrito[código]['nombre']}: "))
                    if cantidad_a_eliminar > 0 and cantidad_a_eliminar <= carrito[código]["cantidad"]:
                        productos[código]["stock"] += cantidad_a_eliminar
                        carrito[código]["cantidad"] -= cantidad_a_eliminar
                        carrito[código]["costo_total"] = carrito[código]["precio_unitario"] * carrito[código]["cantidad"]

                        # Si la cantidad llega a 0, eliminar el producto del carrito
                        if carrito[código]["cantidad"] == 0:
                            producto_nombre = carrito[código]["nombre"]  # Guardamos el nombre antes de eliminar
                            del carrito[código]
                            print(f"El producto {producto_nombre} fue eliminado del carrito porque la cantidad llegó a 0.")
                        else:
                            print(f"{cantidad_a_eliminar} unidades de {carrito[código]['nombre']} fueron eliminadas del carrito.")
                        break  # Salimos del bucle después de eliminar
                    else:
                        print("Cantidad inválida. Debe ser mayor que 0 y no mayor que la cantidad en el carrito.")
                else:
                    print("El producto no se encuentra en el carrito. Ingrese otro código.")
                
        elif opcion2 == 3:
            agregar_al_carrito(carrito)
        else:
            print("Opción inválida.")
                
    elif opcion1==2:
        confirmarcompra = validar_confirmar_compra()
        
        if confirmarcompra == 1:
            os.system("cls")
            pedir_direccion()
        else:
            cancelar_compra()
    else:
        print("Su respuesta es inválida ")


def cancelar_compra():
    opcion_cancelar = input("""
¿Desea cancelar la compra? 
1) Si
2) No
""").strip().lower()
    if opcion_cancelar == "1":
        # Restaurar stock de los productos en el carrito
        for codigo, producto in carrito.items():
            productos[codigo]["stock"] += producto["cantidad"]
        carrito.clear()
        print("Compra cancelada. El carrito ha sido vaciado y el stock restaurado.")
    elif opcion_cancelar == "2":
        input("Presione ENTER para seguir.")
    else:
        print("Opción inválida. Intente nuevamente.")
        cancelar_compra()  # Volver a preguntar si ingresó una opción inválida.

def validar_opciones_modificar_carrito(opcion1):
    while(True):
        if opcion1.isnumeric():
            opcion1 =int(opcion1)
            if opcion1==1 or opcion1==2:
                return opcion1
            else:
                opcion1= input("La opción ingresada no es correcta, vuelva a ingresar otra opción: ")   
        else:
            opcion1= input("La opción ingresada no es un número, vuelva a ingresar otra opción: ")

while (salir==False):
    print (""" 
Bienvenido a tienda "TechMarket":
    1) Mostrar lista de productos
    2) Ver producto por código
    3) Agregar al carrito 
    4) Ver carrito
    """)
    
    opcion= validar_opcion(input("Ingrese una opción: "))
    
    if opcion == 1:
        os.system("cls")
        print()
        mostrar_productos(productos)
    if opcion ==2:
        buscarProducto(input("Ingrese el código del producto a buscar: "),productos)
        #asi llamo una función
        continuar = input("Ingrese ENTER para continuar")
        os.system("cls")
    #agregar productos a al diccionario carrito
    if opcion == 3: #agregar productos al carrito
        agregar_al_carrito(carrito)
        continuar = input("Ingrese ENTER para continuar")
        os.system("cls")
    if opcion==4:#realizar la compra si es que hay productos en el carrito
        ver_carrito()
        print("")
        continuar = input("Ingrese ENTER para continuar")
        os.system("cls")
        print("")
