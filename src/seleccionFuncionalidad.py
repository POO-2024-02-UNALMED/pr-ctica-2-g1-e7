import tkinter as tk
from tkinter import ttk, messagebox, Tk, Frame, ttk
from Admin import Admin 
  
class VentanaSecundaria(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
        menu_procesos.add_command(label="Opción 1")
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

        self.boton_aceptar = tk.Button(self.frame_botones, text="Ejecutar Proceso")
        self.boton_aceptar.pack(side="left", padx=10, pady=5)

        self.boton_borrar = tk.Button(self.frame_botones, text="Limpiar")
        self.boton_borrar.pack(side="right", padx=10, pady=5)

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
        tk.Label(self.frame_interaccion,text="Desde este menú podrá gestionar reembolsos o cambios de los productos de los clientes",font=("Arial",10)).pack(pady=10)
        tk.Label(self.frame_interaccion,text="Seleccione el número de la factura a la que desea hacer la devolucion",font=("Arial", 14)).pack(pady=10)        
        self.frameFacturas = Frame(self.frame_interaccion)
        self.frameFacturas.pack()
        self.frameBotones = tk.Frame(self.frame_interaccion)
        self.frameBotones.pack(pady=10)
        # Botón "Atrás"
        self.botonAtras = tk.Button(self.frameBotones, text="Atrás", command=self.mostrarFacturasAtras)
        self.botonAtras.pack(side="left", padx=20)  # Separación entre botones

        # Botón "Siguiente"
        self.botonSiguiente = tk.Button(self.frameBotones, text="Siguiente", command=self.mostrarFacturasSiguiente)
        self.botonSiguiente.pack(side="right", padx=20)

        self.mostrarFacturas()

        self.factura_seleccionada = tk.StringVar()

        tk.Label(self.frame_interaccion, text="Ingrese el número de la factura de la que quiere devolver el producto",
                 font=("Arial", 12)).pack(anchor="s")

        # Campo de entrada asociado a la variable
        entry_factura = tk.Entry(self.frame_interaccion, textvariable=self.factura_seleccionada)
        entry_factura.pack()

        # Botón para procesar la factura seleccionada
        tk.Button(self.frame_interaccion, text="Seleccionar Factura", 
          command=lambda: Admin.obtenerFactura(self.factura_seleccionada.get(), self.frame_interaccion)).pack()
        

  
    def mostrarFacturas(self):
        """Obtiene las facturas desde Admin y las muestra en pantalla."""

        # Limpiar el frame antes de agregar nuevos elementos
        for widget in self.frameFacturas.winfo_children():
            widget.destroy()

        facturas = Admin.mostrarFacturas()

        # Agregar líneas antes y después de las facturas
        tk.Label(self.frameFacturas, text="----------------------------").pack(anchor="n")

        for factura in facturas:
            tk.Label(self.frameFacturas, text=factura, font=("Arial", 12)).pack()

        tk.Label(self.frameFacturas, text="----------------------------").pack(anchor="s")
    
  

    def mostrarFacturasSiguiente(self):
        """Maneja el avance de página."""
        Admin.avanzarPagina()
        self.mostrarFacturas()

    def mostrarFacturasAtras(self):
        """Maneja el retroceso de página."""
        Admin.retrocederPagina()
        self.mostrarFacturas()  

    @staticmethod
    def mostrarMotivosDevolucion(frameInteraccion):
        from gestorAplicacion.produccion.Producto import Producto
        motivos= Producto.getMotivosDevolucion()
        tk.Label(frameInteraccion,text="¿Por qué desea devolver el producto?",font=("Arial",10)).pack()
        motivos=ttk.Combobox(frameInteraccion,values=motivos,width=50,state="readonly").pack()
        

        


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

        # Botón para revisar metas
        tk.Button(self.frame_interaccion, text="Revisar Metas", 
                  command=lambda: self.mostrar_metas_trabajador(trabajador),
                  width=20, height=2).pack(pady=10)

        # Botón para realizar el pago
        tk.Button(self.frame_interaccion, text="Realizar Pago", 
                  command=lambda: self.realizar_pago(trabajador, pago_potencial),
                  width=20, height=2).pack(pady=10)

        # Botón para volver
        tk.Button(self.frame_interaccion, text="Volver", command=self.pagoTrabajadores, width=20, height=2).pack(pady=10)


    def mostrar_metas_trabajador(self, trabajador):
        """Muestra las metas del trabajador seleccionado."""
        self.limpiar_frame_interaccion()

        # Usamos Admin.revisarMetasTrabajador para obtener las metas no pagadas
        metas_no_pagas = Admin.revisarMetasTrabajador(trabajador)

        if not metas_no_pagas:
            tk.Label(self.frame_interaccion, text="El trabajador no tiene metas pendientes.", font=("Arial", 14)).pack(pady=20)
            tk.Button(self.frame_interaccion, text="Volver", command=lambda: self.seleccionar_trabajador(trabajador),
                      width=20, height=2).pack(pady=10)
            return

        tk.Label(self.frame_interaccion, text="Metas del trabajador:", font=("Arial", 14)).pack(pady=20)

        for i, meta in enumerate(metas_no_pagas):
            tk.Button(self.frame_interaccion, text=f"Meta {i + 1}: {meta.getDescripcion()} - Pago: {meta.getPago()}",
                      command=lambda m=meta: self.revisar_meta(trabajador, m), width=40, height=2).pack(pady=5)

        tk.Button(self.frame_interaccion, text="Volver", command=lambda: self.seleccionar_trabajador(trabajador),
                  width=20, height=2).pack(pady=10)

    def revisar_meta(self, trabajador, meta):
        """Revisa si la meta seleccionada ha sido cumplida."""
        # Usamos Admin.cumplirMeta para marcar la meta como cumplida
        if Admin.cumplirMeta(trabajador, meta):
            messagebox.showinfo("Meta Cumplida", f"La meta '{meta.getDescripcion()}' ha sido cumplida. Se ha añadido {meta.getPago()} al pago total.")
        else:
            messagebox.showinfo("Meta No Cumplida", f"La meta '{meta.getDescripcion()}' no ha sido cumplida.")

        self.mostrar_metas_trabajador(trabajador)

    def realizar_pago(self, trabajador, pago_potencial):
        """Realiza el pago al trabajador y muestra el comprobante."""
        # Usamos Admin.realizarPago para realizar el pago
        pago_por_metas = sum(meta.getPago() for meta in trabajador.getMeta() if meta.getVerificador())
        pago_total = pago_potencial + pago_por_metas

        Admin.realizarPago(trabajador, pago_total)

        self.limpiar_frame_interaccion()

        tk.Label(self.frame_interaccion, text="COMPROBANTE DE PAGO", font=("Arial", 16)).pack(pady=20)
        tk.Label(self.frame_interaccion, text=f"Trabajador: {trabajador.getNombre()}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_interaccion, text=f"Total pagado: {pago_total}", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.frame_interaccion, text=f"- {pago_potencial} por las veces trabajadas", font=("Arial", 12)).pack(pady=5)
        tk.Label(self.frame_interaccion, text=f"- {pago_por_metas} por las metas cumplidas", font=("Arial", 12)).pack(pady=5)

        tk.Button(self.frame_interaccion, text="Volver al Menú Principal", command=self.mostrar_menu, width=20, height=2).pack(pady=20)


# Ejecutar la aplicación desde una ventana principal
if __name__ == "__main__":
    ventanaSecundaria = VentanaSecundaria()
    ventanaSecundaria.mainloop()