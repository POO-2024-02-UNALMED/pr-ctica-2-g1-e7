
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.gestion.Vendedor import Vendedor#prueba
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria#prueba

class Fabrica:
    # Atributos "privados" (convención con guion bajo)
    _cuentaBancaria = None
    _listaTienda = []
    _productosDisponibles = []

    # Getters y Setters para atributos privados (estáticos)
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
    def setListaTienda(listaTienda):
        Fabrica._listaTienda = listaTienda

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

        return [Producto(producto.nombre, producto.precio, producto.estado,
                         producto.tipo, producto.categoria, producto.peso)
                for _ in range(cantidad_a_enviar)]

cuentaBancaria1=CuentaBancaria(1001 , 10000)
mi_vendedor = Vendedor("Juan Pérez", 123456789, 30, cuentaBancaria1)
mi_tienda = Tienda(
    nombre="Supermercado La Estrella",
    vendedor=mi_vendedor,
    cuentaBancaria="9876543210",
    capacidadMaximaMaterial=100,
    capacidadMaximaConsumible=200,
    capacidadMaximaLimpieza=150
)

Fabrica.getListaTienda().append(mi_tienda)
from gestorAplicacion.produccion.Producto import Producto

producto1 = Producto("Laptop", 3000, "Nuevo", "Electrónica", 2.5)
producto2 = Producto("Laptop", 3000, "Nuevo", "Electrónica", 2.5)
producto3 = Producto("Teléfono", 1000, "Usado", "Electrónica", 0.3)
producto4 = Producto("Mesa", 500, "Nuevo", "Muebles", 20.0)
producto5 = Producto("Mesa", 500, "Nuevo", "Muebles", 20.0)
producto6 = Producto("Audífonos", 200, "Nuevo", "Electrónica", 0.2)
producto7 = Producto("Monitor", 400, "Nuevo", "Electrónica", 5.0)
producto8 = Producto("Monitor", 400, "Nuevo", "Electrónica", 5.0)


mi_tienda.agregarProducto(producto1)
mi_tienda.agregarProducto(producto2)
mi_tienda.agregarProducto(producto3)
mi_tienda.agregarProducto(producto4)
mi_tienda.agregarProducto(producto5)
mi_tienda.agregarProducto(producto6)
mi_tienda.agregarProducto(producto7)
mi_tienda.agregarProducto(producto8)
