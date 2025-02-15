#interfaz de inicio 

import tkinter as tk
from tkinter import messagebox

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("500x300")

#Menú

barraMenu = tk.Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)

menu1 = tk.Menu(barraMenu)
barraMenu.add_cascade(label="Inicio", menu=menu1)
menu1.add_command(label="Salir de la aplicación", command=ventanaPrincipal.quit)
menu1.add_separator()

def info():
    messagebox.showinfo("Información", "Este sistema fue desarrollado por el grupo JJAYC, \n")

menu1.add_command(label="Descripción del sistema", command=info)

#Frame superior

frame_superior = tk.Frame(ventanaPrincipal)
frame_superior.pack(fill="both", expand=True)

etiqueta1 = tk.Label(
    frame_superior,
    text="Bienvenido al sistema de distribución JJAYC,\n"
         "el sistema donde podrás manejar tu negocio,\n"
         "pudiendo abastecer tiendas, enviar pedidos,\n"
         "manejar devoluciones, pagar a tus trabajadores\n"
         "y revisar las estadísticas de la empresa.",
    bg="lightgreen",
    justify="left"
)
etiqueta1.pack(side="left", fill="both", expand=True, padx=10, pady=10)  

etiqueta2 = tk.Label(
    frame_superior,
    text="Aca van las fotos",
    bg="lightblue",
    justify="center"
)
etiqueta2.pack(side="right", fill="both", expand=True, padx=10, pady=10)

#Frame inferior

frame_inferior = tk.Frame(ventanaPrincipal)
frame_inferior.pack(fill="both", expand=True)   


boton1 = tk.Button(frame_inferior, text="Presione para utilizar\nel sistema")
boton1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

etiqueta3 = tk.Label(frame_inferior, text="Aca van las fotos de los \ndesarrolladores", bg="lightblue")
etiqueta3.pack(side="right", fill="both", expand=True, padx=10, pady=10)

ventanaPrincipal.mainloop()
