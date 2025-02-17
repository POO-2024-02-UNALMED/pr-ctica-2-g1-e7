from src.gestorAplicacion.gestion.Factura import Factura
from src.gestorAplicacion.produccion.Producto import Producto
from src.gestorAplicacion.gestion.Cliente import Cliente
from src.gestorAplicacion.produccion.Tienda import Tienda

def bienvenida():
    return "¡Bienvenido al sistema!\n\n Esta es la sección de mostrar estadísticas,\n en este, podras ver informaciones estadísticas detalladas, a partir de cualquier fecha dentro del margen de fechas de facturación.\n"

def asignar_fechas(fecha_inicio, fecha_fin):
    global fecha_inicial, fecha_final
    fecha_inicial = fecha_inicio
    fecha_final = fecha_fin

def mostrar_estadisticas():
    global fecha_inicial, fecha_final
    facturas = Factura.facturas_entre_fechas(fecha_inicial, fecha_final)
    if not facturas:
        return "No hay facturas en el rango de fechas seleccionado."
    else:
        return "Estadísticas de la empresa entre las fechas " + str(fecha_inicial) + " y " + str(fecha_final) + ":\n" + \
               "Total de facturas: " + str(len(facturas)) + "\n" + \
               "Total de productos vendidos: " + str(sum([factura.cantidad for factura in facturas])) + "\n" + \
               "Total de ingresos: " + str(sum([factura.total for factura in facturas])) + "\n" + \
               "Total de clientes: " + str(len(set([factura.cliente for factura in facturas]))) + "\n" + \
               "Total de tiendas: " + str(len(set([factura.tienda for factura in facturas])))