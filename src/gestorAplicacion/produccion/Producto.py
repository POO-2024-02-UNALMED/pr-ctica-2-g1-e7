from EstadoProducto import EstadosProducto

class Producto:
    totalCreados = 0
    listaProductos = []
    motivosDevolucion = [
        "No llego a tiempo",
        "Llego en mal estado",
        "Se envio el producto equivocado",
        "El cliente cambió de opinión con la compra",
        "El producto no era lo que esperaba",
        "Otro motivo"
    ]

    def __init__(self, *args, **kwargs):
        """
        Se pueden utilizar tres formas de construcción:
          1. Constructor posicional: 
             Producto(nombre, precio, estado, tipo, categoria, peso)
          2. Constructor con palabras clave.
          3. Constructor de copia: Producto(otro_producto) donde otro_producto es una instancia de Producto.
          4. Constructor vacío: sin parámetros, solo incrementa el contador.
        """
        # Constructor de copia
        if len(args) == 1 and isinstance(args[0], Producto):
            producto = args[0]
            self.nombre = producto.nombre
            self.precio = producto.precio
            self.estado = producto.estado
            self.tipo = producto.tipo
            self.categoria = producto.categoria
            self.peso = producto.peso
            self.cantidad = getattr(producto, "cantidad", 0)
            self.motivoDevolucion = producto.motivoDevolucion
            self.devuelto = producto.devuelto
            self.id = Producto.totalCreados
            Producto.listaProductos.append(self)
            Producto.totalCreados += 1
        # Constructor con parámetros posicionales (6 argumentos)
        elif len(args) == 6:
            self.nombre = args[0]
            self.precio = args[1]
            self.estado = args[2]  
            self.tipo = args[3]
            self.categoria = args[4]
            self.peso = args[5]
            self.cantidad = 0
            self.motivoDevolucion = None
            self.devuelto = False
            self.id = Producto.totalCreados
            Producto.listaProductos.append(self)
            Producto.totalCreados += 1
        # Constructor con parámetros por palabra clave
        elif kwargs:
            try:
                self.nombre = kwargs['nombre']
                self.precio = kwargs['precio']
                self.estado = kwargs['estado']
                self.tipo = kwargs['tipo']
                self.categoria = kwargs['categoria']
                self.peso = kwargs['peso']
            except KeyError as e:
                raise ValueError(f"Falta el parámetro requerido: {e}")
            self.cantidad = 0
            self.motivoDevolucion = None
            self.devuelto = False
            self.id = Producto.totalCreados
            Producto.listaProductos.append(self)
            Producto.totalCreados += 1
        else:
            # Constructor vacío
            self.id = Producto.totalCreados
            Producto.totalCreados += 1

    @staticmethod
    def mostrarMotivosDeDevolucion() -> str:
        """
        Método que devuelve una lista de motivos de devolución en formato enumerado.
        """
        return "\n".join(f"{i + 1}. {motivo}" for i, motivo in enumerate(Producto.motivosDevolucion))
     
    @staticmethod
    def obtenerMotivoDeDevolucion(index: int) -> str:
        """
        Método que devuelve un motivo de devolución basado en el índice proporcionado.
        """
        if index < 1 or index > len(Producto.motivosDevolucion):
            return "Motivo no válido."
        return Producto.motivosDevolucion[index - 1]
    


    #getters y setters: 
    def setMotivoDevolucion(self, motivoDevolucion): 
        self.motivoDevolucion=motivoDevolucion
    def getPrecio(self): 
        return self.precio