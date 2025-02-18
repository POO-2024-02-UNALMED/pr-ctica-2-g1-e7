from gestorAplicacion.gestion.Cliente import Cliente 
from gestorAplicacion.produccion.Fabrica import Fabrica
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.gestion.Operario import Operario
from gestorAplicacion.gestion.Factura import Factura
from gestorAplicacion.gestion.Vendedor import Vendedor
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria
from gestorAplicacion.produccion.EstadoProducto import EstadosProducto
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import time 

# 🔹 CREACIÓN DE OBJETOS NECESARIOS PARA LA FUNCIONALIDAD
p1=Producto("a",12,"dispo","venta","si",12)
p2=Producto("a",12,"dispo","venta","si",12)
p3=Producto("a",12,"dispo","venta","si",12)
p4=Producto("a",12,"dispo","venta","si",12)
p5=Producto("a",12,"dispo","venta","si",12)
p6=Producto("a",12,"dispo","venta","si",12)
p7=Producto("a",12,"dispo","venta","si",12)
p8=Producto("a",12,"dispo","venta","si",12)
p9=Producto("a",12,"dispo","venta","si",12)
p0=Producto("a",12,"dispo","venta","si",12)

listaProductos=[p1,p2,p3]
tienda=Tienda("tienda 1",Vendedor("juan",123,12,CuentaBancaria(124,1000000)),CuentaBancaria(12,100000),10,10,10)
tienda.__listaProducto=listaProductos
fabrica=Fabrica(1,"si","Av del rio",CuentaBancaria(12,100000),[p1,p2,p3,p4,p5,p6,p7,p8],[tienda],Operario("Juan",12,12,CuentaBancaria(2,2000),None))

factura=Factura(tienda,Cliente("Juan",12,1234,CuentaBancaria(12,1000)),"si",[p1,p2,p3,p4,p5,p6,p7,p8],20,datetime.now())

