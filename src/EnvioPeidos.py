import time

# Asumimos que existen clases y métodos similares a los de Java
# Cliente, Fabrica, Tienda, Producto, Conductor, TipoTransporte

def enviar_pedidos():
    while True:
        print("\nEligió la opción de envio de pedidos. \n\nSeleccione al cliente que realizó el pedido. Oprima 0 para salir.")
        print("\n0. Salir")
        print(mostrarCliente)#llamar el metodo mostrar clientes
        seleccion = -1
        
        # Selección de cliente
        while True:
            clienteSeleccionado = None
            confirmacionCliente = 0

            # Bucle para confirmar la selección del cliente
            while confirmacionCliente == 0:
                try:
                    seleccion = int(input("» "))
                    if seleccion == 0:  # Opción para salir
                        print("\nSaliendo...")
                        time.sleep(2)
                        return  # Salir del método
                    elif 0 < seleccion <= len(listaClientes):#llamar el metodo lista clientes
                        break  # Cliente seleccionado correctamente
                    else:
                        print("\nNúmero fuera de rango. Por favor, elija un cliente válido.")
                except ValueError:
                    print("\nEntrada inválida. Por favor, ingrese un número.")

                # Confirmación de cliente
                print(f"\nHa seleccionado el cliente: {listaClientes[seleccion - 1].getNombre()}")#llamar el metodo lista clientes
                print("\nPara confirmar, ingrese '1'. Para regresar al menú anterior, ingrese '0'.")

                while True:
                    eleccion = input("\n» ")
                    if eleccion == "1":  # Confirmar cliente
                        clienteSeleccionado = listaClientes[seleccion - 1]#llamar el metodo lista clientes
                        print(f"\nCliente confirmado: {clienteSeleccionado.getNombre()}")
                        confirmacionCliente = 1  # Confirmación de selección
                        break
                    elif eleccion == "0":  # Regresar al menú anterior
                        print("\nRegresando al menú anterior...")
                        time.sleep(2)
                        break
                    else:
                        print("\nPor favor, ingrese '1' para confirmar o '0' para volver al menú anterior.")
            break
        
        # Selección de tienda desde la cual se enviará el pedido
        print("\nSeleccione la tienda desde la cual se enviará el pedido. Si no desea continuar, presione 0 para salir.")
        print("\nListado de Tiendas:")
        print("0. Salir")
        print(mostrarTiendas(True))#llamar el metodo mostrarTiendas

        opcion = -1
        tiendaSeleccionada = None
        confirmacionTienda = 0

        # Bucle para confirmar la tienda seleccionada
        while confirmacionTienda == 0:
            try:
                opcion = int(input("\n» "))
                if opcion == 0:  # Opción para salir
                    print("\nSaliendo...")
                    time.sleep(2)
                    return
                elif 0 < opcion <= len(listaTienda): #llamar el atriburo listaTienda de la clase fabrica
                    tiendaSeleccionada = listaTienda[opcion - 1]#llamar el atriburo listaTienda de la clase fabrica
                    break  # Tienda seleccionada correctamente
                else:
                    print("\nNúmero fuera de rango. Por favor, elija una tienda válida.")
            except ValueError:
                print("\nEntrada inválida. Por favor, ingrese un número.")
            
            # Confirmación de tienda
            print(f"\nTienda Seleccionada: {tiendaSeleccionada.getNombre()}")
            print("\nPara confirmar la tienda seleccionada, ingrese '1'. Si desea cambiar su selección, ingrese '0'.")

            while True:
                eleccion = input("\n» ")
                if eleccion == "1":  # Confirmar tienda
                    print(f"\nTienda confirmada: {tiendaSeleccionada.getNombre()}")
                    confirmacionTienda = 1
                    break
                elif eleccion == "0":  # Regresar al menú anterior
                    print("\nRegresando al menú anterior...")
                    time.sleep(2)
                    break
                else:
                    print("\nLa opción ingresada no es válida. Por favor, ingrese '1' para confirmar o '0' para cambiar.")

        # Selección de la cantidad de productos a enviar
        print("\nIndique la cantidad de productos que desea enviar (máximo 5).")
        cantidadProductosSeleccionados = -1
        confirmacionCantidadProductos = 0
        while confirmacionCantidadProductos == 0:
            try:
                cantidadProductosSeleccionados = int(input("\n» "))
                if 0 < cantidadProductosSeleccionados <= 5:  # Validación de cantidad
                    print(f"\nHa ingresado que desea enviar {cantidadProductosSeleccionados} productos. Para confirmar, ingrese '1'. Si desea cambiar la cantidad, ingrese '0'.")
                    while True:
                        eleccion = input("\n» ")
                        if eleccion == "1":  # Confirmación de cantidad de productos
                            print(f"\nHa confirmado que desea enviar {cantidadProductosSeleccionados} productos.")
                            confirmacionCantidadProductos = 1
                            break
                        elif eleccion == "0":  # Volver a ingresar cantidad
                            print("\nPor favor, ingrese nuevamente la cantidad de productos que desea enviar.")
                            break
                        else:
                            print("\nLa opción ingresada no es válida. Por favor, ingrese '1' para confirmar o '0' para cambiarla.")
                else:
                    print("\nEl valor ingresado está fuera del rango permitido. Recuerde que el máximo de productos a enviar es 5.")
            except ValueError:
                print("\nEntrada inválida. Por favor, ingrese un número.")

        # Lista para almacenar los productos que el cliente ha seleccionado para su pedido
        listaProductosPedidos = []

        # Lista de productos de la tienda seleccionada
        listaProductosTienda = tiendaSeleccionada.listaProductosTienda()

        # Instrucción al cliente para seleccionar productos
        print("\nPor favor, seleccione los productos de manera individual. Si desea cancelar el envío, ingrese 0.")

        # Bucle para solicitar los productos uno por uno
        for i in range(cantidadProductosSeleccionados):
            if i != 0:
                print("\nPor favor, seleccione el siguiente producto para enviar.")
            while True:
                print("0. Salir")
                try:
                    # Mostrar la lista de productos disponibles
                    print(tiendaSeleccionada.mostrarListaProductosTienda(listaProductosTienda))
                    eleccion = int(input("\n» "))
                    
                    # Si el usuario elige salir, termina el proceso
                    if eleccion == 0:
                        print("\nSaliendo...")
                        time.sleep(2)
                        return
                    elif 0 < eleccion <= len(listaProductosTienda):
                        # Obtener el producto seleccionado y la cantidad disponible
                        productoSeleccionado = listaProductosTienda[eleccion - 1][0]
                        cantidadProducto = listaProductosTienda[eleccion - 1][1]

                        # Verificar si hay stock disponible
                        if cantidadProducto <= 0:
                            print("\nEl producto seleccionado ya no tiene stock disponible. Por favor, elija otro.")
                            continue  # Volver a pedir otro producto

                        print("\nPara confirmar, ingrese 1. Si desea volver a ingresar el producto, ingrese 0.")

                        while True:
                            confirmacionProductoSeleccionado = int(input("\n» "))
                            if confirmacionProductoSeleccionado == 1:
                                # Agregar el producto a la lista de pedidos y actualizar el stock
                                listaProductosPedidos.append(productoSeleccionado)
                                listaProductosTienda[eleccion - 1][1] -= 1

                                print(f"\nProducto agregado: {productoSeleccionado.getNombre()}")
                                time.sleep(0.5)
                                break
                            elif confirmacionProductoSeleccionado == 0:
                                break  # Permitir al usuario seleccionar otro producto
                            else:
                                print("\nPor favor, ingrese 1 para confirmar su selección o 0 para volver a ingresar el producto.")
                        break
                    else:
                        print("\nNúmero fuera de rango. Por favor, elija un producto válido.")
                except ValueError:
                    print("\nEntrada inválida. Por favor, ingrese un número.")


