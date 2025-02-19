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
            self.__nombre = producto.__nombre
            self.__precio = producto.__precio
            self.__estado = producto.__estado
            self.__tipo = producto.__tipo
            self.__categoria = producto.__categoria
            self.__peso = producto.__peso
            self.__cantidad = getattr(producto, "__cantidad", 0)
            self.__motivoDevolucion = producto.__motivoDevolucion
            self.__devuelto = producto.__devuelto
            self.__id = Producto.totalCreados
            Producto.listaProductos.append(self)
            Producto.totalCreados += 1
        # Constructor con parámetros posicionales (6 argumentos)
        elif len(args) == 6:
            self.__nombre = args[0]
            self.__precio = args[1]
            self.__estado = args[2]  
            self.__tipo = args[3]
            self.__categoria = args[4]
            self.__peso = args[5]
            self.__cantidad = 0
            self.__motivoDevolucion = None
            self.__devuelto = False
            self.__id = Producto.totalCreados
            Producto.listaProductos.append(self)
            Producto.totalCreados += 1
        # Constructor con parámetros por palabra clave
        elif kwargs:
            try:
                self.__nombre = kwargs['nombre']
                self.__precio = kwargs['precio']
                self.__estado = kwargs['estado']
                self.__tipo = kwargs['tipo']
                self.__categoria = kwargs['categoria']
                self.__peso = kwargs['peso']
            except KeyError as e:
                raise ValueError(f"Falta el parámetro requerido: {e}")
            self.__cantidad = 0
            self.__motivoDevolucion = None
            self.__devuelto = False
            self.__id = Producto.totalCreados
            Producto.listaProductos.append(self)
            Producto.totalCreados += 1
        else:
            # Constructor vacío
            self.__id = Producto.totalCreados
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
    #getters
    def getNombre(self): 
        return self.__nombre
    def getPrecio(self): 
        return self.__precio
    def getEstado(self): 
        return self.__estado
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
        return self.__devuelto
    def getId(self): 
        return self.__id

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre
    def setPrecio(self, precio):
        self.__precio = precio
    def setEstado(self, estado): 
        self.__estado = estado
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
        self.__devuelto = devuelto