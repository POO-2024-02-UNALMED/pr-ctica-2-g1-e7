from gestorAplicacion.gestion.Factura import Factura
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.gestion.Cliente import Cliente
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.produccion.Transporte import Transporte
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
        print( f"Bienvenido al módulo de estadísticas\n Las fechas por defecto son {Factura.getFechaMinima()} y {Factura.getFechaMaxima()}\n")
    

if __name__ == "__main__":
    try:
        fact1 = Factura(Tienda(nombre="Tienda1", vendedor=None), Cliente("Juan", 20, 1234567890), Transporte("Transporte1", "Calle 2", "0987654321"), [Producto("Producto1", 1000, None, "Tipo1", "Categoria1", 1), Producto("Producto2", 2000, None, "Tipo2", "Categoria2", 2)], 1000, datetime.now())
        print(fact1)
    except Exception as e:
        print(e)
