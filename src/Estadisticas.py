from gestorAplicacion.produccion.EstadoProducto import EstadosProducto
from gestorAplicacion.gestion.Factura import Factura
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.gestion.Cliente import Cliente
from gestorAplicacion.produccion.Tienda import Tienda
from datetime import datetime

class Estadisticas:
    def __init__(self):
        pass

    def asignarFechas(self):
        global fechaInicio, fechaFinal
        while (True):
            sel1 = input("Desea usar las fechas por defecto? (s/n): ")
            
            try:
                if sel1 == "s":
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
                        
                else:
                    print("Entrada inválida")
            except ValueError:
                print("Entrada inválida")


    def estadistica(self):
        print( f"Bienvenido al módulo de estadísticas\n Las fechas por defecto son {Factura.fechaInicio} y {Factura.fechaFin}\n")
    

if __name__ == "__main__":
    fact1 = Factura(Tienda("Tienda1", "Calle 1", "1234567890"), Cliente("Juan", "Perez", "1234567890"), Transporte("Transporte1", "Calle 2", "0987654321"))
    print(fact1.getFecha())