def devoluciones():
    """
    Implementa la funcionalidad de devoluciones en la consola.
    """
    while True:
        
        print("\nEligió la opción de devoluciones.")
        print("Seleccione la factura que desea consultar. Oprima 0 para salir.")
        print("0. Salir")

        # Mostrar las facturas disponibles
        for i, factura in enumerate(Factura.listaFacturas):
            print(f"{i+1}. Factura ID: {factura.id}, Cliente: {factura.cliente.getNombre()}")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue

        if opcion == 0:
            print("Saliendo del menú de devoluciones.")
            break

        if 1 <= opcion <= len(Factura.listaFacturas):
            factura:Factura = Factura.listaFacturas[opcion - 1]
            tienda = factura.tienda

            while True:
                print("\nSeleccione el producto que desea devolver o presione 0 para regresar al menú anterior:")
                
                # Mostrar los productos de la factura
                productosFactura=factura.mostrarProductosFactura()
                print(productosFactura)

                try:
                    opcion2 = int(input("Ingrese una opción: "))
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue

                if opcion2 == 0:
                    print("Regresando al menú de facturas.")
                    break

                if 1 <= opcion2 <= len(factura.listaProductos):
                    if factura.todosDevueltos():  
                        print("Todos los productos de esta factura ya han sido devueltos.")
                        break

                    producto = factura.listaProductos[opcion2 - 1]

                    if producto.estado ==EstadosProducto.DEVUELTO:
                        print("El producto ya ha sido devuelto, elija otro.")
                    else:
                        print(f"Eligió el producto: {producto.nombre}")
                        print("Indique el motivo de la devolución:")
                        
                        # Mostrar los motivos de devolución
                        print("\nMotivos de devolución:")
                        motivos = Producto.motivosDevolucion
                        for i, motivo in enumerate(motivos, 1):
                            print(f"{i}. {motivo}")
                        print(f"{len(motivos) + 1}. Otro (especificar)")

                        try:
                            motivoDevolucion = int(input("Ingrese una opción: "))
                        except ValueError:
                            print("Entrada inválida. Intente nuevamente.")
                            continue

                        if 1 <= motivoDevolucion <= len(motivos):
                            producto.motivo_devolucion = motivos[motivoDevolucion - 1]
                        elif motivoDevolucion == len(motivos) + 1:
                            motivo = input("Especifique su causa de la devolución: ")
                            producto.motivo_devolucion = motivo
                            Producto.motivosDevolucion.append(motivo)
                        else:
                            print("Motivo de devolución inválido. Intente nuevamente.")
                            continue

                        # Procesar reembolso si aplica
                        if motivoDevolucion in [1, 2, 3]:
                            print("Por el motivo indicado, se le hará el reembolso del dinero.")
                            cliente = tienda.devolverProducto(factura, producto)
                            valorADevolver = Fabrica.descontarDineroCuenta(producto)
                            Fabrica.cuentaBancaria.devolverDinero(valorADevolver, cliente)
                            cliente.removerProducto(producto)
                            print(f"Se le devolverá el valor de su producto: ${producto.precio}")
                            print("----Devolviendo el dinero...----")
                            time.sleep(2)
                            print("El producto ha sido devuelto exitosamente y se ha reembolsado su dinero.")

                        else:
                            print("Por el motivo indicado, se le hará el cambio del producto.")
                            print("Si el producto que seleccione tiene un precio menor, puede agregar otro para completar el valor restante.")
                            print("NO se le devolverá el dinero restante.")
                            print("Seleccione el producto por el cual desea cambiar:")

                            precio = producto.precio
                            seleccionProductos = []
                            carrito = []
                            subtotal = 0

                            productosDisponibles = tienda.mostrarProductos(producto)

                            while True:
                                if not productosDisponibles:
                                    print("Se han agotado los productos en la tienda disponibles para cambiar.")
                                    break

                                productosUnicos = []
                                frecuencias = []

                                for p in productosDisponibles:
                                    if p.nombre in [prod.nombre for prod in productosUnicos]:
                                        idx = [prod.nombre for prod in productosUnicos].index(p.nombre)
                                        frecuencias[idx] += 1
                                    else:
                                        productosUnicos.append(p)
                                        frecuencias.append(1)

                                for i, p in enumerate(productosUnicos):
                                    print(f"{i+1}. {p.nombre} - ${p.precio} - Cantidad disponible: {frecuencias[i]}")

                                try:
                                    opcion4 = int(input("Ingrese el número del producto a añadir (0 para finalizar): "))
                                except ValueError:
                                    print("Entrada inválida. Intente nuevamente.")
                                    continue

                                if opcion4 == 0:
                                    print("Ha decidido no añadir más productos.")
                                    break

                                seleccionProductos.append(opcion4)
                                productoSeleccionado = productosUnicos[opcion4 - 1]

                                carrito = tienda.agregarProductosParaCambio(precio, seleccionProductos, productosUnicos)

                                subtotal = sum(p.precio for p in carrito)
                                print("\nResumen del cambio:")
                                for p in carrito:
                                    print(f"- {p.nombre}: ${p.precio}")
                                print(f"Subtotal actual: ${subtotal}")

                                if subtotal > precio:
                                    break

                                continuar = int(input("¿Desea continuar añadiendo productos? (1: Sí, 0: No): "))
                                if continuar == 0:
                                    print("Proceso finalizado. Su carrito de cambio está listo.")
                                    break

                            excedente = Fabrica.calcularExcedente(carrito, precio)
                            if excedente > 0:
                                print(f"El excedente a pagar es de: ${excedente}")
                            else:
                                print("El total no supera el precio del producto original. No se devuelve dinero.")
                            cliente=factura.getCliente() 
                            cliente.getCuentaBancaria().transferirDinero(excedente, Fabrica.cuentaBancaria)
                            cliente.removerProducto(producto)
                            producto.estado = "DEVUELTO"

                            for p in carrito:
                                cliente.listaProductos.append(p)
                                tienda.listaProducto.remove(p)

                            print("Generando resumen final del cambio...")
                            time.sleep(2)
                            print("\n----- Resumen final del cambio -----")
                            print(f"Usted ha cambiado un {producto.nombre} por:")
                            for p in carrito:
                                print(f" - {p.nombre}: ${p.precio}")
                            print(f"Total del carrito: ${subtotal}\nExcedente pagado: ${excedente}")
                            print("---------------------------------------")
                            
                        break  # Finaliza la operación de devolución

                else:
                    print("Opción inválida. Intente nuevamente.")

        else:
            print("Opción inválida. Intente nuevamente.")

#🔹 Ejemplo de ejecución del método en la terminal:
devoluciones()
