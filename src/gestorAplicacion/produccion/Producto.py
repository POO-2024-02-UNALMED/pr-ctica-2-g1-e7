class Producto:
    totalCreados = 0
    listaProductos = []
    motivosDevolucion = [
        "No llegó a tiempo",
        "Llegó en mal estado",
        "Se envió el producto equivocado",
        "El cliente cambió de opinión con la compra",
        "El producto no era lo que esperaba",
        "Otro motivo"
    ]

    def __init__(self, *args, **kwargs):

        """
        Se pueden utilizar tres formas de construcción:
          1. Constructor posicional: 
             Producto(nombre, precio, tipo, categoria, peso)
          2. Constructor con palabras clave.
          3. Constructor de copia: Producto(otro_producto) donde otro_producto es una instancia de Producto.
          4. Constructor vacío: sin parámetros, solo incrementa el contador.
        """

        if len(args) == 1 and isinstance(args[0], Producto):  # 🔹 Constructor de copia
            producto = args[0]
            self._nombre = producto._nombre
            self._precio = producto._precio  
            self._tipo = producto._tipo
            self._categoria = producto._categoria
            self._peso = producto._peso
            self._cantidad = getattr(producto, "_cantidad", 0)
            self._motivoDevolucion = producto._motivoDevolucion
            self._devuelto = producto._devuelto
            self._id = Producto.totalCreados

        elif len(args) == 5:  # Constructor con parámetros posicionales
            self._nombre = args[0]
            self._precio = args[1]  
            self._tipo = args[2]
            self._categoria = args[3]
            self._peso = args[4]
            self._cantidad = 0
            self._motivoDevolucion = None
            self._devuelto = False
            self._id = Producto.totalCreados

        elif kwargs:  # Constructor con palabras clave
            try:
                self._nombre = kwargs['nombre']
                self._precio = kwargs['precio']
                self._tipo = kwargs['tipo']
                self._categoria = kwargs['categoria']
                self._peso = kwargs['peso']

            except KeyError as e:
                raise ValueError(f"Falta el parámetro requerido: {e}")

            self._cantidad = kwargs.get('cantidad', 0)
            self._motivoDevolucion = None
            self._devuelto = False
            self._id = Producto.totalCreados

        else:  # Constructor vacío
            self._id = Producto.totalCreados

        Producto.listaProductos.append(self)
        Producto.totalCreados += 1

    @staticmethod
    def mostrarMotivosDeDevolucion() -> str:
        return "\n".join(f"{i + 1}. {motivo}" for i, motivo in enumerate(Producto.motivosDevolucion))
     
    @staticmethod
    def obtenerMotivoDeDevolucion(index: int) -> str:
        if index < 1 or index > len(Producto.motivosDevolucion):
            return "Motivo no válido."
        return Producto.motivosDevolucion[index - 1]
    
    # Getters
    def getNombre(self): 
        return self._nombre
    def getPrecio(self):
        return self._precio  
    def getTipo(self): 
        return self._tipo
    def getCategoria(self): 
        return self._categoria
    def getPeso(self): 
        return self._peso
    def getCantidad(self): 
        return self._cantidad
    def getMotivoDevolucion(self): 
        return self._motivoDevolucion
    def getDevuelto(self): 
        return self._devuelto
    def getId(self): 
        return self._id
    @classmethod
    def getMotivosDevolucion(cls): 
        return cls.motivosDevolucion

    # Setters
    def setNombre(self, nombre):
        self._nombre = nombre
    def setPrecio(self, precio):
        self._precio = precio
    def setTipo(self, tipo): 
        self._tipo = tipo
    def setCategoria(self, categoria): 
        self._categoria = categoria
    def setPeso(self, peso): 
        self._peso = peso
    def setCantidad(self, cantidad): 
        self._cantidad = cantidad
    def setMotivoDevolucion(self, motivo): 
        self._motivoDevolucion = motivo
    def setDevuelto(self, devuelto): 
        self._devuelto = devuelto
    @classmethod
    def setMotivosDevolucion(cls, motivos): 
        cls.motivosDevolucion = motivos
