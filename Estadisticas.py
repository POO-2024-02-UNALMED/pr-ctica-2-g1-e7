from src.gestorAplicacion.gestion.Factura import Factura
from src.gestorAplicacion.produccion.EstadoProducto import EstadosProducto
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

    while(True):
        pass
    