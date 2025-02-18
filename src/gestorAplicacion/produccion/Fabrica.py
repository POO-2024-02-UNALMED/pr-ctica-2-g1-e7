from gestorAplicacion.produccion.Producto import Producto
from gestorAplicacion.produccion.Tienda import Tienda
from gestorAplicacion.gestion.Vendedor import Vendedor#prueba


class Fabrica:
    # Variables de clase
    cuentaBancaria = None
    operario = None
    productosDisponibles = []
    listaTienda = []

    def __init__(self, idFabrica=None, nombre=None, direccion=None,
                 cuentaBancariaFabrica=None, productosDisponibles=None,
                 listaTienda=None, operario=None):
        self.idFabrica = idFabrica
        self.nombre = nombre
        self.direccion = direccion

        if cuentaBancariaFabrica is not None:
            Fabrica.cuentaBancaria = cuentaBancariaFabrica
        if productosDisponibles is not None:
            Fabrica.productosDisponibles = productosDisponibles
        if listaTienda is not None:
            Fabrica.listaTienda = listaTienda
        if operario is not None:
            Fabrica.operario = operario
            operario.set_fabrica(self)

    @staticmethod
    def descontarDineroCuenta(producto) -> float:
        """
        Resta el precio del producto devuelto de la cuenta bancaria de la fábrica.
        """
        if Fabrica.cuentaBancaria is None:
            raise ValueError("Error: La fábrica no tiene una cuenta bancaria registrada.")
        
        if producto.precio is None:
            raise ValueError("Error: El producto no tiene un precio definido.")

        Fabrica.cuentaBancaria.setSaldo(Fabrica.cuentaBancaria.getSaldo() - producto.precio)
        return producto.precio

    @staticmethod
    def calcularExcedente(productos, valor: float) -> float:
        """
        Calcula si el cliente debe pagar un excedente al cambiar productos.
        """
        subtotal = sum(p.precio for p in productos if p.precio is not None)
        return max(0, subtotal - valor)

    @staticmethod
    def mostrar_tiendas():
        """
        Muestra las tiendas registradas y sus productos en stock.
        """
        if not Fabrica.listaTienda:
            return "No hay tiendas disponibles."

        resultado = "Listado de Tiendas:\n"
        for i, tienda in enumerate(Fabrica.listaTienda, start=1):
            resultado += f"{i}. {tienda.nombre}:\n"
            productos = tienda.cantidad_productos().split("\n")
            resultado += "\n".join(f"    {p}" for p in productos) + "\n"

        return resultado.strip()

    @staticmethod
    def mostrarTiendasSinProductos():
        """
        Muestra una lista numerada de las tiendas sin incluir los productos.
        """
        if not Fabrica.listaTienda:
            return "No hay tiendas registradas."

        return "\n".join(f"{i}. Tienda: {t.getNombre()}" for i, t in enumerate(Fabrica.listaTienda, start=1))

    @staticmethod
    def mostrarProductos():
        """
        Muestra los productos disponibles en la fábrica usando la interfaz IMostrarProductos.
        """
        from gestion.IMostrarProductos import IMostrarProductos
        return IMostrarProductos.mostrarProductosLista(Fabrica.productosDisponibles)

    @staticmethod
    def cantidadProductos(producto, cantidad_a_enviar: int):
        """
        Genera una cantidad específica de productos para abastecimiento.
        """
        from gestorAplicacion.produccion.Producto import Producto

        if not isinstance(producto, Producto):
            raise ValueError("Error: El objeto proporcionado no es un producto válido.")
        if cantidad_a_enviar <= 0:
            raise ValueError("Error: La cantidad a enviar debe ser mayor a 0.")

        return [Producto(producto.nombre, producto.precio, producto.estado, 
                         producto.tipo, producto.categoria, producto.peso) 
                for _ in range(cantidad_a_enviar)]
mi_vendedor = Vendedor("Juan Pérez", 123456789, 30, "1234567890")
mi_tienda = Tienda(
    nombre="Supermercado La Estrella",
    vendedor=mi_vendedor,
    cuentaBancaria="9876543210",
    capacidadMaximaMaterial=100,
    capacidadMaximaConsumible=200,
    capacidadMaximaLimpieza=150
)
Fabrica.listaTienda.append(mi_tienda)
