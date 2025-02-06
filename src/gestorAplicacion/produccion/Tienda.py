
class Tienda:
    numTiendas = 0

    def __init__(self, nombre=None, vendedor=None, cuentaBancaria=None,
                 capacidadMaximaMaterial=None, capacidadMaximaConsumible=None,
                 capacidadMaximaLimpieza=None):
        if (nombre is not None and vendedor is not None and cuentaBancaria is not None and 
            capacidadMaximaMaterial is not None and capacidadMaximaConsumible is not None and 
            capacidadMaximaLimpieza is not None):
            self.nombre = nombre
            self.vendedor = vendedor
            # Se asigna la tienda al vendedor (se asume que vendedor posee el método setTienda)
            self.vendedor.setTienda(self)
            self.cuentaBancaria = cuentaBancaria
            Tienda.numTiendas += 1
            self.listaProducto = []  # Cada tienda tiene su propia lista de productos
            self.productosPorCategoria = []  # Lista de [Producto, Categoria]
            self.categorias = []
            self.conteoCategorias = []  # Conteo de productos por categoría
            self.capacidadMaximaMaterial = capacidadMaximaMaterial
            self.capacidadMaximaConsumible = capacidadMaximaConsumible
            self.capacidadMaximaLimpieza = capacidadMaximaLimpieza
        else:
            # Constructor vacío
            pass
