from gestorAplicacion.gestion.Operario import Operario
from gestorAplicacion.gestion.Vendedor import Vendedor
from gestorAplicacion.gestion.Conductor import Conductor
from gestorAplicacion.produccion.Fabrica import Fabrica
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria
from gestorAplicacion.gestion.Meta import Meta
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.produccion.Tienda import Tienda
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

#Creacion de vendedores
meta1 = Meta("facil", 5, 10000)
meta2 = Meta("Dificil", 10, 20000)

cuenta1 = CuentaBancaria(123456, 10000)
cuenta2 = CuentaBancaria(123457, 20000)

vendedor1 = Vendedor("carlos", 10356, 19, cuenta1)
vendedor2 = Vendedor("Juan", 98765, 20, cuenta2)

vendedor1.setMetaVendedor(meta1)
vendedor1.setMetaVendedor(meta2)

vendedor2.setMetaVendedor(meta1)
vendedor2.setMetaVendedor(meta2)

vendedor1.setIndiceMeta(6)
vendedor1.setCantidadTrabajo(6)

vendedor2.setIndiceMeta(4)
vendedor2.setCantidadTrabajo(4)

import time

def pagoTrabajadores():
    print("\nEligió la opción de pagar a sus trabajadores.")
    while True:
        listaTrabajadores = []
        verificador = None
        while True:
            print("Seleccione el tipo de empleado que desea pagarle.")
            print("1. Operarios \n2. Conductores \n3. Vendedores\n0. Volver al menú.")
            opcionPT = input("» ")

            if not opcionPT.isdigit():
                print("\nEntrada inválida. Por favor, ingrese un número.")
                continue
            
            opcionPT = int(opcionPT)
            if opcionPT == 0:
                print("Volviendo al menú principal.\n")
                time.sleep(1)
                return
            elif opcionPT == 1:
                listaTrabajadores = Operario.getListaOperarios()
            elif opcionPT == 2:
                listaTrabajadores = Conductor.getListaConductores()
            elif opcionPT == 3:
                listaTrabajadores = Vendedor.getListaVendedores()
            else:
                print("\nEntrada inválida. Por favor, ingrese un número en el rango [0-3].")
                continue
            break
        
        while True:
            trabajadores = Fabrica.busquedaTrabajo(listaTrabajadores)
            if not trabajadores:
                print("\nNo hay trabajadores de este tipo para pagarles.")
                time.sleep(0.65)
                break
            
            print("Mostrando trabajadores...")
            time.sleep(1)
            print(Fabrica.mostrarPersonas(trabajadores))
            time.sleep(1)
            
            print(f"Elija el trabajador que desea pagarle. Seleccione un número entre: [1 - {len(trabajadores)}] \n0. Volver al menú.")
            opcionPT2 = input("» ")
            
            if not opcionPT2.isdigit():
                print("Entrada inválida. Por favor, ingrese un número.\n")
                continue
            
            opcionPT2 = int(opcionPT2)
            if opcionPT2 == 0:
                return
            
            if opcionPT2 < 1 or opcionPT2 > len(trabajadores):
                print("Escoja un número que esté dentro del rango.")
                continue
            
            trabajadorSeleccionado = trabajadores[opcionPT2 - 1]
            pagoPorMetas = 0
            pagoPotencial = trabajadorSeleccionado.getCuentaBancaria().calcularPago(trabajadorSeleccionado) + trabajadorSeleccionado.getSalarioBase()
            print(f"\nTrabajador(a) seleccionado(a): {trabajadorSeleccionado.getNombre()}. Se le debe hacer un pago de: {pagoPotencial} por haber trabajado {trabajadorSeleccionado.getCantidadTrabajo()} veces.\n")
            
            while True:
                if verificador == False:
                    break

                print("¿Quiere revisar las metas del trabajador?\n1. Sí\n2. No\n3. Cambiar de Trabajador\n0. Volver al menú principal.")
                opcionPT3 = input("» ")
                
                if not opcionPT3.isdigit():
                    print("\nEntrada inválida. Por favor, ingrese un número.\n")
                    continue
                
                opcionPT3 = int(opcionPT3)
                if opcionPT3 == 0:
                    print("Volviendo al menú principal.\n")
                    time.sleep(1)
                    return
                elif opcionPT3 == 3:
                    break
                elif opcionPT3 == 1:
                    while True:
                        if verificador == False:
                            break

                        metasTrabajador = trabajadorSeleccionado.getMeta()
                        metasNoPagas = [m for m in metasTrabajador if not m.getVerificador()]
                        
                        if not metasNoPagas:
                            print("El trabajador no tiene metas en este momento.\nProcediendo con el pago.")
                            verificador = False
                            break
                        
                        print(trabajadorSeleccionado.mostrarMetas())
                        time.sleep(1)
                        
                        print(f"\nSeleccione una meta entre [1 - {len(metasNoPagas)}] \n{len(metasNoPagas)+1}. Proceder con el pago. \n0. Volver al menú.")
                        opcionPT4 = input("» ")
                        
                        if not opcionPT4.isdigit():
                            print("Entrada inválida. Por favor, ingrese un número.\n")
                            continue
                        
                        opcionPT4 = int(opcionPT4)
                        if opcionPT4 == 0:
                            return
                        
                        elif opcionPT4 == len(metasNoPagas) + 1:
                            verificador = False
                            break

                        elif 1 <= opcionPT4 <= len(metasNoPagas):
                            metaSeleccionada = metasNoPagas[opcionPT4 - 1]
                            print(f"\nINFORMACIÓN DE LA META SELECCIONADA:\n{metaSeleccionada.porcentajeCumplidos(trabajadorSeleccionado.getIndiceMeta())}")
                            if metaSeleccionada.cumpleMeta(trabajadorSeleccionado.getIndiceMeta()):
                                print("La meta ha sido cumplida exitosamente.\nSumaremos el pago indicado por haberlo conseguido.\n")
                                pagoPorMetas += metaSeleccionada.getPago()
                                metaSeleccionada.setVerificador(True)
                            while True:
                                opcionPT5 = int(input("¿Qué desea hacer? \n1. Revisar otra meta. \n2. Proceder con el pago. \n» "))
                                if opcionPT5 != 1 and opcionPT5 != 2:
                                    print("Escoja alguna de las opciones.")
                                    continue
                                elif not int:
                                    print("Entrada inválida. Por favor, ingrese un número.\n")
                                    continue
                                elif opcionPT5 == 1:
                                    break
                                else: 
                                    verificador == False
                                    break
                                
                elif opcionPT3 == 2:
                    break
            if opcionPT3 == 2 or opcionPT3 == 1:    
                pagoTotal = pagoPotencial + pagoPorMetas
                print("Procesando pago...")
                time.sleep(1.5)
                Fabrica.cuentaBancaria.descontarDinero(pagoTotal)
                trabajadorSeleccionado.recibirSueldo(pagoTotal)
                print("\n------------------------------------------------------------")
                print(f"COMPROBANTE \nTrabajador(a): {trabajadorSeleccionado.getNombre()}")
                print(f"Total pagado: {pagoTotal}")
                print(f"- {pagoPotencial} por las veces trabajadas")
                print(f"- {pagoPorMetas} por las metas cumplidas")
                print("------------------------------------------------------------")
                break
                    
        while True:
                print("\n¿Qué desea hacer? \n1. Pagar a otro trabajador de la misma categoría. \n2. Volver a elegir tipo de trabajador. \n0. Volver al menú principal.")
                opcionPT4 = input("» ")
                
                if not opcionPT4.isdigit():
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
                
                opcionPT4 = int(opcionPT4)
                if opcionPT4 == 1:
                    continue
                elif opcionPT4 == 2:
                    break
                elif opcionPT4 == 0:
                    print("Volviendo al menú principal.")
                    time.sleep(1)
                    return
                else:
                    print("Seleccione una opción válida.")
                    continue

pagoTrabajadores()