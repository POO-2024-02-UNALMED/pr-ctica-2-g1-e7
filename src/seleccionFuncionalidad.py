import tkinter as tk
from tkinter import ttk, messagebox, Tk, Frame, ttk
from Admin import Admin 
from  baseDatos.Deserializarcion import cargar_datos
from  baseDatos.Serialización import guardar_datos
from gestorAplicacion.produccion.Producto import Producto

class VentanaSecundaria(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._pago_por_metas = 0
        cargar_datos()
        # Configuración de la ventana
        self.geometry("800x600")
        self.title("Distribuidora JJAYC")
        self.pagina_actual = 0
        # 🔹 ZONA 0 - Título de la aplicación
        self.frame_titulo = tk.Frame(self, relief="solid", bd=1)
        self.frame_titulo.pack(fill="x", padx=5, pady=5)

        self.titulo = tk.Label(self.frame_titulo, text="Distribuidora JJAYC", font=("Arial", 14, "bold"))
        self.titulo.pack(pady=5)

        # 🔹 ZONA 1 - Menú superior
        self.frame_menu = tk.Frame(self, relief="solid", bd=1)
        self.frame_menu.pack(fill="x", padx=5, pady=5)

        # Menú de opciones
        self.menubar = tk.Menu(self)

        # Menú Archivo
        menu_archivo = tk.Menu(self.menubar, tearoff=0)
        menu_archivo.add_command(label="Aplicación", command=self.mostrar_info_aplicacion)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.cerrarVentana)
        self.menubar.add_cascade(label="Archivo", menu=menu_archivo)

        # Menú Procesos y Consultas
        menu_procesos = tk.Menu(self.menubar, tearoff=0)
        menu_procesos.add_command(label="Envio de Pedidos", command=self.EnvioPedidos)
        menu_procesos.add_command(label="Gestor de devoluciones", command=self.devoluciones)
        menu_procesos.add_command(label="Pago a los Trabajadores", command=self.pagoTrabajadores)
        menu_procesos.add_command(label="Opción 4", command=self.mostrar_abastecimiento)
        menu_procesos.add_command(label="Estadísticas", command=self.mostrar_estadisticas)
        self.menubar.add_cascade(label="Procesos y Consultas", menu=menu_procesos)

        # Menú Ayuda
        menu_ayuda = tk.Menu(self.menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.mostrar_autores)
        self.menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        # Asignar menú a la ventana
        self.config(menu=self.menubar)

        # 🔹 ZONA 2 - Zona de interacción con el usuario
        self.frame_interaccion = tk.Frame(self, relief="solid", bd=1)
        self.frame_interaccion.pack(fill="both", expand=True, padx=10, pady=10)

        # 🔹 Botones de acción
        self.frame_botones = tk.Frame(self, relief="solid", bd=1)
        self.frame_botones.pack(fill="x", padx=10, pady=5)


        # Mostrar la interfaz principal
        self.mostrar_menu()

    # 🔹 Funciones de menú
    def mostrar_info_aplicacion(self):
        messagebox.showinfo("Aplicación", "Esta aplicación gestiona procesos y consultas del sistema.")

    def mostrar_autores(self):
        messagebox.showinfo("Acerca de", "Autores: Equipo de Desarrollo JJAYC")

    def cerrarVentana(self):
        from Admin import Admin
        Admin.volverVentanaInicio(self)

    # 🔹 Función para limpiar el frame de interacción antes de cargar otra interfaz
    def limpiar_frame_interaccion(self):
        for widget in self.frame_interaccion.winfo_children():
            widget.destroy()

    # 🔹 Función para mostrar la interfaz de abastecimiento dentro de frame_interaccion
    def mostrar_abastecimiento(self):
        self.limpiar_frame_interaccion()

        tk.Label(self.frame_interaccion, text="Interfaz de Abastecimiento", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.frame_interaccion, text="Seleccione la tienda:").pack()
        ttk.Combobox(self.frame_interaccion, values=["Tienda 1", "Tienda 2", "Tienda 3"]).pack()

        tk.Label(self.frame_interaccion, text="Seleccione los productos:").pack()
        ttk.Checkbutton(self.frame_interaccion, text="Producto A").pack()
        ttk.Checkbutton(self.frame_interaccion, text="Producto B").pack()
        ttk.Checkbutton(self.frame_interaccion, text="Producto C").pack()

        tk.Label(self.frame_interaccion, text="Cantidad:").pack()
        tk.Entry(self.frame_interaccion).pack()

        tk.Button(self.frame_interaccion, text="Confirmar Envío",
                  command=lambda: messagebox.showinfo("Éxito", "Abastecimiento confirmado")).pack(pady=10)
        tk.Button(self.frame_interaccion, text="Volver al Menú", command=self.mostrar_menu).pack()

    # Funcionalidad de devoluciones:
    def devoluciones(self):
        self.limpiar_frame_interaccion()
        self.titulo.config(text="Bienvenido al gestor de devoluciones")
        tk.Label(
            self.frame_interaccion,
            text="Desde este menú podrá gestionar reembolsos o cambios de los productos de los clientes",
            font=("Arial", 10)
        ).pack(pady=10)
        tk.Label(
            self.frame_interaccion,
            text="Seleccione el número de la factura a la que desea hacer la devolución",
            font=("Arial", 14)
        ).pack(pady=10)

        self.frameFacturas = tk.Frame(self.frame_interaccion)
        self.frameFacturas.pack()

        self.frameBotones = tk.Frame(self.frame_interaccion)
        self.frameBotones.pack(pady=10)

        # Botón "Atrás"
        self.botonAtras = tk.Button(self.frameBotones, text="Atrás", command=self.mostrarFacturasAtras)
        self.botonAtras.pack(side="left", padx=20)
        # Botón "Siguiente"
        self.botonSiguiente = tk.Button(self.frameBotones, text="Siguiente", command=self.mostrarFacturasSiguiente)
        self.botonSiguiente.pack(side="right", padx=20)

        self.mostrarFacturas()

        # Variable para almacenar el número de factura ingresado
        self.factura_seleccionada = tk.StringVar()
        tk.Label(
            self.frame_interaccion,
            text="Ingrese el número de la factura de la que quiere devolver el producto",
            font=("Arial", 12)
        ).pack(anchor="s")
        entry_factura = tk.Entry(self.frame_interaccion, textvariable=self.factura_seleccionada)
        entry_factura.pack()

        tk.Button(
            self.frame_interaccion,
            text="Seleccionar Factura",
            command=lambda: self.procesarFactura(self.factura_seleccionada.get())
        ).pack()

    def procesarFactura(self, num_factura):
        # Se delega en Admin la obtención de la factura
        factura = Admin.obtenerFactura(num_factura)
        if factura:
            Admin.facturaSeleccionada = factura  # Guardamos la factura en Admin
            self.mostrarProductosFactura(factura)

    def mostrarFacturas(self):
        # Limpia el frame de facturas y las repinta
        for widget in self.frameFacturas.winfo_children():
            widget.destroy()
        facturas = Admin.mostrarFacturas()
        tk.Label(self.frameFacturas, text="----------------------------").pack(anchor="n")
        for factura in facturas:
            tk.Label(self.frameFacturas, text=factura, font=("Arial", 12)).pack()
        tk.Label(self.frameFacturas, text="----------------------------").pack(anchor="s")

    def mostrarFacturasSiguiente(self):
        Admin.avanzarPagina()
        self.mostrarFacturas()

    def mostrarFacturasAtras(self):
        Admin.retrocederPagina()
        self.mostrarFacturas()

    def mostrarProductosFactura(self, factura):
        # Limpia solo el frame de interacción para mostrar los productos
        for widget in self.frame_interaccion.winfo_children():
            widget.destroy()

        # Se obtiene la lista de productos (se asume que factura.mostrarProductosFactura() retorna un string con saltos de línea)
        productos_str = factura.mostrarProductosFactura()
        productos = productos_str.split("\n")

        tk.Label(
            self.frame_interaccion,
            text="Selecciona el producto de la factura que deseas cambiar:",
            font=("Arial", 12)
        ).pack(pady=10)

        combobox = ttk.Combobox(self.frame_interaccion, values=productos, state="readonly")
        combobox.pack()
        listaProductos = factura.getListaProductos()

        tk.Button(
            self.frame_interaccion,
            text="Seleccionar Producto",
            command=lambda: self.seleccionarProducto(combobox, listaProductos)
        ).pack(pady=5)

    def seleccionarProducto(self, combobox, lista_objetos_productos):
        indice_seleccionado = combobox.current()
        if indice_seleccionado == -1:
            messagebox.showerror("Error", "Seleccione un producto válido.")
            return

        producto_seleccionado = lista_objetos_productos[indice_seleccionado]
        Admin.productoSeleccionado = producto_seleccionado
        self.mostrarMotivosDevolucion()

    def mostrarMotivosDevolucion(self):
        from gestorAplicacion.produccion.Producto import Producto
        motivos = Producto.getMotivosDevolucion()
        tk.Label(
            self.frame_interaccion,
            text="¿Por qué desea devolver el producto?",
            font=("Arial", 10)
        ).pack()
        self.comboboxMotivos = ttk.Combobox(self.frame_interaccion, values=motivos, width=50, state="readonly")
        self.comboboxMotivos.pack()

        tk.Button(
            self.frame_interaccion,
            text="Confirmar Motivo",
            command=lambda: self.verificarMotivo(self.comboboxMotivos.get())
        ).pack(pady=5)

    def verificarMotivo(self, motivoSeleccionado):
        if not motivoSeleccionado:
            messagebox.showerror("Error", "Seleccione un motivo válido.")
            return

        # Si el motivo es "otro motivo", se solicita que el usuario ingrese su descripción
        if motivoSeleccionado.lower() == "otro motivo":
            from fieldFrame import FieldFrame
            criterios = ["Ingrese su motivo"]
            self.fieldFrame = FieldFrame(self.frame_interaccion, "Criterio", criterios, "Valor")
            self.fieldFrame.pack(pady=10)
            tk.Button(
                self.frame_interaccion,
                text="Confirmar Motivo Personalizado",
                command=lambda: self.obtenerMotivoPersonalizado(self.fieldFrame)
            ).pack(pady=5)

        else:
            # Se delega la evaluación en Admin (la lógica de negocio) y se procede al reembolso
            accion=Admin.evaluarMotivo(motivoSeleccionado, self.frame_interaccion)
            if accion==0: 
                self.procesarReembolso(Admin.productoSeleccionado)
            else: 
                self.procesarCambio(Admin.productoSeleccionado)

    def obtenerMotivoPersonalizado(self, fieldFrame):
        motivoPersonalizado = fieldFrame.getValue("Ingrese su motivo")
        if not motivoPersonalizado.strip():
            messagebox.showerror("Error", "Debe ingresar un motivo válido.")
            return
        Admin.productoSeleccionado.setMotivoDevolucion(motivoPersonalizado)
        # Luego de ingresar el motivo personalizado se puede proceder al reembolso
        self.procesarCambio(Admin.productoSeleccionado)

    def procesarReembolso(self, producto):
        tk.Label(
            self.frame_interaccion,
            text="Por el motivo seleccionado se le hará el reembolso del dinero, el cual es de $" + str(producto.getPrecio()),
            font=("Arial", 12)
        ).pack()
        # Simula el proceso de transferencia con un retardo
        self.frame_interaccion.after(2000, lambda: self.mostrarTransferencia(producto))

    def mostrarTransferencia(self, producto):
        tk.Label(
            self.frame_interaccion,
            text="Transfiriendo el dinero...",
            font=("Arial", 12)
        ).pack()
        self.frame_interaccion.after(2000, lambda: self.finalizarReembolso(producto))

    def finalizarReembolso(self, producto):
        Admin.procesarReembolso()
        tk.Label(
            self.frame_interaccion,
            text="Transferencia exitosa. Su dinero ha sido reembolsado exitosamente.",
            font=("Arial", 14)
        ).pack()
        tk.Button(
            self.frame_interaccion,
            text="Oprima el botón si desea gestionar otra devolución",
            bg="Green",
            command=self.devoluciones
        ).pack(pady=10)
    
    def procesarCambio(self, producto):
        tk.Label(
            self.frame_interaccion,
            text=("Por el motivo seleccionado, se le hará el cambio del producto.\n"
                  "Si el producto que seleccione tiene un precio menor, puede agregar otro para completar el valor restante.\n"
                  "NO se le devolverá el dinero restante."),
            font=("Arial", 12)
        ).pack(pady=10)
        tk.Button(
            self.frame_interaccion,
            text="Continuar con el cambio",
            bg="red",
            command=self.mostrarProductosTienda
        ).pack(pady=10)
    def mostrarProductosTienda(self):
        self.limpiar_frame_interaccion()
        # Almacenar la tienda y el precio original para usar en otros métodos
        self.original_price = Admin.productoSeleccionado.getPrecio()
        tk.Label(
            self.frame_interaccion,
            text=f"El precio de su producto es: ${self.original_price}",
            font=("Arial", 12)
        ).pack(pady=10)
        self.tienda = Admin.facturaSeleccionada.getTienda()
        productosDisponibles = self.tienda.mostrarProductos(Admin.productoSeleccionado)
        
        # Agrupar productos disponibles (productos únicos y sus cantidades)
        self.productosUnicos = []
        self.frecuencias = []
        for p in productosDisponibles:
            encontrado = False
            for i, prod in enumerate(self.productosUnicos):
                if prod.getNombre() == p.getNombre():
                    self.frecuencias[i] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.productosUnicos.append(p)
                self.frecuencias.append(1)

        # Crear un frame para la sección de cambio
        self.frameCambio = tk.Frame(self.frame_interaccion)
        self.frameCambio.pack(pady=10)
        tk.Label(
            self.frameCambio,
            text="Productos disponibles para cambio:",
            font=("Arial", 12)
        ).pack(pady=5)

        # Combobox de mayor ancho para visualizar las opciones
        self.comboboxCambio = ttk.Combobox(self.frameCambio, state="readonly", width=80)
        opciones = []
        for i, prod in enumerate(self.productosUnicos):
            opciones.append(f"{i+1}. {prod.getNombre()} - Precio: ${prod.getPrecio()} - Cantidad: {self.frecuencias[i]}")
        self.comboboxCambio['values'] = opciones
        self.comboboxCambio.pack(pady=5)

        # Label para mostrar mensajes informativos o de error
        self.labelInfo = tk.Label(self.frameCambio, text="", font=("Arial", 12))
        self.labelInfo.pack(pady=5)

        # Botón para agregar el producto seleccionado al carrito
        self.btnAgregar = tk.Button(
            self.frameCambio,
            text="Agregar al carrito",
            command=self.agregarProductoCambio
        )
        self.btnAgregar.pack(pady=5)

        # Inicializar el carrito y el subtotal
        self.carrito = []
        self.subtotal = 0.0
        self.labelSubtotal = tk.Label(
            self.frameCambio,
            text=f"Subtotal actual: ${self.subtotal}",
            font=("Arial", 12)
        )
        self.labelSubtotal.pack(pady=5)

        # Botón para finalizar la selección manualmente (si el usuario decide no seguir agregando)
        self.btnFinalizar = tk.Button(
            self.frameCambio,
            text="Finalizar selección",
            command=self.finalizarCambio
        )
        self.btnFinalizar.pack(pady=10)

    def agregarProductoCambio(self):
        index = self.comboboxCambio.current()
        if index == -1:
            self.labelInfo.config(text="Seleccione un producto válido.", fg="red")
            return
        if self.frecuencias[index] == 0:
            self.labelInfo.config(text="Este producto ya no está disponible.", fg="red")
            return

        producto_seleccionado = self.productosUnicos[index]
        nuevo_subtotal = self.subtotal + producto_seleccionado.getPrecio()

        # Permitir agregar el producto, incluso si hace que el subtotal supere el precio original
        self.frecuencias[index] -= 1
        self.carrito.append(producto_seleccionado)
        self.subtotal = nuevo_subtotal
        self.labelSubtotal.config(text=f"Subtotal actual: ${self.subtotal}")
        self.labelInfo.config(text=f"Se agregó {producto_seleccionado.getNombre()} al carrito.", fg="green")

        # Actualizar las opciones del combobox con las nuevas cantidades
        nuevas_opciones = []
        for i, prod in enumerate(self.productosUnicos):
            nuevas_opciones.append(f"{i+1}. {prod.getNombre()} - Precio: ${prod.getPrecio()} - Cantidad: {self.frecuencias[i]}")
        self.comboboxCambio['values'] = nuevas_opciones

        # Si el subtotal alcanza o supera el precio original, se deshabilita la opción de agregar más y se muestra el resumen automáticamente
        if self.subtotal >= self.original_price:
            self.btnAgregar.config(state="disabled")
            self.labelInfo.config(text="El valor del carrito ha superado (o igualado) el precio original.", fg="green")
            # Se procede a confirmar el cambio automáticamente
            self.confirmarCambio()

    def finalizarCambio(self):
        # Este método se invoca si el usuario finaliza manualmente la selección
        if self.subtotal < self.original_price:
            self.labelInfo.config(
                text="El subtotal no supera el precio original. No se le devolverá la diferencia. ¿Desea confirmar el cambio?",
                fg="red"
            )
            # Mostrar un botón de confirmación para proceder a pesar de que no se alcance el precio
            self.btnConfirmarCambio = tk.Button(
                self.frameCambio,
                text="Confirmar cambio",
                command=self.confirmarCambio
            )
            self.btnConfirmarCambio.pack(pady=5)
        else:
            self.confirmarCambio()

    def confirmarCambio(self):
        from gestorAplicacion.produccion.Fabrica import Fabrica 
        # Calcular el excedente (si el carrito supera el precio original, se le cobrará la diferencia)
        excedente = Fabrica.calcularExcedente(self.carrito, self.original_price)
        # Delegar en Admin el procesamiento del cambio
        Admin.procesarCambioProducto(self.carrito, excedente)
        
        # Mostrar el resumen final del cambio en un label
        resumen = "----- Resumen final del cambio -----\n"
        resumen += f"Usted ha cambiado un {Admin.productoSeleccionado.getNombre()} por:\n"
        for p in self.carrito:
            resumen += f" - {p.getNombre()}: ${p.getPrecio()}\n"
        resumen += f"Total del carrito: ${self.subtotal}\nExcedente pagado: ${excedente}\n"
        resumen += "---------------------------------------"
        tk.Label(self.frame_interaccion, text=resumen, font=("Arial", 12), justify="left").pack(pady=10)
        
        # Botón para volver a seleccionar otra factura (como en el proceso de reembolso)
        tk.Button(
            self.frame_interaccion,
            text="Volver a seleccionar otra factura",
            command=self.devoluciones
        ).pack(pady=10)


    # 🔹 Funcionalidad de estadísticas (a implementar)
    def mostrar_estadisticas(self):
        self.limpiar_frame_interaccion()
        tk.Label(self.frame_interaccion, text="Interfaz de Estadísticas", font=("Arial", 14)).pack()
        tk.Label(self.frame_interaccion, text="Aquí se mostrarán las estadísticas del sistema").pack()


    # 🔹 Función para volver a la interfaz principal
    def mostrar_menu(self):
        self.limpiar_frame_interaccion()
        tk.Label(self.frame_interaccion, text="Descripción del proceso o consulta:", font=("Arial", 12)).pack(pady=5)

        frame_resultados = tk.Frame(self.frame_interaccion, relief="solid", bd=1)
        frame_resultados.pack(fill="both", expand=True, padx=5, pady=5)

        texto_resultados = tk.Text(frame_resultados, wrap="word", height=10)
        texto_resultados.pack(fill="both", expand=True, padx=5, pady=5)

    # 🔹 Funcionalidad de Pago de Trabajadores
    def pagoTrabajadores(self):
        self.limpiar_frame_interaccion()
        self.titulo.config(text="Bienvenido al gestor del pago de sus trabajadores")
        tk.Label(self.frame_interaccion, text="Desde este menú podrá gestionar el pago a todos sus trabajadores",
                 font=("Arial", 10)).pack(pady=10)
        tk.Label(self.frame_interaccion, text="Seleccione el tipo de trabajadores que desea pagarle",
                 font=("Arial", 14)).pack(pady=10)

        # Botones para seleccionar el tipo de trabajador
        self.frame_botones_trabajadores = tk.Frame(self.frame_interaccion)
        self.frame_botones_trabajadores.pack(pady=10)

        # Usamos Admin.obtenerListaTrabajadores para obtener las listas
        tk.Button(self.frame_botones_trabajadores, text="Operarios", 
                  command=lambda: self.mostrar_lista_trabajadores(Admin.obtenerListaTrabajadores(1)),
                  width=20, height=2).pack(side="left", padx=10)
        tk.Button(self.frame_botones_trabajadores, text="Conductores", 
                  command=lambda: self.mostrar_lista_trabajadores(Admin.obtenerListaTrabajadores(2)),
                  width=20, height=2).pack(side="left", padx=10)
        tk.Button(self.frame_botones_trabajadores, text="Vendedores", 
                  command=lambda: self.mostrar_lista_trabajadores(Admin.obtenerListaTrabajadores(3)),
                  width=20, height=2).pack(side="left", padx=10)

        # Botón para volver al menú principal
        tk.Button(self.frame_interaccion, text="Volver al Menú", command=self.mostrar_menu).pack(pady=10)


    def mostrar_lista_trabajadores(self, lista_trabajadores):
        """Muestra la lista de trabajadores disponibles para pagar."""
        self.limpiar_frame_interaccion()

        if not lista_trabajadores:
            tk.Label(self.frame_interaccion, text="No hay trabajadores de este tipo para pagar.", font=("Arial", 14)).pack(pady=20)
            tk.Button(self.frame_interaccion, text="Volver", command=self.pagoTrabajadores, width=20, height=2).pack(pady=10)
            return

        tk.Label(self.frame_interaccion, text="Seleccione un trabajador para pagar:", font=("Arial", 14)).pack(pady=20)

        for i, trabajador in enumerate(lista_trabajadores):
            # Usamos Admin.calcularPagoTrabajador para obtener el pago potencial
            pago_potencial = Admin.calcularPagoTrabajador(trabajador)
            tk.Button(self.frame_interaccion, 
                      text=f"{trabajador.getNombre()} - Trabajos: {trabajador.getCantidadTrabajo()} - Pago: {pago_potencial}",
                      command=lambda t=trabajador: self.seleccionar_trabajador(t), width=40, height=2).pack(pady=5)

        tk.Button(self.frame_interaccion, text="Volver", command=self.pagoTrabajadores, width=20, height=2).pack(pady=10)

    def seleccionar_trabajador(self, trabajador):
        """Muestra los detalles del trabajador seleccionado."""
        self.limpiar_frame_interaccion()

        # Usamos Admin.calcularPagoTrabajador para obtener el pago potencial
        pago_potencial = Admin.calcularPagoTrabajador(trabajador)

        tk.Label(self.frame_interaccion, text=f"Trabajador seleccionado: {trabajador.getNombre()}", font=("Arial", 14)).pack(pady=20)
        tk.Label(self.frame_interaccion, text=f"Pago potencial: {pago_potencial} por {trabajador.getCantidadTrabajo()} trabajos realizados.",
                font=("Arial", 12)).pack(pady=10)

        # Botón para revisar metas (solo si no hay metas cumplidas)
        if self._pago_por_metas == 0:
            tk.Button(self.frame_interaccion, text="Revisar Metas", 
                    command=lambda: self.mostrar_metas_trabajador(trabajador),
                    width=20, height=2).pack(pady=10)

        # Botón para realizar el pago
        tk.Button(self.frame_interaccion, text="Realizar Pago", 
                command=lambda: self.realizar_pago(trabajador, pago_potencial),
                width=20, height=2).pack(pady=10)

        # 🔹 Botón para volver (solo si no hay metas cumplidas)
        if self._pago_por_metas == 0:
            tk.Button(self.frame_interaccion, text="Volver", command=self.pagoTrabajadores, width=20, height=2).pack(pady=10)


    def mostrar_metas_trabajador(self, trabajador):
        """Muestra las metas del trabajador seleccionado."""
        self.limpiar_frame_interaccion()

        # Usamos Admin.revisarMetasTrabajador para obtener las metas no pagadas
        metas_no_pagas = [meta for meta in trabajador.getMeta() if not meta.getVerificador()]

        if not metas_no_pagas:
            tk.Label(self.frame_interaccion, text="El trabajador no tiene metas pendientes.", font=("Arial", 14)).pack(pady=20, fill="x", padx=10)
            tk.Button(self.frame_interaccion, text="Volver", command=lambda: self.seleccionar_trabajador(trabajador),
                    width=20, height=2).pack(pady=10)
            return

        # Título de las metas
        tk.Label(self.frame_interaccion, text="Metas del trabajador:", font=("Arial", 14)).pack(pady=10, fill="x", padx=10)

        # Crear un Canvas y un Scrollbar para hacer el contenido desplazable
        canvas = tk.Canvas(self.frame_interaccion)
        scrollbar = tk.Scrollbar(self.frame_interaccion, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        # Configurar el Canvas y el Scrollbar
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Empaquetar el Canvas y el Scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Configurar el grid en el frame desplazable
        scrollable_frame.grid_columnconfigure(0, weight=1)  # Centrar el contenido en la columna 0

        # Mostrar cada meta en el frame desplazable
        for i, meta in enumerate(metas_no_pagas):
            # Crear un Frame para cada meta
            frame_meta = tk.Frame(scrollable_frame, borderwidth=2, relief="groove")
            frame_meta.grid(row=i, column=0, pady=5, padx=10, sticky="ew")

            # Mostrar la información de la meta en un Label
            tk.Label(frame_meta, text=f"Meta {i + 1}: {str(meta)}", font=("Arial", 12), justify="left").pack(pady=5, padx=10, fill="x")

            # Botón para revisar la meta
            tk.Button(frame_meta, text="Revisar Meta", command=lambda m=meta: self.revisar_meta(trabajador, m),
                    width=20, height=1).pack(pady=5)

        # 🔹 Botón para proceder con el pago (si hay metas cumplidas)
        if self._pago_por_metas > 0:
            tk.Button(self.frame_interaccion, text="Proceder con el Pago", 
                    command=lambda: self.seleccionar_trabajador(trabajador),
                    width=20, height=2).pack(pady=10)

        # Botón para volver
        tk.Button(self.frame_interaccion, text="Volver", command=lambda: self.seleccionar_trabajador(trabajador),
                width=20, height=2).pack(pady=10)
        
    def revisar_meta(self, trabajador, meta):
        """Revisa si la meta seleccionada ha sido cumplida."""
        self.limpiar_frame_interaccion()

        # Crear un nuevo frame para mostrar la información de la meta
        frame_meta = tk.Frame(self.frame_interaccion, borderwidth=2, relief="groove")
        frame_meta.pack(pady=10, padx=10, fill="x")

        # Verificar si la meta ha sido cumplida
        if meta.cumpleMeta(trabajador.getCantidadTrabajo()):  # Usar el índice de trabajo del trabajador
            # Mostrar información de la meta cumplida
            tk.Label(frame_meta, text=f"Meta Cumplida: {str(meta)}", font=("Arial", 12), justify="left").pack(pady=5, padx=10, fill="x")
            tk.Label(frame_meta, text=f"Se ha añadido {meta.getPago()} al pago total.", font=("Arial", 12), justify="left").pack(pady=5, padx=10, fill="x")

            # Marcar la meta como cumplida
            meta.setVerificador(True)

            # Sumar el valor de la meta al pago por metas
            self._pago_por_metas += meta.getPago()  # Aquí se suma el valor de la meta

            # 🔹 No eliminar la meta de la lista, solo marcarla como cumplida

            # 🔹 Opciones después de cumplir una meta
            frame_opciones = tk.Frame(self.frame_interaccion)
            frame_opciones.pack(pady=10)

            # Botón para revisar otra meta
            tk.Button(frame_opciones, text="Revisar Otra Meta", 
                    command=lambda: self.mostrar_metas_trabajador(trabajador),
                    width=20, height=2).pack(side="left", padx=10)

            # Botón para proceder con el pago
            tk.Button(frame_opciones, text="Proceder con el Pago", 
                    command=lambda: self.seleccionar_trabajador(trabajador),
                    width=20, height=2).pack(side="left", padx=10)
        else:
            # Mostrar información de la meta no cumplida
            tk.Label(frame_meta, text=f"Meta No Cumplida: {str(meta)}", font=("Arial", 12), justify="left").pack(pady=5, padx=10, fill="x")
            tk.Label(frame_meta, text=meta.porcentajeCumplidos(trabajador.getCantidadTrabajo()), font=("Arial", 12), justify="left").pack(pady=5, padx=10, fill="x")

            # 🔹 Botón para volver a la lista de metas
            tk.Button(self.frame_interaccion, text="Volver a Metas", command=lambda: self.mostrar_metas_trabajador(trabajador),
                    width=20, height=2).pack(pady=10)
        
    def realizar_pago(self, trabajador, pago_potencial):
        """Realiza el pago al trabajador y muestra el comprobante."""
        # Sumar el pago por metas al pago total
        pago_total = pago_potencial + self._pago_por_metas

        # Realizar el pago
        Admin.realizarPago(trabajador, pago_total)

        # Limpiar el frame de interacción
        self.limpiar_frame_interaccion()

        # Mostrar el comprobante de pago
        tk.Label(self.frame_interaccion, text="COMPROBANTE DE PAGO", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.frame_interaccion, text=f"Trabajador: {trabajador.getNombre()}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_interaccion, text=f"Total pagado: {pago_total}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_interaccion, text=f"- {pago_potencial} por las veces trabajadas", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.frame_interaccion, text=f"- {self._pago_por_metas} por las metas cumplidas", font=("Arial", 12)).pack(pady=5)

        # 🔹 Reiniciar el valor de las metas cumplidas
        self._pago_por_metas = 0

        # Botón para volver al menú principal
        tk.Button(self.frame_interaccion, text="Volver al Menú Principal", command=self.mostrar_menu, width=20, height=2).pack(pady=20)
    
        
        tk.Button(self.frame_interaccion, text="Volver al Menú Principal", command=self.mostrar_menu, font=("Helvetica", 10)).pack(pady=10)
    def EnvioPedidos(self):
        self.limpiar_frame_interaccion()
        self.titulo.config(text="Bienvenido Al Gestor De Envio De Pedidos")
        tk.Label(
            self.frame_interaccion,
            text="Desde este menú podrá gestionar los Envios de Pedidos de los clientes",
            font=("Helvetica", 14, "bold")).pack(pady=10)
        
        self.seleccionar_cliente()

    def seleccionar_cliente(self):
        from gestorAplicacion.gestion.Cliente import Cliente
        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text="Seleccione al cliente que realizó el pedido:", font=("Helvetica", 12)).pack(pady=10)
        
        clientes = Cliente.listaClientes  # Tomamos la lista directamente
        if not clientes:
            tk.Label(self.frame_interaccion, text="No hay clientes registrados.", font=("Helvetica", 12)).pack(pady=10)
            return  # Salimos de la función si no hay clientes

        opciones = [f"{i+1}. {cliente.getNombre()}" for i, cliente in enumerate(clientes)]
        
        combobox = ttk.Combobox(self.frame_interaccion, values=opciones, state="readonly", font=("Helvetica", 10))
        combobox.pack(pady=5)
        
        self.boton_confirmar_cliente = tk.Button(self.frame_interaccion, text="Confirmar Cliente", command=lambda: self.confirmar_cliente(combobox, clientes), font=("Helvetica", 10))
        self.boton_confirmar_cliente.pack(pady=10)

    def confirmar_cliente(self, combobox, clientes):
        seleccion = combobox.current()
        if seleccion == -1:
            messagebox.showerror("Error", "Seleccione un cliente válido.")
            return
        
        self.clienteSeleccionado = clientes[seleccion]
        self.boton_confirmar_cliente.pack_forget()
        combobox.config(state="disabled")
        self.seleccionar_tienda()

    def seleccionar_tienda(self):
        from gestorAplicacion.produccion.Fabrica import Fabrica
        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text="Seleccione la tienda desde la cual se enviará el pedido:", font=("Helvetica", 12)).pack(pady=10)
        
        tiendas = Fabrica.getListaTienda()
        opciones = [f"{i+1}. {tienda.getNombre()}" for i, tienda in enumerate(tiendas)]
        combobox = ttk.Combobox(self.frame_interaccion, values=opciones, state="readonly", font=("Helvetica", 10))
        combobox.pack(pady=5)
        
        self.boton_confirmar_tienda = tk.Button(self.frame_interaccion, text="Confirmar Tienda", command=lambda: self.confirmar_tienda(combobox, tiendas), font=("Helvetica", 10))
        self.boton_confirmar_tienda.pack(pady=10)

    def confirmar_tienda(self, combobox, tiendas):
        seleccion = combobox.current()
        if seleccion == -1:
            messagebox.showerror("Error", "Seleccione una tienda válida.")
            return
        
        self.tiendaSeleccionada = tiendas[seleccion]
        self.boton_confirmar_tienda.pack_forget()
        combobox.config(state="disabled")
        self.seleccionar_cantidad_productos()

    def seleccionar_cantidad_productos(self):
        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text="Indique la cantidad de productos que desea enviar (máximo 5):", font=("Helvetica", 12)).pack(pady=10)
        
        self.cantidadProductosSeleccionados = tk.IntVar()
        spinbox = tk.Spinbox(self.frame_interaccion, from_=1, to=5, textvariable=self.cantidadProductosSeleccionados, font=("Helvetica", 10))
        spinbox.pack(pady=5)
        
        self.boton_confirmar_cantidad = tk.Button(self.frame_interaccion, text="Confirmar Cantidad", command=self.confirmar_cantidad_productos, font=("Helvetica", 10))
        self.boton_confirmar_cantidad.pack(pady=10)

    def confirmar_cantidad_productos(self):
        cantidad = self.cantidadProductosSeleccionados.get()
        if cantidad < 1 or cantidad > 5:
            messagebox.showerror("Error", "Seleccione una cantidad válida.")
            return
        
        self.listaProductosPedidos = []
        self.listaProductosTienda = self.tiendaSeleccionada.listaProductosTienda()
        self.boton_confirmar_cantidad.pack_forget()
        self.seleccionar_productos(0)

    def seleccionar_productos(self, indice):
        if indice >= self.cantidadProductosSeleccionados.get():
            self.seleccionar_transporte()
            return
        
        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text=f"Seleccione el producto {indice + 1}:", font=("Helvetica", 12)).pack(pady=10)
        
        productos = [f"{i+1}. {producto[0].getNombre()} - Cantidad: {producto[1]}" for i, producto in enumerate(self.listaProductosTienda)]
        combobox = ttk.Combobox(self.frame_interaccion, values=productos, state="readonly", font=("Helvetica", 10))
        combobox.pack(pady=5)
        
        self.boton_confirmar_producto = tk.Button(self.frame_interaccion, text="Confirmar Producto", command=lambda: self.confirmar_producto(combobox, indice), font=("Helvetica", 10))
        self.boton_confirmar_producto.pack(pady=10)

    def confirmar_producto(self, combobox, indice):
        seleccion = combobox.current()
        if seleccion == -1:
            messagebox.showerror("Error", "Seleccione un producto válido.")
            return
        
        productoSeleccionado = self.listaProductosTienda[seleccion][0]
        cantidadProducto = self.listaProductosTienda[seleccion][1]
        
        if cantidadProducto <= 0:
            messagebox.showerror("Error", "El producto seleccionado ya no tiene stock disponible.")
            self.seleccionar_productos(indice)
            return
        
        self.listaProductosPedidos.append(productoSeleccionado)
        self.listaProductosTienda[seleccion][1] -= 1
        self.boton_confirmar_producto.pack_forget()
        combobox.config(state="disabled")
        self.seleccionar_productos(indice + 1)

    def seleccionar_transporte(self):
        from gestorAplicacion.produccion.Transporte import Transporte
        from gestorAplicacion.produccion.TipoTransporte import TipoTransporte
        from gestorAplicacion.gestion.Conductor import Conductor

        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text="Seleccione el transporte para el envío:", font=("Helvetica", 12)).pack(pady=10)
        
        totalPeso = sum([producto.getPeso() for producto in self.listaProductosPedidos])
        listaPosibleTransporte = TipoTransporte.crearTipoTransporteSegunCarga(totalPeso)
        listaTransporteFiltrada = [conductor.getTransporte() for conductor in Conductor.getListaConductores() if conductor.getTransporte().getTipoTransporte() in listaPosibleTransporte]
        
        envioGratis = Transporte.enviarGratis(self.listaProductosPedidos)
        
        transportes = [f"{i+1}. {transporte.getTipoTransporte().getNombre()} - Precio: {'0.0' if envioGratis else transporte.getPrecioEnvio()}" for i, transporte in enumerate(listaTransporteFiltrada)]
        combobox = ttk.Combobox(self.frame_interaccion, values=transportes, state="readonly", font=("Helvetica", 10))
        combobox.pack(pady=5)
        
        self.boton_confirmar_transporte = tk.Button(self.frame_interaccion, text="Confirmar Transporte", command=lambda: self.confirmar_transporte(combobox, listaTransporteFiltrada, envioGratis), font=("Helvetica", 10))
        self.boton_confirmar_transporte.pack(pady=10)

    def confirmar_transporte(self, combobox, listaTransporteFiltrada, envioGratis):
        seleccion = combobox.current()
        if seleccion == -1:
            messagebox.showerror("Error", "Seleccione un transporte válido.")
            return
        
        self.transporteSeleccionado = listaTransporteFiltrada[seleccion]
        self.precioEnvio = 0.0 if envioGratis else self.transporteSeleccionado.getPrecioEnvio()
        self.boton_confirmar_transporte.pack_forget()
        combobox.config(state="disabled")
        self.ingresar_fecha()

    def ingresar_fecha(self):
        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text="Ingrese la fecha de la venta (formato: DD/MM/AAAA):", font=("Helvetica", 12)).pack(pady=10)
        
        self.fechaVenta = tk.StringVar()
        entry_fecha = tk.Entry(self.frame_interaccion, textvariable=self.fechaVenta, font=("Helvetica", 10))
        entry_fecha.pack(pady=5)
        
        self.boton_confirmar_fecha = tk.Button(self.frame_interaccion, text="Confirmar Fecha", command=self.confirmar_fecha, font=("Helvetica", 10))
        self.boton_confirmar_fecha.pack(pady=10)

    def confirmar_fecha(self):
        import datetime
        formatoFecha = "%d/%m/%Y"
        try:
            self.fechaVenta = datetime.datetime.strptime(self.fechaVenta.get(), formatoFecha)
            self.boton_confirmar_fecha.pack_forget()
            self.generar_factura()
        except ValueError:
            messagebox.showerror("Error", "La fecha ingresada no es válida o no cumple con el formato DD/MM/AAAA.")
            self.ingresar_fecha()

    def formatear_factura(self, factura, tree):
        totalPrecio = 0
        totalPeso = 0
        precioEnvio = factura.getPrecioEnvio()

        # Añadir los productos al Treeview
        for producto in factura.getListaProductos():
            if producto is not None:
                tree.insert("", "end", values=(producto.getNombre(), f"${producto.getPrecio():.2f}", f"{producto.getPeso():.2f}"))
                totalPrecio += producto.getPrecio()
                totalPeso += producto.getPeso()

        # Añadir el envío y los totales al Treeview
        tree.insert("", "end", values=("Envío", f"${precioEnvio:.2f}", "N/A"))
        totalPrecio += precioEnvio
        tree.insert("", "end", values=("Total", f"${totalPrecio:.2f}", f"{totalPeso:.2f}"))

    def generar_factura(self):
        self.verificar_espacio()
        tk.Label(self.frame_interaccion, text="Generando Factura...", font=("Helvetica", 12)).pack(pady=10)
        
        factura = self.tiendaSeleccionada.enviarPedido(self.listaProductosPedidos, self.transporteSeleccionado, self.clienteSeleccionado, self.precioEnvio, self.fechaVenta)
        
        tk.Label(self.frame_interaccion, text="¡Factura creada con éxito! A continuación, se mostrará la factura:", font=("Helvetica", 12)).pack(pady=10)
        
        # Añadir el nombre de la tienda centrado en la parte superior
        tk.Label(self.frame_interaccion, text=factura.getTienda().getNombre(), font=("Helvetica", 14, "bold")).pack(pady=10)
        
        # Crear un Treeview widget para mostrar los detalles de la factura
        columns_detalles = ("Campo", "Valor")
        tree_detalles = ttk.Treeview(self.frame_interaccion, columns=columns_detalles, show="headings", height=5)
        tree_detalles.heading("Campo", text="Campo")
        tree_detalles.heading("Valor", text="Valor")
        tree_detalles.pack(pady=10)
        
        # Añadir detalles de la factura
        detalles = [
            ("Cliente", factura.getCliente().getNombre()),
            ("Cédula", factura.getCliente().getCedula()),
            ("Fecha", factura.getFecha().strftime('%Y-%m-%d')),
            ("Transporte", factura.getTransporte().getTipoTransporte().getNombre())
        ]
        for detalle in detalles:
            tree_detalles.insert("", "end", values=detalle)
        
        # Crear un Treeview widget para mostrar los productos de la factura
        columns_productos = ("Producto", "Precio", "Peso (kg)")
        tree_productos = ttk.Treeview(self.frame_interaccion, columns=columns_productos, show="headings", height=15)
        tree_productos.heading("Producto", text="Producto")
        tree_productos.heading("Precio", text="Precio")
        tree_productos.heading("Peso (kg)", text="Peso (kg)")
        tree_productos.pack(pady=10)
        
        # Formatear la factura
        self.formatear_factura(factura, tree_productos)
        
        self.tiendaSeleccionada.getVendedor().aumentarCargaTrabajo()
        self.transporteSeleccionado.getConductor().aumentarCargaTrabajo()
        self.tiendaSeleccionada.getVendedor().aumentarIndiceMeta()
        self.transporteSeleccionado.getConductor().aumentarIndiceMeta(sum([producto.getPeso() for producto in self.listaProductosPedidos]))
        self.tiendaSeleccionada.eliminarProductosPorNombre(self.listaProductosPedidos)
        guardar_datos()
        
        tk.Button(self.frame_interaccion, text="Volver al Menú Principal", command=self.mostrar_menu, font=("Helvetica", 10)).pack(pady=10)

    def formatear_factura(self, factura, tree):
        totalPrecio = 0
        totalPeso = 0
        precioEnvio = factura.getPrecioEnvio()

        # Añadir los productos al Treeview
        for producto in factura.getListaProductos():
            if producto is not None:
                tree.insert("", "end", values=(producto.getNombre(), f"${producto.getPrecio():.2f}", f"{producto.getPeso():.2f}"))
                totalPrecio += producto.getPrecio()
                totalPeso += producto.getPeso()

        # Añadir el envío y los totales al Treeview
        tree.insert("", "end", values=("Envío", f"${precioEnvio:.2f}", "N/A"))
        totalPrecio += precioEnvio
        tree.insert("", "end", values=("Total", f"${totalPrecio:.2f}", f"{totalPeso:.2f}"))
    def verificar_espacio(self):
        # Verificar si hay suficiente espacio en el frame_interaccion
        if len(self.frame_interaccion.winfo_children()) > 10:  # Ajustar el número según sea necesario
            self.limpiar_frame_interaccion()
# Ejecutar la aplicación desde una ventana principal
if __name__ == "__main__":
    
    ventanaSecundaria = VentanaSecundaria()
    ventanaSecundaria.mainloop()