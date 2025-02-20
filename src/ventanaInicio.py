import tkinter as tk
from tkinter import messagebox, Tk

class VentanaInicio(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventanaSecundaria = None
        
        # Configuración de la ventana
        self.geometry("800x600")
        self.title("Ventana Principal")

        # Datos de los desarrolladores
        self.indiceDesarrollador = 0
        self.nombresDesarrolladores = ["Carlos", "Andres", "Juan", "Yhan", "Jose"]
        self.descripciones = [
            "Carlos Ernesto Galvis González \n19 años \nEstudiante de Ingeniería de Sistemas \nDeportista",
            "Andrés Felipe Guerra Amaris \n18 años \nIngeniería de sistemas e informática  \nNacido en Bucaramanga",
            "Juan Esteban Herrera Navarro \n22 años \nEstudiante ingeniería de sistemas \nTrabajador nato.",
            "Yhan Carlos Jaramillo Diaz \n17 años \nEstudiante de Ingeniería de Sistemas \nTrabajador",
            "Jose Luis Sanchez Alvarez \n18 años \nEstudiante de Ingenieria de Sistemas \nNacido en Uraba"
        ]
        self.fotosDesarrolladoresPaths = [
            "./imagenes/collageCarlos.png",
            "./imagenes/collageAndres.png",
            "./imagenes/collageJuan.png",
            "./imagenes/collageYhan.png",
            "./imagenes/collageJoseLuis.png"
        ]

        # Creación de la interfaz gráfica
        self.crearInterfaz()

    def crearInterfaz(self):
        """ Configura toda la interfaz gráfica. """

        # 🔹 Menú de opciones
        menubar = tk.Menu(self)
        menuArchivo = tk.Menu(menubar, tearoff=0)
        menuArchivo.add_command(label="Salir", command=self.quit)
        menuArchivo.add_command(label="Descripción del sistema",
                                 command=lambda: messagebox.showinfo("Acerca de", "Autores: Equipo de Desarrollo JJAYC"))
        menubar.add_cascade(label="Inicio", menu=menuArchivo)
        self.config(menu=menubar)

        # 🔹 Marcos principales
        frameDeArriba = tk.Frame(self)
        frameDeArriba.pack(fill="both", expand=True)
        frameDeAbajo = tk.Frame(self)
        frameDeAbajo.pack(fill="both", expand=True)

        # 🔹 P3 - Saludo
        p3Frame = tk.Frame(frameDeArriba, bg="lightgreen", width=200, height=100)
        p3Frame.pack(side="left", fill="both", expand=True)
        tk.Label(p3Frame, text="¡Bienvenido al sistema!\n\n Bienvenido al sistema de distribución JJAYC,\n"
                 "el sistema donde podrás manejar tu negocio,\n"
                 "pudiendo abastecer tiendas, enviar pedidos,\n"
                 "manejar devoluciones, pagar a tus trabajadores\n"
                 "y revisar las estadísticas de la empresa.", font=("Arial", 12, "bold")).pack()

        # 🔹 P5 - Hoja de Vida
        p5Frame = tk.Frame(frameDeArriba, bg="lightblue", width=200, height=100)
        p5Frame.pack(side="right", fill="both", expand=True)
        self.descripcionLabel = tk.Label(p5Frame, text=self.descripciones[self.indiceDesarrollador], font=("Arial", 10))
        self.descripcionLabel.pack()
        self.descripcionLabel.bind("<Button-1>", lambda e: self.cambiarDesarrollador())

        # 🔹 P4 - Imagen del sistema
        p4Frame = tk.Frame(frameDeAbajo, bg="gray")
        p4Frame.pack(side="left", fill="both", expand=True)

        self.fotoNegocio = tk.PhotoImage(file="./imagenes/fotosDistribuidora.png")
        imagen = self.fotoNegocio.subsample(2, 2)
        fotoLabel = tk.Label(p4Frame, image=imagen)
        fotoLabel.image = imagen
        fotoLabel.pack(expand=True)

        # 🔹 Botón para continuar
        botonParaContinuar = tk.Button(self, text="Continuar con el programa",command=self.abrirVentanaSecundaria)
        botonParaContinuar.pack()

        # 🔹 P6 - Foto del desarrollador
        p6Frame = tk.Frame(frameDeAbajo, bg="gray")
        p6Frame.pack(side="right", fill="both", expand=True)

        self.fotoLabel = tk.Label(p6Frame)
        self.fotoLabel.pack(expand=True)
        self.fotoLabel.bind("<Button-1>", lambda e: self.cambiarDesarrollador())

        # Inicializar con la primera imagen
        self.actualizarFoto()

    def cambiarDesarrollador(self):
        """ Cambia la información del desarrollador mostrado. """
        self.indiceDesarrollador = (self.indiceDesarrollador + 1) % len(self.nombresDesarrolladores)
        self.descripcionLabel.config(text=self.descripciones[self.indiceDesarrollador])
        self.actualizarFoto()

    def actualizarFoto(self):
        """ Actualiza la foto del desarrollador. """
        rutaImagen = self.fotosDesarrolladoresPaths[self.indiceDesarrollador]
        imagen = tk.PhotoImage(file=rutaImagen)
        imagen = imagen.subsample(2, 2)  # Escalar la imagen
        self.fotoLabel.config(image=imagen)
        self.fotoLabel.image = imagen  # Mantener referencia
    
    def abrirVentanaSecundaria(self):
        from seleccionFuncionalidad import VentanaSecundaria
        """ Abre la ventana secundaria sin cerrar la principal. """
        if self.ventanaSecundaria is None or not self.ventanaSecundaria.winfo_exists():
            self.ventanaSecundaria = VentanaSecundaria(self)
        else:
            messagebox.showinfo("Información", "La ventana secundaria ya está abierta.")


# Ejecutar la aplicación
if __name__ == "__main__":
    app = VentanaInicio()
    app.mainloop()
