import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))



class Fabrica:
    listaFabrica = []
    _cuentaBancaria = None
    _productosDisponibles = []
    _listaTienda=[]

    def __init__(self, idFabrica, nombre, direccion, cuentaBancariaFabrica, productosDisponibles, operario):
        self.idFabrica = idFabrica
        self.nombre = nombre
        self.direccion = direccion
        self.operario = operario  

        Fabrica.listaFabrica.append(self)
        Fabrica._cuentaBancaria = cuentaBancariaFabrica
        Fabrica._productosDisponibles.extend(productosDisponibles)

        operario.setFabrica(self)

    # Getters y Setters para atributos privados (estáticos)
    @staticmethod
    def agregarTienda(tienda):
        Fabrica.getListaTienda().append(tienda)
    @staticmethod
    def getCuentaBancaria():
        return Fabrica._cuentaBancaria

    @staticmethod
    def setCuentaBancaria(cuentaBancaria):
        Fabrica._cuentaBancaria = cuentaBancaria

    @staticmethod
    def getListaTienda():
        return Fabrica._listaTienda
    @staticmethod
    def getProductosDisponibles():
        return Fabrica._productosDisponibles

    @staticmethod
    def setProductosDisponibles(productosDisponibles):
        Fabrica._productosDisponibles = productosDisponibles

    @staticmethod
    def busquedaTrabajo(listaTrabajadores):
        trabajadores = []
        for e in listaTrabajadores:
            if e.getCantidadTrabajo() > 0:
                trabajadores.append(e)
        return trabajadores

    @staticmethod
    def mostrarPersonas(listaTrabajadores):
        texto = ""
        for indice, persona in enumerate(listaTrabajadores, start=1):
            texto += f"\nTrabajador {indice} {persona}"
        return texto

    @staticmethod
    def descontarDineroCuenta(producto) -> float:
        """
        Resta el precio del producto devuelto de la cuenta bancaria de la fábrica.
        """
        if Fabrica.getCuentaBancaria() is None:
            raise ValueError("Error: La fábrica no tiene una cuenta bancaria registrada.")

        if producto.getPrecio() is None:
            raise ValueError("Error: El producto no tiene un precio definido.")

        cuenta = Fabrica.getCuentaBancaria()
        cuenta.setSaldo(cuenta.getSaldo() - producto.getPrecio())
        return producto.getPrecio()

    @staticmethod
    def calcularExcedente(productos, valor: float) -> float:
        """
        Calcula si el cliente debe pagar un excedente al cambiar productos.
        """
        subtotal = sum(p.getPrecio() for p in productos if p.getPrecio() is not None)
        return max(0, subtotal - valor)

    @staticmethod
    def mostrarTiendas():
        """
        Muestra las tiendas registradas y sus productos en stock.
        """
        if not Fabrica.getListaTienda():
            return "No hay tiendas disponibles."

        resultado = "Listado de Tiendas:\n"
        for i, tienda in enumerate(Fabrica.getListaTienda(), start=1):
            resultado += f"{i}. {tienda.getNombre()}:\n"
            productos = tienda.cantidadProductos().split("\n")
            resultado += "\n".join(f"    {p}" for p in productos) + "\n"

        return resultado.strip()

    @staticmethod
    def mostrarTiendasSinProductos():
        """
        Muestra una lista numerada de las tiendas sin incluir los productos.
        """
        if not Fabrica.getListaTienda():
            return "No hay tiendas registradas."

        return "\n".join(f"{i}. Tienda: {t.getNombre()}" for i, t in enumerate(Fabrica.getListaTienda(), start=1))

    @staticmethod
    def mostrarProductos():
        """
        Muestra los productos disponibles en la fábrica usando la interfaz IMostrarProductos.
        """
        from gestorAplicacion.gestion.IMostrarProductos import IMostrarProductos
        return IMostrarProductos.mostrarProductosLista(Fabrica.getProductosDisponibles())

    @staticmethod
    def cantidadProductos(producto, cantidad_a_enviar: int):
        from gestorAplicacion.produccion.Producto import Producto
        """
        Genera una cantidad específica de productos para abastecimiento.
        """

        if not isinstance(producto, Producto):
            raise ValueError("Error: El objeto proporcionado no es un producto válido.")
        if cantidad_a_enviar <= 0:
            raise ValueError("Error: La cantidad a enviar debe ser mayor a 0.")

        return [Producto(producto.getNombre, producto.getPrecio, producto.getEstado,
                         producto.getTipo, producto.getCategoria, producto.getPeso)
                for _ in range(cantidad_a_enviar)]

