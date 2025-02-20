import time
from gestorAplicacion.produccion.Fabrica import Fabrica  # Importar la clase Fabrica
from gestorAplicacion.produccion.Tienda import Tienda    # Importar la clase Tienda
from gestorAplicacion.produccion.Producto import Producto  # Importar la clase Producto
from gestorAplicacion.produccion.TipoTransporte import TipoTransporte  # Importar la clase TipoTransporte
from gestorAplicacion.produccion.Transporte import Transporte  # Importar la clase Transporte
from gestorAplicacion.gestion.Conductor import Conductor  # Importar la clase Conductor
from gestorAplicacion.gestion.Vendedor import Vendedor #prueba
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria#prueba

cuentaBancaria2=CuentaBancaria(1002 , 10002)

mi_vendedor2 = Vendedor("Juan Pablo", 1037121919, 20, cuentaBancaria2)

producto10 = Producto("Laptop", 1200, "Tecnología", 2.5)
producto11 = Producto("Teléfono", 800, "Tecnología", 0.3)
producto12 = Producto("Tablet", 500, "Tecnología", 0.6)
producto13= Producto("Impresora", 200, "Oficina", 5.0)
producto14 = Producto("Monitor", 300,  "Tecnología", 4.0)

mi_tienda2 = Tienda(
    nombre="Supermercado La Estrella",
    vendedor=mi_vendedor2,
    cuentaBancaria="9876543210",
    capacidadMaximaMaterial=100,
    capacidadMaximaConsumible=200,
    capacidadMaximaLimpieza=150
)

Fabrica.listaTienda.append(mi_tienda2)
    
