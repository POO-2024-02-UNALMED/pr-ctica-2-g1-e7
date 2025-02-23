from gestorAplicacion.gestion.Factura import Factura
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.gestion.Cliente import Cliente
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.produccion.Transporte import Transporte
from Excepciones import FechaFueraDeRango
from datetime import datetime
import time



class Estadisticas:
    def __init__(self):
        pass

    def asignarFechas(self):
        global fechaInicio, fechaFinal
        while (True):
            print(f"Las fechas por defecto son {Factura.getFechaMinima()} y {Factura.getFechaMaxima()}\n")
            sel1 = input("Desea usar las fechas por defecto? (s/n): ")
            
            try:
                if sel1 == "s":
                    fechaInicio = Factura.getFechaMinima()
                    fechaFinal = Factura.getFechaMaxima()
                    break
                elif sel1 == "n":
                    while(True):
                        try:
                            FechaInicio = input("Ingrese la fecha de inicio (dd-mm-yyyy): ")
                            fechaInicio = datetime.strptime(FechaInicio, "%d-%m-%Y")
                            if fechaInicio < datetime.strptime(Factura.getFechaMinima(), "%d-%m-%Y"):
                                print("La fecha de inicio debe ser mayor o igual a la de inicio por defecto")
                                #raise FechaFueraDeRango("menor", "de inicio")
                            elif fechaInicio > datetime.strptime(Factura.getFechaMaxima(), "%d-%m-%Y"):
                                print("La fecha de inicio debe ser menor o igual a la de fin por defecto")
                            else:
                                break
                        #except FechaFueraDeRango as ffr:
                            #print(ffr)
                        except ValueError:
                            print("formato de fecha inválido")

                    while(True):
                        try:
                            FechaFinal = input("Ingrese la fecha de finalización (dd-mm-yyyy): ")
                            fechaFinal = datetime.strptime(FechaFinal, "%d-%m-%Y")
                            if fechaFinal < fechaInicio:
                                print("La fecha de finalización debe ser mayor o igual a la de inicio")
                                #raise FechaFueraDeRango("menor", "de inicio")
                            elif fechaFinal > datetime.strptime(Factura.getFechaMaxima(), "%d-%m-%Y"):
                                print("La fecha de finalización debe ser menor o igual a la de fin por defecto")
                            else:
                                break
                        #except FechaFueraDeRango as ffr:
                            #print(ffr)
                        except ValueError:
                            print("formato de fecha inválido")
                        
                else:
                    print("Entrada inválida")
            except ValueError:
                print("Entrada inválida")
        
            break

    def menu(self):
        print("Seleccione la estadística que desea consultar: ")
        print("1. Ganancias Discretas")
        print("2. Ganancias totales")
        print("3. Promedio de ganancias")
        print("4. Ganancias porcentuales")
        print("5. Modas")
        print("6. Cambiar fechas")
        print("0. Salir")


    def estadistica(self):
        print( f"Bienvenido al módulo de estadísticas\n")
        self.asignarFechas()
        print(f"Las fechas seleccionadas son {fechaInicio} y {fechaFinal}")
        while(True):
            try:
                self.menu()
                sel = input("Ingrese el número de la opción que desea seleccionar: ")
                if sel == "1":
                    print("Las Ganancias Discretas son: ")
                    print(Factura.gananciasDiscretas(fecha_min=fechaInicio, fecha_max=fechaFinal))
                elif sel == "2":
                    print("Las Ganancias totales son: ")
                    print(Factura.gananciaTotal(fechaInicio, fechaFinal))
                elif sel == "3":
                    print("El Promedio de ganancias es: ")
                    print(Factura.promedioDeGanancias(fechaInicio, fechaFinal))
                elif sel == "4":
                    print("Las Variaciones porcentuales son: ")
                    print(Factura.aumentosPorcentuales(fechaInicio, fechaFinal))
                elif sel == "5":
                    print("Estas son los valores moda: ")
                    print("Producto más vendido: ")
                    print(Factura.modaProductos(fechaInicio, fechaFinal))
                    print("Cliente con más facturaciones: ")
                    print(Factura.modaClientes(fechaInicio, fechaFinal))
                    print("Tienda con más facturaciones: ")
                    print(Factura.modaTiendas(fechaInicio, fechaFinal))
                elif sel == "6":
                    self.asignarFechas()
                elif sel == "0":
                    print("Saliendo del módulo de estadísticas")
                    time.sleep(2)
                    break
            except ValueError:
                    print("Entrada inválida")
            
            print("Desea realizar otra consulta? \ns | pulse cualquier tecla para salir")
            sel2 = input()
            if sel2 != "s":
                break
                

if __name__ == "__main__":
    f1 = Factura(tienda=Tienda(nombre="Tienda 1"), cliente=Cliente(nombre="Cliente 1"), fecha=datetime(2021, 5, 1).strftime("%d-%m-%Y"), transporte=Transporte(), lista_productos=[Producto(nombre="Producto 1", precio=3000, peso=3, tipo="Prod", categoria="Inmueble"), Producto(nombre="Producto 2", precio=3000, peso=3, tipo="Prod", categoria="Inmueble")], precio_envio=1000)
    f2 = Factura(tienda=Tienda(nombre="Tienda 2"), cliente=Cliente(nombre="Cliente 2"), fecha=datetime(2021, 5, 2).strftime("%d-%m-%Y"), transporte=Transporte(), lista_productos=[Producto(nombre="Producto 3", precio=3000, peso=3, tipo="Prod", categoria="Inmueble"), Producto(nombre="Producto 3", precio=3000, peso=3, tipo="Prod", categoria="Inmueble")], precio_envio=2000)
    e = Estadisticas()
    e.estadistica()
