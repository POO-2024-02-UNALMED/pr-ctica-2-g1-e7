# fabrica.py

from gestion.CuentaBancaria import CuentaBancaria
from gestion.Operario import Operario
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
