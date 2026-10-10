

# # Lista de productos como ejemplo
# productos = [
#     ["Mouse Gamer", "Periféricos", 45],     
#     ["Teclado Mecánico", "Periféricos", 120], 
#     ["Monitor 24 pulgadas", "Pantallas", 250],
#     ["Auriculares Bluetooth", "Audio", 85],   
#     ["Memoria RAM 16GB", "Componentes", 60] 
# ]

productos = []

while True:
    print("\n")
    print("="*40) # <-  ==================================
    print("Sistema de getion de productos") 
    print("="*40) # <-  ==================================
    print("1. Agregar productos")
    print("2. Mostrar productos")        
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Elegi una opción (1-5): ").strip()

    if opcion == "1":
        
        print("\n--- Agregar producto ---\n")
        # validaciones de los datos agregados

        nombre = input("Nombre del producto: ").strip()
        while nombre == "":
            print("Error: el nombre no puede estar vacio.")
            nombre = input("Nombre del producto: ").strip()

        categoria = input("Categoria del producto: ").strip()
        while categoria == "":
            print("Error: la categoria no puede estar vacia.")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Error: ingresa solo numeros positivos.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre,categoria,precio]
        productos.append(datos)

        print(f"lista de productos {productos}")
        print(f"len() {len(productos)}")
        print(f"rangue(len())    {range(len(productos))}")

    elif opcion == "2":  
        print("\n--- lista de productos ---\n") 

        if not any(productos):
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")

    elif opcion == "3":
        print("\n--- Buscar producto ---\n")

        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()

            while busqueda == "":
                print("Error: escribi algo para buscar")
                busqueda = input("Nombre del producto a buscar: ").strip().lower()

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print("No se encontra ningun resultado.")
            else:
                print(f"Productos encontrados {encontrado}")


    elif opcion == "4":
        print("\n--- Eliminar producto ---\n")
        if len(productos) == 0:
            print("Todavia no hay productos cargados.")
        else:
            for i in range(len(productos)):
                print(f"{i+1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}") 

            while True:
                id_elminar = input("Numero de producto a elminar: ").strip()

                while not id_elminar.isdigit(): # verifico que el dato ingresado sean numeros
                    print("Error: ingresa un numero")
                    id_elminar = input("Numero de producto a elminar: ").strip()

                seleccion = int(id_elminar) # convierto a entero el dato ingresado

                if 1 <= seleccion <= len(productos): # corroboro que el numero ingresado este dentro de la lista
                    indice_real = seleccion - 1
                    prod_borrado = productos.pop(indice_real)
                    print(f"se elimino el producto: {prod_borrado[0]} ")
                    break
                else:
                    print("Error: eliga un numero de la lista")
                
        

    elif opcion == "5":
        print("\n¡Gracias por usar nuestro sistema!\n")
        break

    else:
        print("Opcion no valida. tenes que elegir entre (1-5)")