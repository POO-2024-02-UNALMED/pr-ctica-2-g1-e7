class Producto:
    _totalCreados = 0
    _listaProductos = []
    _motivosDevolucion = [
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
            self._nombre = producto._nombre
            self._precio = producto._precio
            self._estado = producto._estado
            self._tipo = producto._tipo
            self._categoria = producto._categoria
            self._peso = producto._peso
            self._cantidad = getattr(producto, "cantidad", 0)
            self._motivoDevolucion = producto._motivoDevolucion
            self._devuelto = producto._devuelto
            self._id = Producto._totalCreados
            Producto._listaProductos.append(self)
            Producto._totalCreados += 1
        # Constructor con parámetros posicionales (6 argumentos)
        elif len(args) == 6:
            self._nombre = args[0]
            self._precio = args[1]
            self._estado = args[2]  
            self._tipo = args[3]
            self._categoria = args[4]
            self._peso = args[5]
            self._cantidad = 0
            self._motivoDevolucion = None
            self._devuelto = False
            self._id = Producto._totalCreados
            Producto._listaProductos.append(self)
            Producto._totalCreados += 1
        # Constructor con parámetros por palabra clave
        elif kwargs:
            try:
                self._nombre = kwargs['nombre']
                self._precio = kwargs['precio']
                self._estado = kwargs['estado']
                self._tipo = kwargs['tipo']
                self._categoria = kwargs['categoria']
                self._peso = kwargs['peso']
            except KeyError as e:
                raise ValueError(f"Falta el parámetro requerido: {e}")
            self._cantidad = 0
            self._motivoDevolucion = None
            self._devuelto = False
            self._id = Producto._totalCreados
            Producto._listaProductos.append(self)
            Producto._totalCreados += 1
        else:
            # Constructor vacío
            self._id = Producto._totalCreados
            Producto._totalCreados += 1

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
    


    #getters: 
    def setMotivoDevolucion(self, motivoDevolucion): 
        self._motivoDevolucion=motivoDevolucion
    def getPrecio(self): 
        return self._precio
    
    def getNombre(self):
        return self._nombre
    
    def getEstado(self):
        return self._estado
    
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
    
    def getID(self):
        return self._id
    
    #setters:

    def setPrecio(self, precio):
        self._precio=precio

    def setNombre(self, nombre):
        self._nombre=nombre

    def setEstado(self, estado):
        self._estado=estado

    def setTipo(self, tipo):
        self._tipo=tipo

    def setCategoria(self, categoria):
        self._categoria=categoria

    def setPeso(self, peso):
        self._peso=peso

    def setCantidad(self, cantidad):
        self._cantidad=cantidad

    def setDevuelto(self, devuelto):
        self._devuelto=devuelto

    def __str__(self):
        return f"ID: {self._id} - Nombre: {self._nombre} - Precio: {self._precio} - Estado: {self._estado} - Tipo: {self._tipo} - Categoría: {self._categoria} - Peso: {self._peso} - Cantidad: {self._cantidad} - Devuelto: {self._devuelto}"