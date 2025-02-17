# fabrica.py

from Producto import Producto
from Tienda import Tienda

class Fabrica:
    # Variables de clase (similares a los atributos estáticos en Java)
    cuentaBancaria = None
    operario = None
    productosDisponibles = []
    listaTienda = []

    def __init__(self, idFabrica=None, nombre=None, direccion=None,
                 cuentaBancariaFabrica=None, productosDisponibles=None,
                 listaTienda=None, operario=None):
        if (idFabrica is not None and nombre is not None and direccion is not None and 
            cuentaBancariaFabrica is not None and productosDisponibles is not None and 
            listaTienda is not None and operario is not None):
            self.idFabrica = idFabrica
            self.nombre = nombre
            self.direccion = direccion
            Fabrica.cuentaBancaria = cuentaBancariaFabrica
            Fabrica.productosDisponibles = productosDisponibles
            Fabrica.listaTienda = listaTienda
            operario.setFabrica(self)
            Fabrica.operario = operario
        else:
            # Constructor vacío
            pass
    
    @staticmethod
    def descontarDineroCuenta(producto: Producto) -> float:
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de descontar el dinero de la cuenta bancaria de la fábrica cuando se realiza una devolución 
        y retorna el precio del producto que se va a devolver.
        """
        precio = producto.precio
        Fabrica.cuentaBancaria.setSaldo(Fabrica.cuentaBancaria.getSaldo() - precio)
        return precio
    
    @staticmethod
    def calcular_excedente(productos: list['Producto'], valor: float) -> float:
        """
        Funcionalidad: Devoluciones
        Método que calcula el excedente que debe pagar el cliente (si debe hacerlo) al realizar un cambio de productos.

        :param productos: Lista de productos seleccionados.
        :param valor: Valor máximo permitido para el cambio.
        :return: El monto del excedente que el cliente debe pagar, o 0 si no hay excedente.
        """
        subtotal = sum(producto.precio for producto in productos)
        if subtotal <= valor:
            return 0
        return subtotal - valor
    
    """Funcionalidad a la que pertenece: Abastecer tiendas
    Metodo que se encarga de mostrar las tiendas disponibles y los productos que tienen en stock"""
    def mostrar_tiendas(lista_tienda):
        if not lista_tienda:
            return "No hay tiendas disponibles."

        resultado = "Listado de Tiendas:\n"
        for i, tienda in enumerate(lista_tienda, start=1):
            resultado += f"{i}. {tienda.nombre}:\n"
            resultado += "  Productos actuales:\n"

            # Obtener los productos de la tienda y agregar indentación
            productos = tienda.cantidad_productos().split("\n")
            for producto in productos:
                resultado += f"    {producto}\n"

        return resultado
    # Método perteneciente a la funcionalidad enviarPedidos:
    # Verifica si hay tiendas registradas y, si es así, devuelve una lista numerada con sus nombres.
    # Si no hay tiendas, indica que no hay ninguna registrada.
    @staticmethod
    def mostrarTiendasSinProductos():
        if not Fabrica.listaTienda:
            return "No hay tiendas registradas."

        texto = ""
        for i, tienda in enumerate(Fabrica.listaTienda, start=1):
            texto += f"{i}. Tienda: {tienda.nombre}\n"

        return texto.strip()
#faltaria el mostrar tiendas pero sin mostrar los productos(Yhan pa jose luis)

    """Funcionalidad a la que pertenece: Abastecer tiendas
       Metodo que se encarga de mostrar los productos disponibles en la fábrica para generar. Hace uso del metodo de la interfaz IMostrarProductos"""
    def mostrarProductos():
        from gestion.IMostrarProductos import IMostrarProductos
        return IMostrarProductos.mostrarProductosLista(Fabrica.productosDisponibles)
    """ Funcionalidad a la que pertenece: Abastecer tiendas
        Metodo que se encarga de generar nuevos productos seleccionados del abastecimiento"""

    def cantidadProductos(producto, cantidad_a_enviar):
        productos_generados = []
        for _ in range(cantidad_a_enviar):
            productos_generados.append(Producto(producto.nombre, producto.peso, producto.precio, producto.categoria))
        return productos_generados