def main():
    salir = False
    
    while not salir:
        print("========================================")
        print("¡Bienvenido a la opción de abastecer tienda!")
        print("Seleccione la tienda que desea abastecer (0 para salir):")
        print("========================================")
        print("0. Salir")
        print(Fabrica.mostrarTiendas())
        print("========================================")

        tiendaSeleccionadaIndex = None
        tiendaSeleccionada = None

        while True:
            try:
                tiendaSeleccionadaIndex = int(input("» "))
                
                if tiendaSeleccionadaIndex == 0:
                    time.sleep(1)
                    print("Saliendo...")
                    return

                if 1 <= tiendaSeleccionadaIndex <= len(Fabrica.listaTienda):
                    break  # Número válido, salir del bucle
                else:
                    print(f"Número inválido. Ingrese un número entre 1 y {len(Fabrica.listaTienda)}.")
            
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        confirmacionTienda = False
        while not confirmacionTienda:
            tiendaSeleccionada = Fabrica.listaTienda[tiendaSeleccionadaIndex - 1]
            print(f"Tienda seleccionada: {tiendaSeleccionada.getNombre()}")
            print("¿Es correcta esta selección? (1 para sí, 2 para no)")
            print("1. Sí, proceder")
            print("2. No, seleccionar otra tienda")

            try:
                confirmacion = int(input("» "))
                if confirmacion == 1:
                    print("Procediendo con la tienda seleccionada...")
                    confirmacionTienda = True
                elif confirmacion == 2:
                    print("========================================")
                    print("Seleccione la tienda que desea abastecer (0 para salir):")
                    print("========================================")
                    print("0. Salir")
                    print(Fabrica.mostrarTiendas())
                    print("========================================")

                    while True:
                        try:
                            tiendaSeleccionadaIndex = int(input("» "))

                            if tiendaSeleccionadaIndex == 0:
                                time.sleep(1)
                                print("Saliendo...")
                                return

                            if 1 <= tiendaSeleccionadaIndex <= len(Fabrica.getListaTienda()):
                                break  # Número válido, salir del bucle
                            else:
                                print(f"Número inválido. Ingrese un número entre 1 y {len(Fabrica.getListaTienda())}.")
                        
                        except ValueError:
                            print("Entrada inválida. Por favor, ingrese un número.")

            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        print("========================================")
        print("Productos por categoría en la tienda seleccionada:")
        print(tiendaSeleccionada.productosPorCategoria(tiendaSeleccionada.getListaProducto()))

        productosGenerados = []
        conteoCategoriasTemporal = [
            tiendaSeleccionada.getCantidadActualPorCategoria("Herramientas"),
            tiendaSeleccionada.getCantidadActualPorCategoria("Muebles"),
            tiendaSeleccionada.getCantidadActualPorCategoria("Aseo")
        ]
        pesoTotalProductos = 0.0

        while True:
            print("========================================")
            print("Seleccione el producto que desea enviar a la tienda (0 para salir):")
            print("========================================")
            print("0. Salir")
            print(Fabrica.mostrarProductos())
            print("========================================")
            productoSeleccionadoIndex = -1
            productoSeleccionado = None

            while productoSeleccionadoIndex < 0 or productoSeleccionadoIndex > len(Fabrica.getProductosDisponibles()):
                try:
                    productoSeleccionadoIndex = int(input("» "))
                    if productoSeleccionadoIndex == 0:
                        time.sleep(1)
                        print("Saliendo...")
                        return
                    if productoSeleccionadoIndex < 1 or productoSeleccionadoIndex > len(Fabrica.getProductosDisponibles()):
                        print(f"Número inválido. Ingrese un número entre 1 y {len(Fabrica.getProductosDisponibles())}.")
                    else:
                        productoSeleccionado = Fabrica.getProductosDisponibles()[productoSeleccionadoIndex - 1]
                        print(f"PRODUCTO SELECCIONADO: {productoSeleccionado.getNombre()}")

                        categoriaProducto = productoSeleccionado.getCategoria()
                        cantidadActual = tiendaSeleccionada.getCantidadActualPorCategoria(categoriaProducto)
                        cantidadMaxima = 100  # Ejemplo de capacidad máxima

                        cantidadDisponible = cantidadMaxima - cantidadActual
                        print(f"Cantidad máxima de productos en la categoría {categoriaProducto}: {cantidadDisponible}")
                        print("Ingrese la cantidad de productos a enviar:")

                        cantidadAEnviar = -1
                        while cantidadAEnviar < 0 or cantidadAEnviar > cantidadDisponible:
                            try:
                                cantidadAEnviar = int(input("» "))
                                if cantidadAEnviar < 0 or cantidadAEnviar > cantidadDisponible:
                                    print(f"Cantidad inválida. Ingrese un número entre 0 y {cantidadDisponible}.")
                                else:
                                    print(f"Enviando {cantidadAEnviar} productos de la categoría {categoriaProducto} a la tienda {tiendaSeleccionada.getNombre()}")

                                    productosGenerados.extend(Fabrica.cantidadProductos(productoSeleccionado, cantidadAEnviar))
                                    pesoTotalProductos += productoSeleccionado.getPeso() * cantidadAEnviar

                                    if categoriaProducto == "Herramientas":
                                        conteoCategoriasTemporal[0] += cantidadAEnviar
                                    elif categoriaProducto == "Muebles":
                                        conteoCategoriasTemporal[1] += cantidadAEnviar
                                    elif categoriaProducto == "Aseo":
                                        conteoCategoriasTemporal[2] += cantidadAEnviar
                            except Exception as e:
                                print("Entrada inválida. Por favor, ingrese un número.")
                except Exception as e:
                    print("Entrada inválida. Por favor, ingrese un número.")

            print("Productos por categoría en la tienda seleccionada:")
            print(tiendaSeleccionada.productosPorCategoria(tiendaSeleccionada.getListaProducto(), conteoCategoriasTemporal))

            print("========================================")
            print("¿Desea añadir más productos?")
            print("(s) para sí, (v) para volver a elegir productos, cualquier otra tecla para continuar):")
            print("========================================")

            try:
                respuesta = input("» ")
                if respuesta.lower() == "v":
                    productosGenerados.clear()
                    conteoCategoriasTemporal = [
                        tiendaSeleccionada.getCantidadActualPorCategoria("Herramientas"),
                        tiendaSeleccionada.getCantidadActualPorCategoria("Muebles"),
                        tiendaSeleccionada.getCantidadActualPorCategoria("Aseo")
                    ]
                    pesoTotalProductos = 0.0
                    continue
                if respuesta.lower() != "s":
                    break
            except Exception as e:
                print("Entrada inválida. Ingrese una letra.")

        listaTransportes = TipoTransporte.crearTipoTransporteSegunCarga(pesoTotalProductos)
        print("========================================")
        print(TipoTransporte.mostrarTipoTransporteSegunCarga(listaTransportes))
        print("========================================")

        print("Seleccione el tipo de transporte para enviar los productos. (0 para salir):")
        transporteSeleccionadoIndex = -1
        transporteSeleccionado = None

        while transporteSeleccionadoIndex < 0 or transporteSeleccionadoIndex > len(listaTransportes):
            try:
                transporteSeleccionadoIndex = int(input("» "))
                if transporteSeleccionadoIndex == 0:
                    time.sleep(1)
                    print("Saliendo...")
                    return
                if transporteSeleccionadoIndex < 1 or transporteSeleccionadoIndex > len(listaTransportes):
                    print(f"Número inválido. Ingrese un número entre 1 y {len(listaTransportes)}.")
                else:
                    transporteSeleccionado = TipoTransporte.seleccionarTransporte(listaTransportes, transporteSeleccionadoIndex)
                    print(f"Transporte seleccionado: {transporteSeleccionado.getNombre()}")

                    conductorSeleccionado = None
                    for conductor in Conductor.getListaConductores():
                        if conductor.getTransporte().tipoTransporte == transporteSeleccionado:
                            conductorSeleccionado = conductor
                            break

                    if conductorSeleccionado is None:
                        print("No se encontró un conductor con el transporte seleccionado.")
                        transporteSeleccionado = None
                        continue

                    print("========================================")
                    print("¿Desea confirmar el abastecimiento?")
                    print("(s) para sí, (v) para volver al paso anterior, cualquier otra tecla para cancelar):")
                    print("========================================")
                    confirmar = input("» ")
                    if confirmar.lower() == "v":
                        conductorSeleccionado = None
                        transporteSeleccionado = None
                        continue
                    if confirmar.lower() == "s":
                        tiendaSeleccionada.setConteoCategorias(conteoCategoriasTemporal)
                        tiendaSeleccionada.setListaProducto(tiendaSeleccionada.getListaProducto())

                        time.sleep(1)
                        print("========================================")
                        print("Abastecimiento confirmado.")
                        print(f"Enviando productos a la tienda {tiendaSeleccionada.getNombre()}...")
                        print("========================================")

                        transporte = conductorSeleccionado.getTransporte()
                        transporte.abastecerProducto(tiendaSeleccionada, productosGenerados)

                        conductorSeleccionado.setIndiceMeta(conductorSeleccionado.indiceMeta + pesoTotalProductos)
                        conductorSeleccionado.cantidadTrabajo += 1
                        Fabrica.getOperario().setIndiceMeta(Fabrica.getOperario().indiceMeta + 1)
                        Fabrica.getOperario().cantidadTrabajo += 1

                        tiendaSeleccionada.descargarProducto(transporte)
                        print(f"PRODUCTOS DESCARGADOS EN LA TIENDA {tiendaSeleccionada.getNombre()}")
                        print(f"Ha seleccionado el transporte: #{transporteSeleccionadoIndex}")
                        print(f"La tienda {tiendaSeleccionada.getNombre()} se abastecerá por: {transporteSeleccionado.getNombre()}")
                        print("\n¡¡¡EL PRODUCTO FUE ENVIADO CON EXITO!!!. Ahora la tienda tiene:\n")
                        print("    PRODUCTOS:")
                        print(tiendaSeleccionada.cantidadProductos())
                    else:
                        print("Abastecimiento cancelado.")
                        continue
            except Exception as e:
                print("Entrada inválida. Por favor, ingrese un número.")

        print("========================================")
        print("¿Desea volver al menú principal o realizar otro proceso de abastecer alguna tienda?")
        print("1. Volver al menú principal")
        print("0. Realizar otro proceso de abastecer alguna tienda")
        print("Cualquier otro número: Salir del programa")
        print("========================================")
        try:
            opcion = int(input("» "))
            if opcion == 1:
                print("========================================")
                print("ABASTECIMIENTO FINALIZADO")
                print("Volviendo al menú principal...")
                salir = True
            elif opcion == 0:
                print("========================================")
                print("Realizando otro proceso de abastecer alguna tienda...")
                print("========================================")
            else:
                print("Opción inválida. Volviendo al menú principal...")
                salir = True
        except Exception as e:
            print("Entrada inválida. Volviendo al menú principal...")
            salir = True

if __name__ == "__main__":
    main()
 


