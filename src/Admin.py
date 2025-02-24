from tkinter import Tk, Label,messagebox, ttk, Button, Frame



from  baseDatos.Deserializarcion import cargar_datos
from  baseDatos.Serialización import guardar_datos
cargar_datos()
from tkinter import messagebox
from ventanaInicio import centrar_ventana

class Admin:
    from gestorAplicacion.gestion.Factura import Factura
    from gestorAplicacion.gestion.Meta import Meta
    from gestorAplicacion.produccion.Producto import Producto
    pagina_actual = 0
    productoSeleccionado:Producto=None
    facturaSeleccionada:Factura=None 

    @staticmethod
    def destruirVentanaPrincipal(ventanaPrincipal:Tk):
        from seleccionFuncionalidad import VentanaSecundaria
        ventanaPrincipal.destroy()
        nuevaVentana=VentanaSecundaria()
        centrar_ventana(nuevaVentana)


    @staticmethod
    def volverVentanaInicio(ventanaSecundaria:Tk):
        from ventanaInicio import VentanaInicio
        ventanaSecundaria.destroy()
        ventana_inicio=VentanaInicio()
        centrar_ventana(ventana_inicio)

    @staticmethod
    def salirDelSistema(): 
        pass #Este es el método que se encarga de serializar los objetos cuando se cierre el programa. Implementacion pendiente 
    @staticmethod
    def obtenerFacturas():
        from gestorAplicacion.gestion.Factura import Factura
        """Devuelve todas las facturas en una lista formateada."""
        facturas = []
        n = 1
        for factura in Factura.listaFacturas:
            facturas.append(f"{n}. {factura.getCliente().getNombre()} - Tienda: {factura.getTienda()} - ID: {factura.getID()}")
            n += 1
        return facturas

    @classmethod
    def mostrarFacturas(cls):
        """Devuelve un subconjunto de 10 facturas según la página actual."""
        facturas = cls.obtenerFacturas()
        inicio = cls.pagina_actual * 10
        fin = inicio + 10
        return facturas[inicio:fin]  # Devuelve solo las facturas de la página actual

    @classmethod
    def avanzarPagina(cls):
        """Avanza a la siguiente página si hay más facturas."""
        if (cls.pagina_actual + 1) * 10 < len(cls.obtenerFacturas()):
            cls.pagina_actual += 1

    @classmethod
    def retrocederPagina(cls):
        """Retrocede a la página anterior si no está en la primera."""
        if cls.pagina_actual > 0:
            cls.pagina_actual -= 1

    @staticmethod
    def obtenerFactura(num, frameInteraccion): 
        from gestorAplicacion.gestion.Factura import Factura
        try:
            num_factura = int(num)  # Convertir a entero
            factura = Factura.seleccionarFactura(num_factura)  # Obtener la factura 
            Admin.facturaSeleccionada=factura 
            Admin.mostrarProductosFactura(factura, frameInteraccion)  # Llamar a otro método para mostrar productos
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
        except IndexError:
            messagebox.showerror("Error", "Número de factura inválido.")

    @staticmethod
    def mostrarProductosFactura(factura:Factura, frameInteraccion):
        # Limpiar solo los widgets relacionados con productos (NO eliminar todo el frame)
        for widget in frameInteraccion.winfo_children():
                widget.destroy()

        # Obtener la lista de productos en formato de lista para el combobox
        productos = factura.mostrarProductosFactura().split("\n")

        # Crear y mostrar el combobox
        Label(frameInteraccion,text="Selecciona el producto de la factura que deseas cambiar: ",font=("Arial",12)).pack(pady=10)
        combobox = ttk.Combobox(frameInteraccion)
        combobox["values"] = productos
        combobox["state"] = "readonly"  
        combobox.pack()
        listaProductos=factura.getListaProductos()
         # 🔹 Botón para seleccionar el producto
        btnSeleccionarProducto = Button(frameInteraccion, text="Seleccionar Producto",
                                       command=lambda: Admin.obtenerProducto(combobox,listaProductos,frameInteraccion))
        btnSeleccionarProducto.pack(pady=5)

    @staticmethod
    def obtenerProducto(combobox, lista_objetos_productos, frameInteraccion):
        from seleccionFuncionalidad import VentanaSecundaria
        from gestorAplicacion.produccion.Producto import Producto

        """Obtiene el objeto seleccionado en el Combobox y lo almacena en una variable."""
        indice_seleccionado = combobox.current()  # Obtener el índice seleccionado
        if indice_seleccionado == -1:  # Si no se ha seleccionado nada
            messagebox.showerror("Error", "Seleccione un producto válido.")
            return

        # Obtener el objeto correspondiente al índice seleccionado
        producto_seleccionado:Producto = lista_objetos_productos[indice_seleccionado]
        Admin.productoSeleccionado = producto_seleccionado
        VentanaSecundaria.mostrarMotivosDevolucion(frameInteraccion)

    @staticmethod
    def evaluarMotivo(motivoDevolucion,frameInteraccion:Frame): 
        from gestorAplicacion.produccion.Producto import Producto
        from seleccionFuncionalidad import VentanaSecundaria
        motivos=Producto.getMotivosDevolucion()
        for widget in frameInteraccion.winfo_children(): 
            widget.destroy()
        if motivoDevolucion==motivos[0] or motivoDevolucion==motivos[1] or motivoDevolucion==motivos[2]: 
            VentanaSecundaria.procesarReembolso(Admin.productoSeleccionado,frameInteraccion)
    
    @classmethod
    def procesarReembolso(cls): 
        from gestorAplicacion.produccion.Tienda import Tienda 
        from gestorAplicacion.gestion.Cliente import Cliente
        from gestorAplicacion.produccion.Fabrica import Fabrica
        tienda:Tienda=Admin.facturaSeleccionada.getTienda()
        cliente: Cliente=tienda.devolverProducto(Admin.facturaSeleccionada,Admin.productoSeleccionado)
        valorADevolver = Fabrica.descontarDineroCuenta(Admin.productoSeleccionado)
        Fabrica.getCuentaBancaria().devolverDinero(valorADevolver, cliente)
        cliente.removerProducto(Admin.productoSeleccionado)
    

    # 🔹 Nuevos métodos para el pago de trabajadores
    @staticmethod
    def obtenerListaTrabajadores(tipo):
        from gestorAplicacion.gestion.Operario import Operario
        from gestorAplicacion.gestion.Vendedor import Vendedor
        from gestorAplicacion.gestion.Conductor import Conductor



        """
        Devuelve la lista de trabajadores según el tipo especificado.
        :param tipo: 1 para Operarios, 2 para Conductores, 3 para Vendedores.
        :return: Lista de trabajadores.
        """
        if tipo == 1:
            return Operario.getListaOperarios()
        elif tipo == 2:
            return Conductor.getListaConductores()
        elif tipo == 3:
            return Vendedor.getListaVendedores()
        else:
            return []

    @staticmethod
    def calcularPagoTrabajador(trabajador):
        """
        Calcula el pago potencial de un trabajador (salario base + pago por trabajo realizado).
        :param trabajador: El trabajador al que se le calculará el pago.
        :return: El pago potencial.
        """
        return trabajador.getCuentaBancaria().calcularPago(trabajador) + trabajador.getSalarioBase()

    @staticmethod
    def revisarMetasTrabajador(trabajador):
        """
        Devuelve las metas no pagadas de un trabajador.
        :param trabajador: El trabajador cuyas metas se revisarán.
        :return: Lista de metas no pagadas.
        """
        return [meta for meta in trabajador.getMeta() if not meta.getVerificador()]

    @staticmethod
    def cumplirMeta(trabajador, meta):
        """
        Marca una meta como cumplida y agrega el pago correspondiente.
        :param trabajador: El trabajador al que pertenece la meta.
        :param meta: La meta que se marcará como cumplida.
        :return: True si la meta fue cumplida, False en caso contrario.
        """
        if meta.cumpleMeta(trabajador.getIndiceMeta()):
            meta.setVerificador(True)
            return True
        return False

    @staticmethod
    def realizarPago(trabajador, pago_total):
        from gestorAplicacion.produccion.Fabrica import Fabrica

        """
        Realiza el pago al trabajador y actualiza la cuenta bancaria de la fábrica.
        :param trabajador: El trabajador al que se le realizará el pago.
        :param pago_total: El monto total a pagar.
        """
        Fabrica._cuentaBancaria.descontarDinero(pago_total)
        trabajador.recibirSueldo(pago_total)

