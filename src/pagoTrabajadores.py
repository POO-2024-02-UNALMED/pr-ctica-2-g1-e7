from gestorAplicacion.gestion.Operario import Operario
from gestorAplicacion.gestion.Vendedor import Vendedor
from gestorAplicacion.gestion.Conductor import Conductor
from gestorAplicacion.produccion.Fabrica import Fabrica
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria
from gestorAplicacion.gestion.Meta import Meta
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.produccion.Tienda import Tienda


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
                break
            
            print("Mostrando trabajadores...")
            print(Fabrica.mostrarPersonas(trabajadores))
            
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
                    return
                elif opcionPT3 == 3:
                    break
                elif opcionPT3 == 1:
                    while True:
                        if verificador == False:
                            break

                        metasTrabajador = trabajadorSeleccionado.getMeta()
                        metasNoPagas = []
                        for meta in metasTrabajador:
                            if meta.getVerificador() == False:
                                metasNoPagas.append(meta)
                        
                        if not metasNoPagas:
                            print("El trabajador no tiene metas en este momento.\nProcediendo con el pago.")
                            verificador = False
                            break
                        
                        print(trabajadorSeleccionado.mostrarMetas())
                        
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
                                elif opcionPT5 == 2: 
                                    verificador = False
                                    break
                                
                elif opcionPT3 == 2:
                    break
            if opcionPT3 == 2 or opcionPT3 == 1:    
                pagoTotal = pagoPotencial + pagoPorMetas
                print("Procesando pago...")
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
                print("\n¿Qué desea hacer? \n1. Pagar a otro trabajador. \n0. Volver al menú principal.")
                opcionPT4 = input("» ")
                
                if not opcionPT4.isdigit():
                    print("Entrada inválida. Por favor, ingrese un número.")
                    continue
                
                opcionPT4 = int(opcionPT4)
                if opcionPT4 == 1:
                    break
                elif opcionPT4 == 0:
                    print("Volviendo al menú principal.")
                    return
                else:
                    print("Seleccione una opción válida.")
                    continue
