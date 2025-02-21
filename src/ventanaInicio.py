from tkinter import *
from Admin import Admin
from tkinter import messagebox, Tk

class ventana_inicio(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # CONFIGURACION PARAMETROS PRINCIPALES DE LA VENTANA
        self.geometry("800x500")
        self.title("Inicio")
        self.option_add("*tearOff", False)
        self.iconbitmap('./imagenes/logodistribuidora.ico')
        self.resizable(0, 0)
        # CONFIGURACION VR--TEXTO HDV DESARROLLADORES
        self.varHDV = StringVar()
        self.varHDV.set("Desarrolladores")

        self.hola = StringVar()
        self.hola.set('')
        # CONFIGURACION ZONA DE MENU
        self.menubar = Menu(self)
        self.menuInicio = Menu(self.menubar)
        self.menubar.add_cascade(menu=self.menuInicio, label="Inicio")
        self.menuInicio.add_command(label="Descripcion", command=self.desno)
        self.menuInicio.add_command(label="Salir", command=self.salir)
        self["menu"] = self.menubar

        # CONFIGURACION ZONA FRAMES

        self.P1 = Frame(self, width=400, height=500, bg="Gray95")
        self.P1.pack(side=LEFT)
        self.P3 = Frame(self.P1, width=400, height=150)
        self.P3.grid(row=0, column=0)
        self.saludo = Label(self.P3, text="Bienvenido al sistema de manejo de su empresa\n""Haz click en la imagen para empezar\n""⇣", font=("Segoe UI", 12))
        self.P4 = Frame(self.P1, width=400, height=350, bg="black")
        self.P4.grid(row=1, column=0)
        self.contenedorImagen = Label(self.P4)
        self.ImagenAplicacion = PhotoImage(file='./imagenes/distribuidora1.png')  # Asegúrate de que la extensión sea correcta
        self.contenedorImagen["image"] = self.ImagenAplicacion
        self.P2 = Frame(self, width=400, height=500, bg="yellow")
        self.P2.pack(side=RIGHT)
        self.P5 = Frame(self.P2, width=400, height=150, bg="Gray")
        self.P5.grid(row=0, column=0)
        self.textoHDV = Label(self.P5, textvariable=self.varHDV, font=("Segoe UI", 8))
        self.textoHDV.bind('<ButtonPress-1>', self.cambioHDV)
        self.textoHDV.place(x=200, y=75, anchor="center")
        self.P6 = Frame(self.P2, width=400, height=350, bg="Gray")
        self.P6.grid(row=1, column=0)
        self.saludo.place(x=200, y=25, anchor="center")
        self.W1 = Frame(self.P6, width=200, height=170, bg="Blue")
        self.W1.place(x=0, y=0)
        self.W2 = Frame(self.P6, width=200, height=170, bg="White")
        self.W2.place(x=200, y=0)
        self.W3 = Frame(self.P6, width=200, height=180, bg="Green")
        self.W3.place(x=0, y=170)
        self.W4 = Frame(self.P6, width=200, height=180, bg="Black")
        self.W4.place(x=200, y=170)
        self.holla = Label(self.P3, textvariable=self.hola, font=("Segoe UI", 8))
        self.holla.place(x=200, y=120, anchor="center")

        # CONTADORES CAMBIO DE CASOS METODOS
        self.acumulador = 0
        self.numClicksHDV = 0

        # LISTA MENEJO IMAGENES DESARROLLADORES
        self.direcciones = [
            "./imagenes/carlos1.png", "./imagenes/carlos2.png", "./imagenes/carlos3.png", "./imagenes/carlos4.png",
            "./imagenes/andres1.png", "./imagenes/andres2.png", "./imagenes/andres3.png", "./imagenes/andres4.png",
            "./imagenes/juan1.png", "./imagenes/juan2.png", "./imagenes/juan3.png", "./imagenes/juan4.png",
            "./imagenes/yhan1.png", "./imagenes/yhan2.png", "./imagenes/yhan3.png", "./imagenes/yhan4.png",
            "./imagenes/jose1.png", "./imagenes/jose2.png", "./imagenes/jose3.png", "./imagenes/jose4.png", "./imagenes/distribuidora5.png"
        ]
        self.cambio_posiciones = []

        # LISTA MANEJO DE IMAGENES DEL SISTEMA
        self.lineas = [
            './imagenes/distribuidora1.png',
            './imagenes/distribuidora2.png',
            './imagenes/distribuidora3.png',
            './imagenes/distribuidora4.png'
        ]
        self.chang_posiciones = []

        # RECORRIDO SOBRE LA LISTA direcciones PARA OBTENER LAS IMAGENES SEGUN LA REFERENIA DEL DESARROLLADOR
        for i in self.direcciones:
            imagen = PhotoImage(file=i)
            self.cambio_posiciones.append(imagen)

        self.im_desa_pos1 = Label(self.W1)
        self.im_desa_pos2 = Label(self.W2)
        self.im_desa_pos3 = Label(self.W3)
        self.im_desa_pos4 = Label(self.W4)

        # Mostrar la foto inicial en los cuatro espacios
        self.im_desa_pos1["image"] = self.cambio_posiciones[20] 
        self.im_desa_pos2["image"] = self.cambio_posiciones[20]  
        self.im_desa_pos3["image"] = self.cambio_posiciones[20]  
        self.im_desa_pos4["image"] = self.cambio_posiciones[20]  

        self.im_desa_pos1.pack()
        self.im_desa_pos2.pack()
        self.im_desa_pos3.pack()
        self.im_desa_pos4.pack()
        self.contador = 0

        # RECORRIDO SOBRE LA LISTA lineas PARA ABRIR DETERMINADA IMAGEN SEGUN LA REFERENCIA DEL EVENTO PARA CAMBIO DE IMAGEN
        for i in self.lineas:
            imagen = PhotoImage(file=i)
            self.chang_posiciones.append(imagen)

        # CONFIGURACION BOTON APERTURA DE LA VENTANA PRINCIPAL Y CAMBIO DE IMAGEN
        self.nueva_ventana = Button(self.P4, image=self.chang_posiciones[0], command=self.abrirVentanaSecundaria)
        self.nueva_ventana.pack()
        self.nueva_ventana.bind('<Enter>', self.cambio)

    # GENERA LA SALIDA DEL TEXTO DE EN LA DESCRIPCION
    def desno(self):
        self.hola.set("Permite el manejo de la distribuidora.\n En la cual se van a poder realizar las siguientes operaciones: \nEnviar Pedidos, manejar devoluciones, abastecer Tiendas, \npagar a los trabajadores, revisar estadisticas.")

    # GENERA LA SALIDA DE LA VENTANA DE INICIO DANDO CULMINADO EL FUNCIONAMIENTO DE LA APLICACION
    def salir(self):
        Admin.salirDelSistema()
        return super().destroy()

    # SUSCITA EL CAMBIO DE INFORMACIÓN DE LA HOJA DE VIDA E IMAGENES DE LOS DESARROLLADORES
    def cambioHDV(self, b):
        self.numClicksHDV += 1
        if self.numClicksHDV == 1:
            self.varHDV.set("Carlos Ernesto Galvis González \n19 años \nEstudiante de Ingeniería de Sistemas \nDeportista")
            self.evento(0)  # Índice inicial para Carlos
        elif self.numClicksHDV == 2:
            self.varHDV.set("Andrés Felipe Guerra Amaris \n18 años \nIngeniería de sistemas e informática  \nNacido en Bucaramanga")
            self.evento(4)  # Índice inicial para Andrés
        elif self.numClicksHDV == 3:
            self.varHDV.set("Juan Esteban Herrera Navarro \n22 años \nEstudiante ingeniería de sistemas \nTrabajador nato.")
            self.evento(8)  # Índice inicial para Juan
        elif self.numClicksHDV == 4:
            self.varHDV.set("Yhan Carlos Jaramillo Diaz \n17 años \nEstudiante de Ingeniería de Sistemas \nTrabajador")
            self.evento(12)  # Índice inicial para Yhan
        elif self.numClicksHDV == 5:
            self.varHDV.set("Jose Luis Sanchez Alvarez \n18 años \nEstudiante de Ingenieria de Sistemas \nNacido en Uraba")
            self.evento(16)  # Índice inicial para Jose
            self.numClicksHDV = 0  # Reiniciar el contador después de 5 clics

    # PROVOCA LA APERTURA DE LAS IMAGENES DE CADA DESARROLLADOR SEGUN SU IDENTIFICADOR POSICIONAL
    def evento(self, c):
        y1 = c
        y2 = c + 1
        y3 = c + 2
        y4 = c + 3

        self.im_desa_pos1.config(image=self.cambio_posiciones[y1])
        self.im_desa_pos2.config(image=self.cambio_posiciones[y2])
        self.im_desa_pos3.config(image=self.cambio_posiciones[y3])
        self.im_desa_pos4.config(image=self.cambio_posiciones[y4])

    # OCASIONA EL CAMBIO EN LA POSICION DE LAS IMAGENES DEL SISTEMA
    def cambio(self, a):
        self.acumulador = (self.acumulador + 1) % len(self.chang_posiciones)
        self.nueva_ventana.config(image=self.chang_posiciones[self.acumulador])

    def abrirVentanaSecundaria(self):
        from seleccionFuncionalidad import VentanaSecundaria
        """ Abre la ventana secundaria sin cerrar la principal. """
        if self.ventanaSecundaria is None or not self.ventanaSecundaria.winfo_exists():
            self.ventanaSecundaria = VentanaSecundaria(self)
        else:
            messagebox.showinfo("Información", "La ventana secundaria ya está abierta.")


def centrar_ventana(vent):
    """
    Basado en https://stackoverflow.com/a/10018670.
    """
    vent.update_idletasks()
    width = vent.winfo_width()
    frm_width = vent.winfo_rootx() - vent.winfo_x()
    win_width = width + 2*frm_width
    height = vent.winfo_height()
    titlebar_height = vent.winfo_rooty() - vent.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = vent.winfo_screenwidth()//2 - win_width//2
    y = vent.winfo_screenheight()//2 - win_height//2
    vent.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    vent.deiconify()

# Ejecutar la aplicación

if __name__ == "__main__":
    ventana_inicios = ventana_inicio()

    centrar_ventana(ventana_inicios)
    ventana_inicios.mainloop()
