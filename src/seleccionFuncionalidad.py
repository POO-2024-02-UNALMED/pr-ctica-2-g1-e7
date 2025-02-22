import tkinter as tk
from tkinter import ttk, messagebox, Tk, Frame, ttk
from Admin import Admin 

class VentanaSecundaria(Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        # Configuración de la ventana
        self.geometry("800x600")
        self.title("Nombre de la Aplicación")
        self.pagina_actual=0

        # 🔹 ZONA 0 - Título de la aplicación
        self.frame_titulo = tk.Frame(self, relief="solid", bd=1)
        self.frame_titulo.pack(fill="x", padx=5, pady=5)

        self.titulo = tk.Label(self.frame_titulo, text="Nombre de la aplicación", font=("Arial", 14, "bold"))
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
        menu_procesos.add_command(label="Opción 3")
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
    
    #Funcionalidad de devoluciones: 
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
    


# Ejecutar la aplicación desde una ventana principal
if __name__ == "__main__":
    ventanaSecundaria=VentanaSecundaria()
    ventanaSecundaria.mainloop()