import datetime
from gestorAplicacion.gestion.Vendedor import Vendedor
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.produccion.EstadoProducto import EstadosProducto
from gestorAplicacion.gestion.Conductor import Conductor
from gestorAplicacion.produccion.Transporte import Transporte
from gestorAplicacion.produccion.TipoTransporte import TipoTransporte
from gestorAplicacion.gestion.Operario import Operario
from gestorAplicacion.gestion.Meta import Meta




cuentaFabrica = CuentaBancaria(99999, 100000)
cuentaVendedor1 = CuentaBancaria(56932, 100)
cuentaVendedor2 = CuentaBancaria(45728, 200)
cuentaVendedor3 = CuentaBancaria(95687, 200)

# Crear vendedores
vendedor1 = Vendedor("Maria Beatriz", 577935, 20, cuentaVendedor1)
vendedor2 = Vendedor("Adriana Alexia Putellas", 89235, 21, cuentaVendedor2)
vendedor3 = Vendedor("Lionel Andres Messi", 14720, 22, cuentaVendedor3)

# Crear tiendas
tienda1 = Tienda("Herramientas UNAL", vendedor1, cuentaFabrica, 100, 100, 100)
tienda2 = Tienda("Muebles Comodísimo", vendedor2, cuentaFabrica, 100, 100, 100)
tienda3 = Tienda("Limpieza UNAL", vendedor3, cuentaFabrica, 100, 100, 100)

#Crear Productos para cada tienda
producto1 = Producto("Cemento Gris", 50000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)
producto2 = Producto("Cemento Gris", 50000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)
producto3 = Producto("Cemento Gris", 50000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)
producto4 = Producto("Cemento Gris", 50000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)
producto5 = Producto("Cemento Gris", 50000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)

producto6 = Producto("Cemento Blanco", 55000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)
producto7 = Producto("Cemento Blanco", 55000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 25.0)

producto8 = Producto("Adhesivo Cerámico", 20000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 5.0)
producto9 = Producto("Adhesivo Cerámico", 20000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 5.0)

producto10 = Producto("Pintura Interior", 35000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 18.0)
producto11 = Producto("Pintura Interior", 35000, EstadosProducto.DISPONIBLE, "Material", "Herramientas", 18.0)

# Tienda 2
producto12 = Producto("Sillas", 10000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)
producto13 = Producto("Sillas", 10000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)
producto14 = Producto("Sillas", 10000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)

producto15 = Producto("Mesas", 8000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 2.0)
producto16 = Producto("Mesas", 8000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 2.0)
producto17 = Producto("Mesas", 8000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 2.0)

producto18 = Producto("Sofa", 5000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)
producto19 = Producto("Sofa", 5000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)
producto20 = Producto("Sofa", 5000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)

producto21 = Producto("Mesa de noche", 12000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 0.5)
producto22 = Producto("Mesa de noche", 12000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 0.5)
producto23 = Producto("Mesa de noche", 12000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 0.5)

producto24 = Producto("Cama", 7000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 0.25)
producto25 = Producto("Cama", 7000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 0.25)
producto26 = Producto("Cama", 7000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 0.25)

producto27 = Producto("Escritorio", 15000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)
producto28 = Producto("Escritorio", 15000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)
producto29 = Producto("Escritorio", 15000, EstadosProducto.DISPONIBLE, "Comodidad", "Muebles", 1.0)

# Tienda 3
producto30 = Producto("Detergente", 15000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 3.0)
producto31 = Producto("Detergente", 15000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 3.0)
producto32 = Producto("Detergente", 15000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 3.0)

producto33 = Producto("Esponja", 5000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 0.5)
producto34 = Producto("Esponja", 5000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 0.5)
producto35 = Producto("Esponja", 5000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 0.5)

producto36 = Producto("Limpiador", 12000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 2.0)
producto37 = Producto("Limpiador", 12000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 2.0)
producto38 = Producto("Limpiador", 12000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 2.0)

producto39 = Producto("Jabón Líquido", 10000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 1.5)
producto40 = Producto("Jabón Líquido", 10000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 1.5)
producto41 = Producto("Jabón Líquido", 10000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 1.5)

