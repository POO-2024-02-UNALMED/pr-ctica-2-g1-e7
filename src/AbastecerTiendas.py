import time

from gestorAplicacion.produccion.Fabrica import Fabrica
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.produccion.TipoTransporte import TipoTransporte
from gestorAplicacion.produccion.Transporte import Transporte
from gestorAplicacion.gestion.Conductor import Conductor
def main():
    salir = False
    while not salir:
        print("========================================")
        print("¡Bienvenido a la opción de abastecer tienda!")
        print("Seleccione la tienda que desea abastecer (0 para salir):")
        print("========================================")
        print("0. Salir")
        print(Fabrica.mostrar_tiendas())
        print("========================================")

        tienda_seleccionada_index = -1
        tienda_seleccionada = None

        while tienda_seleccionada_index < 0 or tienda_seleccionada_index > len(Fabrica.get_lista_tienda()):
            try:
                tienda_seleccionada_index = int(input("» "))
                if tienda_seleccionada_index == 0:
                    time.sleep(1)
                    print("Saliendo...")
                    return
                if tienda_seleccionada_index < 1 or tienda_seleccionada_index > len(Fabrica.get_lista_tienda()):
                    print(f"Número inválido. Ingrese un número entre 1 y {len(Fabrica.get_lista_tienda())}.")
                else:
                    confirmacion_tienda = False
                    while not confirmacion_tienda:
                        tienda_seleccionada = Fabrica.get_lista_tienda()[tienda_seleccionada_index - 1]
                        print(f"Tienda seleccionada: {tienda_seleccionada.get_nombre()}")
                        print("¿Es correcta esta selección? (1 para sí, 2 para no)")
                        print("1. Sí, proceder")
                        print("2. No, seleccionar otra tienda")

                        try:
                            confirmacion = int(input("» "))
                            if confirmacion == 1:
                                print("Procediendo con la tienda seleccionada...")
                                confirmacion_tienda = True
                            elif confirmacion == 2:
                                print("========================================")
                                print("Seleccione la tienda que desea abastecer (0 para salir):")
                                print("========================================")
                                print("0. Salir")
                                print(Fabrica.mostrar_tiendas())
                                print("========================================")
                                tienda_seleccionada_index = int(input("» "))
                                if tienda_seleccionada_index == 0:
                                    time.sleep(1)
                                    print("Saliendo...")
                                    return
                                if tienda_seleccionada_index < 1 or tienda_seleccionada_index > len(Fabrica.get_lista_tienda()):
                                    print(f"Número inválido. Ingrese un número entre 1 y {len(Fabrica.get_lista_tienda())}.")
                                else:
                                    print("Entrada inválida. Por favor, ingrese un número.")
                        except Exception as e:
                            print("Entrada inválida. Por favor, ingrese un número.")
            except Exception as e:
                print("Entrada inválida. Por favor, ingrese un número.")

        print("========================================")
        print("Productos por categoría en la tienda seleccionada:")
        print(tienda_seleccionada.productos_por_categoria(tienda_seleccionada.get_lista_producto()))

        productos_generados = []
        conteo_categorias_temporal = [
            tienda_seleccionada.get_cantidad_actual_por_categoria("Herramientas"),
            tienda_seleccionada.get_cantidad_actual_por_categoria("Muebles"),
            tienda_seleccionada.get_cantidad_actual_por_categoria("Aseo")
        ]
        peso_total_productos = 0.0

        while True:
            print("========================================")
            print("Seleccione el producto que desea enviar a la tienda (0 para salir):")
            print("========================================")
            print("0. Salir")
            print(Fabrica.mostrar_productos())
            print("========================================")
            producto_seleccionado_index = -1
            producto_seleccionado = None

            while producto_seleccionado_index < 0 or producto_seleccionado_index > len(Fabrica.get_productos_disponibles()):
                try:
                    producto_seleccionado_index = int(input("» "))
                    if producto_seleccionado_index == 0:
                        time.sleep(1)
                        print("Saliendo...")
                        return
                    if producto_seleccionado_index < 1 or producto_seleccionado_index > len(Fabrica.get_productos_disponibles()):
                        print(f"Número inválido. Ingrese un número entre 1 y {len(Fabrica.get_productos_disponibles())}.")
                    else:
                        producto_seleccionado = Fabrica.get_productos_disponibles()[producto_seleccionado_index - 1]
                        print(f"PRODUCTO SELECCIONADO: {producto_seleccionado.get_nombre()}")

                        categoria_producto = producto_seleccionado.get_categoria()
                        cantidad_actual = tienda_seleccionada.get_cantidad_actual_por_categoria(categoria_producto)
                        cantidad_maxima = 100  # Ejemplo de capacidad máxima

                        cantidad_disponible = cantidad_maxima - cantidad_actual
                        print(f"Cantidad máxima de productos en la categoría {categoria_producto}: {cantidad_disponible}")
                        print("Ingrese la cantidad de productos a enviar:")

                        cantidad_a_enviar = -1
                        while cantidad_a_enviar < 0 or cantidad_a_enviar > cantidad_disponible:
                            try:
                                cantidad_a_enviar = int(input("» "))
                                if cantidad_a_enviar < 0 or cantidad_a_enviar > cantidad_disponible:
                                    print(f"Cantidad inválida. Ingrese un número entre 0 y {cantidad_disponible}.")
                                else:
                                    print(f"Enviando {cantidad_a_enviar} productos de la categoría {categoria_producto} a la tienda {tienda_seleccionada.get_nombre()}")

                                    productos_generados.extend(Fabrica.cantidad_productos(producto_seleccionado, cantidad_a_enviar))
                                    peso_total_productos += producto_seleccionado.get_peso() * cantidad_a_enviar

                                    if categoria_producto == "Herramientas":
                                        conteo_categorias_temporal[0] += cantidad_a_enviar
                                    elif categoria_producto == "Muebles":
                                        conteo_categorias_temporal[1] += cantidad_a_enviar
                                    elif categoria_producto == "Aseo":
                                        conteo_categorias_temporal[2] += cantidad_a_enviar
                            except Exception as e:
                                print("Entrada inválida. Por favor, ingrese un número.")
                except Exception as e:
                    print("Entrada inválida. Por favor, ingrese un número.")

            print("Productos por categoría en la tienda seleccionada:")
            print(tienda_seleccionada.productos_por_categoria(tienda_seleccionada.get_lista_producto(), conteo_categorias_temporal))

            print("========================================")
            print("¿Desea añadir más productos?")
            print("(s) para sí, (v) para volver a elegir productos, cualquier otra tecla para continuar):")
            print("========================================")

            try:
                respuesta = input("» ")
                if respuesta.lower() == "v":
                    productos_generados.clear()
                    conteo_categorias_temporal = [
                        tienda_seleccionada.get_cantidad_actual_por_categoria("Herramientas"),
                        tienda_seleccionada.get_cantidad_actual_por_categoria("Muebles"),
                        tienda_seleccionada.get_cantidad_actual_por_categoria("Aseo")
                    ]
                    peso_total_productos = 0.0
                    continue
                if respuesta.lower() != "s":
                    break
            except Exception as e:
                print("Entrada inválida. Ingrese una letra.")

        lista_transportes = TipoTransporte.crear_tipo_transporte_segun_carga(peso_total_productos)
        print("========================================")
        print(TipoTransporte.mostrar_tipo_transporte_segun_carga(lista_transportes))
        print("========================================")

        print("Seleccione el tipo de transporte para enviar los productos. (0 para salir):")
        transporte_seleccionado_index = -1
        transporte_seleccionado = None

        while transporte_seleccionado_index < 0 or transporte_seleccionado_index > len(lista_transportes):
            try:
                transporte_seleccionado_index = int(input("» "))
                if transporte_seleccionado_index == 0:
                    time.sleep(1)
                    print("Saliendo...")
                    return
                if transporte_seleccionado_index < 1 or transporte_seleccionado_index > len(lista_transportes):
                    print(f"Número inválido. Ingrese un número entre 1 y {len(lista_transportes)}.")
                else:
                    transporte_seleccionado = TipoTransporte.seleccionar_transporte(lista_transportes, transporte_seleccionado_index)
                    print(f"Transporte seleccionado: {transporte_seleccionado.get_nombre()}")

                    conductor_seleccionado = None
                    for conductor in Conductor.get_lista_conductores():
                        if conductor.get_transporte().tipo_transporte == transporte_seleccionado:
                            conductor_seleccionado = conductor
                            break

                    if conductor_seleccionado is None:
                        print("No se encontró un conductor con el transporte seleccionado.")
                        transporte_seleccionado = None
                        continue

                    print("========================================")
                    print("¿Desea confirmar el abastecimiento?")
                    print("(s) para sí, (v) para volver al paso anterior, cualquier otra tecla para cancelar):")
                    print("========================================")
                    confirmar = input("» ")
                    if confirmar.lower() == "v":
                        conductor_seleccionado = None
                        transporte_seleccionado = None
                        continue
                    if confirmar.lower() == "s":
                        tienda_seleccionada.set_conteo_categorias(conteo_categorias_temporal)
                        tienda_seleccionada.set_lista_producto(tienda_seleccionada.get_lista_producto())

                        time.sleep(1)
                        print("========================================")
                        print("Abastecimiento confirmado.")
                        print(f"Enviando productos a la tienda {tienda_seleccionada.get_nombre()}...")
                        print("========================================")

                        transporte = conductor_seleccionado.get_transporte()
                        transporte.abastecer_producto(tienda_seleccionada, productos_generados)

                        conductor_seleccionado.set_indice_meta(conductor_seleccionado.indice_meta + peso_total_productos)
                        conductor_seleccionado.cantidad_trabajo += 1
                        Fabrica.get_operario().set_indice_meta(Fabrica.get_operario().indice_meta + 1)
                        Fabrica.get_operario().cantidad_trabajo += 1

                        tienda_seleccionada.descargar_producto(transporte)
                        print(f"PRODUCTOS DESCARGADOS EN LA TIENDA {tienda_seleccionada.get_nombre()}")
                        print(f"Ha seleccionado el transporte: #{transporte_seleccionado_index}")
                        print(f"La tienda {tienda_seleccionada.get_nombre()} se abastecerá por: {transporte_seleccionado.get_nombre()}")
                        print("\n¡¡¡EL PRODUCTO FUE ENVIADO CON EXITO!!!. Ahora la tienda tiene:\n")
                        print("    PRODUCTOS:")
                        print(tienda_seleccionada.cantidad_productos())
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
