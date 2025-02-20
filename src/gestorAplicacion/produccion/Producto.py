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
            self.__nombre = producto.__nombre
            self._precio = producto._precio  
            self.__tipo = producto.__tipo
            self.__categoria = producto.__categoria
            self.__peso = producto.__peso
            self.__cantidad = getattr(producto, "__cantidad", 0)
            self.__motivoDevolucion = producto.__motivoDevolucion
            self._devuelto = producto.__devuelto
            self.__id = Producto.totalCreados

        elif len(args) == 5:  # 🔹 Constructor con parámetros posicionales
            self.__nombre = args[0]
            self._precio = args[1]  
            self.__tipo = args[2]
            self.__categoria = args[3]
            self.__peso = args[4]
            self.__cantidad = 0
            self.__motivoDevolucion = None
            self._devuelto = False
            self._id = Producto.totalCreados

        elif kwargs:  # 🔹 Constructor con palabras clave
            try:
                self.__nombre = kwargs['nombre']
                self._precio = kwargs['precio']  
                self.__tipo = kwargs['tipo']
                self.__categoria = kwargs['categoria']
                self.__peso = kwargs['peso']
            except KeyError as e:
                raise ValueError(f"Falta el parámetro requerido: {e}")

            self.__cantidad = kwargs.get('cantidad', 0)
            self.__motivoDevolucion = None
            self._devuelto = False
            self.__id = Producto.totalCreados

        else:  # 🔹 Constructor vacío
            self._id = Producto.totalCreados

        # Agregar a la lista de productos y aumentar el contador total
        Producto.listaProductos.append(self)
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
    



    #getters
    def getNombre(self): 
        return self.__nombre
    
    def getPrecio(self):
        return self._precio  
    def getTipo(self): 
        return self.__tipo
    def getCategoria(self): 
        return self.__categoria
    def getPeso(self): 
        return self.__peso
    def getCantidad(self): 
        return self.__cantidad
    def getMotivoDevolucion(self): 
        return self.__motivoDevolucion
    def getDevuelto(self): 
        return self._devuelto
    def getId(self): 
        return self._id
    @classmethod
    def getMotivosDevolucion(cls): 
        return cls.motivosDevolucion

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self, precio):
        self._precio = precio
    def setTipo(self, tipo): 
        self.__tipo = tipo
    def setCategoria(self, categoria): 
        self.__categoria = categoria
    def setPeso(self, peso): 
        self.__peso = peso
    def setCantidad(self, cantidad): 
        self.__cantidad = cantidad
    def setMotivoDevolucion(self, motivo): 
        self.__motivoDevolucion = motivo
    def setDevuelto(self, devuelto): 
        self._devuelto = devuelto
    @classmethod
    def setMotivosDevolucion(cls,motivos): 
        cls.motivosDevolucion=motivos