producto42 = Producto("Trapeador", 25000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 0.8)
producto43 = Producto("Trapeador", 25000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 0.8)
producto44 = Producto("Trapeador", 25000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 0.8)

producto45 = Producto("Cloro", 8000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 2.0)
producto46 = Producto("Cloro", 8000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 2.0)
producto47 = Producto("Cloro", 8000, EstadosProducto.DISPONIBLE, "Limpieza", "Aseo", 2.0)

# Listas de productos por tienda
lista_productos_tienda1 = [
    producto1, producto2, producto3, producto4, producto5,  # Cemento Gris
    producto6, producto7,  # Cemento Blanco
    producto8, producto9,  # Adhesivo Cerámico
    producto10, producto11  # Pintura Interior
]

lista_productos_tienda2 = [
    producto12, producto13, producto14,  # Sillas
    producto15, producto16, producto17,  # Mesas
    producto18, producto19, producto20,  # Sofa
    producto21, producto22, producto23,  # Mesa de noche
    producto24, producto25, producto26,  # Cama
    producto27, producto28, producto29   # Escritorio
]

lista_productos_tienda3 = [
    producto30, producto31, producto32,  # Detergente
    producto33, producto34, producto35,  # Esponja
    producto36, producto37, producto38,  # Limpiador
    producto39, producto40, producto41,  # Jabón Líquido
    producto42, producto43, producto44,  # Trapeador
    producto45, producto46, producto47   # Cloro
]

# Agregar productos a las tiendas
tienda1.getListaProducto().extend(lista_productos_tienda1)
tienda2.getListaProducto().extend(lista_productos_tienda2)
tienda3.getListaProducto().extend(lista_productos_tienda3)
# Crear cuenta bancaria para el operario
cuentaOperario = CuentaBancaria(55555, 100000)

# Crear operario
operario1 = Operario("Jaime", 97890, 20, cuentaOperario, None)

catalogo = [
    producto1, producto6, producto8, producto10, producto12, producto15, 
    producto18, producto21, producto24, producto27, producto30, 
    producto33, producto36, producto39, producto42, producto45
]

listaTiendas = [tienda1, tienda2, tienda3]

# Crear fábrica
fabrica = Fabrica("F001", "Fábrica Principal", "Calle Principal 123", cuentaFabrica, catalogo, operario1)

# Crear cuentas bancarias para los conductores
cuentaConductor1 = CuentaBancaria(12345, 5000)
cuentaConductor2 = CuentaBancaria(23456, 6000)
cuentaConductor3 = CuentaBancaria(34567, 7000)
cuentaConductor4 = CuentaBancaria(45678, 8000)
cuentaConductor5 = CuentaBancaria(56789, 9000)
cuentaConductor6 = CuentaBancaria(67890, 10000)
cuentaConductor7 = CuentaBancaria(78901, 11000)
cuentaConductor8 = CuentaBancaria(89012, 12000)
cuentaConductor9 = CuentaBancaria(90123, 13000)
cuentaConductor10 = CuentaBancaria(123456, 14000)
# Crear transportes
transporte1 = Transporte(TipoTransporte.CAMION, 15000, 16329)
transporte2 = Transporte(TipoTransporte.AVION, 30000, 64000)
transporte3 = Transporte(TipoTransporte.AUTOMOVIL, 9000, 500)
transporte4 = Transporte(TipoTransporte.CAMIONETA, 12000, 650)
transporte5 = Transporte(TipoTransporte.BICICLETA, 5000, 35)
transporte6 = Transporte(TipoTransporte.PATINES, 3000, 20)
transporte7 = Transporte(TipoTransporte.BARCO, 20000, 3356835)
transporte8 = Transporte(TipoTransporte.HELICOPTERO, 70000, 29000)
transporte9 = Transporte(TipoTransporte.TREN, 20000, 30000)
transporte10 = Transporte(TipoTransporte.CAMINANDO, 5000, 15)

