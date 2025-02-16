import tkinter as tk

# Datos de los desarrolladores
indice_desarrollador = 0
nombres_desarrolladores = ["Carlos", "Andres", "Juan", "Yhan", "Jose"]
descripciones = [
    "Carlos Ernesto Galvis González \n19 años \nEstudiante de Ingeniería de Sistemas \nDeportista",
    "Andrés Felipe Guerra Amaris \n18 años \nIngeniería de sistemas e informática  \nNacido en Bucaramanga",
    "Juan Esteban Herrera Navarro \n22 años \nEstudiante ingeniería de sistemas \nTrabajador nato.",
    "Yhan Carlos Jaramillo Diaz \n17 años \nEstudiante de Ingeniería de Sistemas \nTrabajador",
    #agregar info de jose luis 
]
fotos_desarrolladores_paths = [
    "src/gestorAplicacion/uiMain/imagenes/collageCarlos.png",
    "src/gestorAplicacion/uiMain/imagenes/collageAndres.png",
    "src/gestorAplicacion/uiMain/imagenes/collageJuan.png",
    "src/gestorAplicacion/uiMain/imagenes/collageYhan.png"
    #Falta agregar la foto de jose luis
]

def cambiar_desarrollador():
    global indice_desarrollador
    indice_desarrollador = (indice_desarrollador + 1) % len(nombres_desarrolladores)
    descripcion_label.config(text=descripciones[indice_desarrollador])
    actualizar_foto()

def actualizar_foto():
    ruta_imagen = fotos_desarrolladores_paths[indice_desarrollador]
    imagen = tk.PhotoImage(file=ruta_imagen)
    imagen = imagen.subsample(2, 2)  
    foto_label.config(image=imagen)
    foto_label.image = imagen  

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("800x600")
ventana.title("Ventana Principal")

# Marcos principales
frame_de_arriba = tk.Frame(ventana)
frame_de_arriba.pack(fill="both", expand=True)
frame_de_abajo = tk.Frame(ventana)
frame_de_abajo.pack(fill="both", expand=True)

# P3 Saludo
p3_frame = tk.Frame(frame_de_arriba, bg="lightgreen", width=200, height=100)
p3_frame.pack(side="left", fill="both", expand=True)
tk.Label(p3_frame, text="¡Bienvenido al sistema!\n\n Bienvenido al sistema de distribución JJAYC,\n"
         "el sistema donde podrás manejar tu negocio,\n"
         "pudiendo abastecer tiendas, enviar pedidos,\n"
         "manejar devoluciones, pagar a tus trabajadores\n"
         "y revisar las estadísticas de la empresa.", font=("Arial", 12, "bold")).pack()

# P5 Hoja de Vida
p5_frame = tk.Frame(frame_de_arriba, bg="lightblue", width=200, height=100)
p5_frame.pack(side="right", fill="both", expand=True)
descripcion_label = tk.Label(p5_frame, text=descripciones[indice_desarrollador], font=("Arial", 10))
descripcion_label.pack()
descripcion_label.bind("<Button-1>", lambda e: cambiar_desarrollador())

# P4 Imagen del sistema 
p4_frame = tk.Frame(frame_de_abajo, bg="gray",)
p4_frame.pack(side="left", fill="both", expand=True)

foto = tk.PhotoImage(file="src/gestorAplicacion/uiMain/imagenes/fotosDistribuidora.png")
imagen = foto.subsample(2, 2)
foto_negocio = tk.Label(p4_frame, image= imagen)
foto_negocio.place(relx=0, rely=0, relwidth=1, relheight=1)
foto_negocio.pack(expand=True, )

boton_para_continuar = tk.Button(text="Continuar con el programa", anchor= "n" )
boton_para_continuar.pack()


# P6 Foto del desarrollador
p6_frame = tk.Frame(frame_de_abajo, bg="gray")
p6_frame.pack(side="right", fill="both", expand=True)

foto_label = tk.Label(p6_frame)
foto_label.pack(expand=True)
foto_label.bind("<Button-1>", lambda e: cambiar_desarrollador())

# Inicializar con la primera imagen
actualizar_foto()

ventana.mainloop()
