from gestorAplicacion.gestion.Factura import Factura
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.gestion.Cliente import Cliente
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.produccion.Transporte import Transporte
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
                    print(Factura.getFechaMaxima())
                    fechaInicio = Factura.getFechaMinima()
                    fechaFinal = Factura.getFechaMaxima()
                    break
                elif sel1 == "n":
                    FechaInicio = datetime(input("Ingrese la fecha de inicio (dd-mm-yyyy): "))
                    while(True):
                        try:
                            if FechaInicio < Factura.getFechaMinima():
                                print("La fecha de inicio debe ser mayor o igual a la de inicio por defecto")
                            else:
                                break
                        except ValueError:
                            print("formato de fecha inválido")

                    while(True):
                        try:
                            FechaFinal = datetime(input("Ingrese la fecha de finalización (dd-mm-yyyy): "))
                            if FechaFinal < FechaInicio:
                                print("La fecha de finalización debe ser mayor o igual a la de inicio")
                            else:
                                break
                        except ValueError:
                            print("formato de fecha inválido")

                    fechaInicio = FechaInicio
                    fechaFinal = FechaFinal
                        
                else:
                    print("Entrada inválida")
            except ValueError:
                print("Entrada inválida")

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
                    print("Ganancias Discretas")
                    print(Factura.gananciasDiscretas(fecha_min=fechaInicio, fecha_max=fechaFinal))
                elif sel == "2":
                    print("Ganancias totales")
                    print(Factura.gananciaTotal(fechaInicio, fechaFinal))
                elif sel == "3":
                    print("Promedio de ganancias")
                    print(Factura.promedioDeGanancias(fechaInicio, fechaFinal))
                elif sel == "4":
                    print("Vriaciones porcentuales")
                    print(Factura.aumentosPorcentuales(fechaInicio, fechaFinal))
                elif sel == "5":
                    print("Modas")
                    print("Producto más vendido: ")
                    print(Factura.modaProductos(fechaInicio, fechaFinal))
                    print("Cliente con más facturaciones: ")
                    print(Factura.modaClientes(fechaInicio, fechaFinal))
                elif sel == "6":
                    self.asignarFechas()
                elif sel == "0":
                    print("Saliendo del módulo de estadísticas")
                    time.sleep(2)
                    break
            except ValueError:
                    print("Entrada inválida")
            
            print("Desea realizar otra consulta? \ns \npulse cualquier tecla para salir")
            sel2 = input()
            if sel2 == "n":
                break
                

if __name__ == "__main__":
    f1 = Factura(tienda=Tienda(nombre="Tienda 1"), cliente=Cliente(nombre="Cliente 1"), fecha=datetime(2021, 5, 1).strftime("%d-%m-%Y"), transporte=Transporte(), lista_productos=[Producto(nombre="Producto 1", precio=3000, peso=3, tipo="Prod", categoria="Inmueble"), Producto(nombre="Producto 2", precio=3000, peso=3, tipo="Prod", categoria="Inmueble")], precio_envio=1000)
    f2 = Factura(tienda=Tienda(nombre="Tienda 2"), cliente=Cliente(nombre="Cliente 2"), fecha=datetime(2021, 5, 2).strftime("%d-%m-%Y"), transporte=Transporte(), lista_productos=[Producto(nombre="Producto 3", precio=3000, peso=3, tipo="Prod", categoria="Inmueble"), Producto(nombre="Producto 3", precio=3000, peso=3, tipo="Prod", categoria="Inmueble")], precio_envio=2000)
    e = Estadisticas()
    e.estadistica()
