from tkinter import *
from tkinter import messagebox, Tk

class VentanaInicio(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Ventana secundaria
        self.ventanaSecundaria = None
        # Configuración de parámetros principales de la ventana
        self.geometry("800x500")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.iconbitmap('./imagenes/logodistribuidora.ico')
        self.resizable(1, 1)  # Permitir redimensionar la ventana

        # Variables de texto
        self.varHDV = StringVar()
        self.varHDV.set("Desarrolladores")
        self.hola = StringVar()
        self.hola.set('')

        # Configuración del menú
        self.menubar = Menu(self)
        self.menuInicio = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menuInicio, label="Inicio")
        self.menuInicio.add_command(label="Descripcion", command=self.desno)
        self.menuInicio.add_command(label="Salir", command=self.salir)
        self["menu"] = self.menubar

        # Configuración de los frames
        self.P1 = Frame(self, bg="Gray95")
        self.P1.place(relx=0, rely=0, relwidth=0.5, relheight=1)
        self.P3 = Frame(self.P1, bg="Gray95")
        self.P3.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.saludo = Label(self.P3, text="Bienvenido al sistema de manejo de su empresa\nHaz click en la imagen para empezar\n⇣", font=("Segoe UI", 12))
        self.saludo.place(relx=0.5, rely=0.5, anchor="center")

        # Agregar un Label para mostrar la descripción
        self.descripcion_label = Label(self.P1, textvariable=self.hola, font=("Segoe UI", 12), bg="Gray95")
        self.descripcion_label.place(relx=0.5, rely=0.15, anchor="center")

        self.P4 = Frame(self.P1, bg="black")
        self.P4.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        # Configurar el botón de apertura de la ventana secundaria
        self.nueva_ventana = Button(self.P4, command=self.abrirVentanaSecundaria)
        self.nueva_ventana.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.nueva_ventana.bind('<Enter>', self.cambio)

        self.P2 = Frame(self, bg="yellow")
        self.P2.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)
        self.P5 = Frame(self.P2, bg="Gray")
        self.P5.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.textoHDV = Label(self.P5, textvariable=self.varHDV, font=("Segoe UI", 8))
        self.textoHDV.bind('<ButtonPress-1>', self.cambioHDV)
        self.textoHDV.place(relx=0.5, rely=0.5, anchor="center")

        self.P6 = Frame(self.P2, bg="Gray")
        self.P6.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        # Crear los 4 cuadros de colores para las fotos de los desarrolladores
        self.W1 = Frame(self.P6, bg="Blue")
        self.W1.place(relx=0, rely=0, relwidth=0.5, relheight=0.5)
        self.W2 = Frame(self.P6, bg="White")
        self.W2.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.5)
        self.W3 = Frame(self.P6, bg="Green")
        self.W3.place(relx=0, rely=0.5, relwidth=0.5, relheight=0.5)
        self.W4 = Frame(self.P6, bg="Black")
        self.W4.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

        # Labels para mostrar las fotos de los desarrolladores
        self.im_desa_pos1 = Label(self.W1)
        self.im_desa_pos1.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.im_desa_pos2 = Label(self.W2)
        self.im_desa_pos2.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.im_desa_pos3 = Label(self.W3)
        self.im_desa_pos3.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.im_desa_pos4 = Label(self.W4)
        self.im_desa_pos4.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Contadores
        self.acumulador = 0
        self.numClicksHDV = 0

        # Lista de imágenes de desarrolladores
        self.direcciones = [
            "./imagenes/carlos1.png", "./imagenes/carlos2.png", "./imagenes/carlos3.png", "./imagenes/carlos4.png",
            "./imagenes/andres1.png", "./imagenes/andres2.png", "./imagenes/andres3.png", "./imagenes/andres4.png",
            "./imagenes/juan1.png", "./imagenes/juan2.png", "./imagenes/juan3.png", "./imagenes/juan4.png",
            "./imagenes/yhan1.png", "./imagenes/yhan2.png", "./imagenes/yhan3.png", "./imagenes/yhan4.png",
            "./imagenes/jose1.png", "./imagenes/jose2.png", "./imagenes/jose3.png", "./imagenes/jose4.png", "./imagenes/distribuidora5.png"
        ]
        self.cambio_posiciones = []

        # Lista de imágenes del sistema
        self.lineas = [
            './imagenes/distribuidora1.png',
            './imagenes/distribuidora2.png',
            './imagenes/distribuidora3.png',
            './imagenes/distribuidora4.png'
        ]
        self.chang_posiciones = []

        # Cargar imágenes de desarrolladores
        for i in self.direcciones:
            imagen = PhotoImage(file=i)
            self.cambio_posiciones.append(imagen)

        # Cargar imágenes del sistema
        for i in self.lineas:
            imagen = PhotoImage(file=i)
            self.chang_posiciones.append(imagen)

        # Mostrar la foto inicial en los cuatro espacios
        self.mostrar_imagen_inicial()

        # Configurar la imagen inicial del botón
        self.imagen_actual = self.chang_posiciones[0]
        self.nueva_ventana.config(image=self.imagen_actual)

    def mostrar_imagen_inicial(self):
        """Muestra la misma imagen en los 4 cuadros al inicio."""
        imagen_inicial = self.cambio_posiciones[20]  # Usar la última imagen (distribuidora5.png)
        self.im_desa_pos1.config(image=imagen_inicial)
        self.im_desa_pos1.image = imagen_inicial
        self.im_desa_pos2.config(image=imagen_inicial)
        self.im_desa_pos2.image = imagen_inicial
        self.im_desa_pos3.config(image=imagen_inicial)
        self.im_desa_pos3.image = imagen_inicial
        self.im_desa_pos4.config(image=imagen_inicial)
        self.im_desa_pos4.image = imagen_inicial

    def desno(self):
        """Muestra la descripción del sistema."""
        self.hola.set("Permite el manejo de la distribuidora.\nEn la cual se van a poder realizar las siguientes operaciones:\nEnviar Pedidos, manejar devoluciones, abastecer Tiendas,\npagar a los trabajadores, revisar estadisticas.")

    def salir(self):
        """Cierra la ventana."""
        self.destroy()

    def cambioHDV(self, event):
        """Cambia la información de los desarrolladores."""
        self.numClicksHDV += 1
        if self.numClicksHDV == 1:
            self.varHDV.set("Carlos Ernesto Galvis González \n19 años \nEstudiante de Ingeniería de Sistemas \nDeportista")
            self.evento(0)  # Índice inicial para Carlos
        elif self.numClicksHDV == 2:
            self.varHDV.set("Andrés Felipe Guerra Amaris \n18 años \nIngeniería de sistemas e informática  \nNacido en Bucaramanga")
            self.evento(4)  # Índice inicial para Andrés
        elif self.numClicksHDV == 3:
            self.varHDV.set("Juan Esteban Herrera Navarro \n22 años \nEstudiante ingeniería de sistemas \nInteresado por las nuevas tecnologías.")
            self.evento(8)  # Índice inicial para Juan
        elif self.numClicksHDV == 4:
            self.varHDV.set("Yhan Carlos Jaramillo Diaz \n17 años \nEstudiante de Ingeniería de Sistemas \nTrabajador")
            self.evento(12)  # Índice inicial para Yhan
        elif self.numClicksHDV == 5:
            self.varHDV.set("Jose Luis Sanchez Alvarez \n18 años \nEstudiante de Ingenieria de Sistemas \nNacido en Uraba")
            self.evento(16)  # Índice inicial para Jose
            self.numClicksHDV = 0  # Reiniciar el contador después de 5 clics

    def evento(self, c):
        """Muestra las imágenes de los desarrolladores."""
        # Asegurarse de que los índices estén dentro del rango válido
        indices = [c, c + 1, c + 2, c + 3]
        for i, idx in enumerate(indices):
            if idx < len(self.cambio_posiciones):
                imagen = self.cambio_posiciones[idx]
                if i == 0:
                    self.im_desa_pos1.config(image=imagen)
                    self.im_desa_pos1.image = imagen
                elif i == 1:
                    self.im_desa_pos2.config(image=imagen)
                    self.im_desa_pos2.image = imagen
                elif i == 2:
                    self.im_desa_pos3.config(image=imagen)
                    self.im_desa_pos3.image = imagen
                elif i == 3:
                    self.im_desa_pos4.config(image=imagen)
                    self.im_desa_pos4.image = imagen

    def cambio(self, event):
        """Cambia la imagen del sistema."""
        self.acumulador = (self.acumulador + 1) % len(self.chang_posiciones)
        self.imagen_actual = self.chang_posiciones[self.acumulador]
        self.nueva_ventana.config(image=self.imagen_actual)

    def abrirVentanaSecundaria(self):
        """Abre la ventana secundaria."""
        from Admin import Admin
        Admin.destruirVentanaPrincipal(self)


def centrar_ventana(vent):
    """Centra la ventana en la pantalla."""
    vent.update_idletasks()
    width = vent.winfo_width()
    frm_width = vent.winfo_rootx() - vent.winfo_x()
    win_width = width + 2 * frm_width
    height = vent.winfo_height()
    titlebar_height = vent.winfo_rooty() - vent.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = vent.winfo_screenwidth() // 2 - win_width // 2
    y = vent.winfo_screenheight() // 2 - win_height // 2
    vent.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    vent.deiconify()


if __name__ == "__main__":
    ventana_inicio = VentanaInicio()
    centrar_ventana(ventana_inicio)
    ventana_inicio.mainloop()