# Crear conductores
conductor1 = Conductor("Julian Lopez", 19658, 30, cuentaConductor1, fabrica, transporte1)
conductor2 = Conductor("Oscar Rodriguez", 27932, 31, cuentaConductor2, fabrica, transporte2)
conductor3 = Conductor("Pablo Estrada", 37431, 32, cuentaConductor3, fabrica, transporte3)
conductor4 = Conductor("Camilo Henriquez", 4496, 33, cuentaConductor4, fabrica, transporte4)
conductor5 = Conductor("Juan Zamora", 55865, 34, cuentaConductor5, fabrica, transporte5)
conductor6 = Conductor("Miguel Zuluaga", 69636, 35, cuentaConductor6, fabrica, transporte6)
conductor7 = Conductor("Juan Herrera", 76970, 36, cuentaConductor7, fabrica, transporte7)
conductor8 = Conductor("Adres Guerra", 80497, 37, cuentaConductor8, fabrica, transporte8)
conductor9 = Conductor("Yhan Jaramillo", 93049, 38, cuentaConductor9, fabrica, transporte9)
conductor10 = Conductor("Jose Sanchez", 10101, 39, cuentaConductor10, fabrica, transporte10)

# Instancias estáticas de las metas para conductor
metaConductor1 = Meta("Facil", 30, 8000)
metaConductor2 = Meta("Normal", 50, 13500)
metaConductor3 = Meta("Dificil", 60, 21000)
metaConductor4 = Meta("Muy Dificil", 100, 28500)

# Instancias estáticas de las metas para operario
metaOperario1 = Meta("Facil", 5, 10000)
metaOperario2 = Meta("Normal", 10, 17000)
metaOperario3 = Meta("Dificil", 15, 25000)
metaOperario4 = Meta("Muy Dificil", 20, 35000)

# Instancias estáticas de las metas para Vendedor
metaVendedor1 = Meta("Facil", 5, 9000)
metaVendedor2 = Meta("Normal", 10, 15000)
metaVendedor3 = Meta("Dificil", 15, 22000)
metaVendedor4 = Meta("Muy Dificil", 20, 30000)

for i in Conductor.getListaConductores():
    i.setMetaConductor(metaConductor1)
    i.setMetaConductor(metaConductor2)
    i.setMetaConductor(metaConductor3)
    i.setMetaConductor(metaConductor4)


# Factura
fecha = datetime.date(2024, 10, 2)
fecha2 = datetime.date(2024, 10, 5)
fecha3 = datetime.date(2024, 10, 8)

#f1 = Factura(tienda1, cliente1, transporte1, listaProductosTienda1, transporte1.tipo_transporte.precio_envio, fecha)
#f2 = Factura(tienda2, csliente2, transporte2, listaProductosTienda2, transporte2.tipo_transporte.precio_envio, fecha2)
#f3 = Factura(tienda2, cliente1, transporte3, listaProductosTienda3, transporte3.tipo_transporte.precio_envio, fecha3)
operario1.setMetaOperario(metaOperario1)
operario1.setMetaOperario(metaOperario2)
operario1.setMetaOperario(metaOperario3)
operario1.setMetaOperario(metaOperario4)

for i in Conductor.getListaConductores():
    i.setMetaConductor(metaConductor1)
    i.setMetaConductor(metaConductor2)
    i.setMetaConductor(metaConductor3)
    i.setMetaConductor(metaConductor4)

for i in Vendedor.getListaVendedores():
    i.setMetaVendedor(metaVendedor1)
    i.setMetaVendedor(metaVendedor2)
    i.setMetaVendedor(metaVendedor3)
    i.setMetaVendedor(metaVendedor4)

vendedor1.setCantidadTrabajo(3)
vendedor2.setCantidadTrabajo(6)
vendedor3.setCantidadTrabajo(11)
vendedor1.setIndiceMeta(3)
vendedor2.setIndiceMeta(6)
vendedor3.setIndiceMeta(11)

operario1.setCantidadTrabajo(7)
operario1.setIndiceMeta(7)

conductor1.setCantidadTrabajo(8)
conductor1.setIndiceMeta(37)

conductor2.setCantidadTrabajo(12)
conductor2.setIndiceMeta(45)

conductor3.setCantidadTrabajo(5)
conductor3.setIndiceMeta(58)

conductor4.setCantidadTrabajo(0)
conductor4.setIndiceMeta(0)

conductor5.setCantidadTrabajo(9)
conductor5.setIndiceMeta(28)

conductor6.setCantidadTrabajo(3)
conductor6.setIndiceMeta(47)

conductor7.setCantidadTrabajo(0)
conductor7.setIndiceMeta(0)

conductor8.setCantidadTrabajo(7)
conductor8.setIndiceMeta(69)

conductor9.setCantidadTrabajo(13)
conductor9.setIndiceMeta(50)

conductor10.setCantidadTrabajo(6)
conductor10.setIndiceMeta(18)
