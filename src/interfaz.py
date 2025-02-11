import tkinter as tk

ventanaPrincipal = tk.Tk()
ventanaPrincipal.geometry("500x300")

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

frame_inferior = tk.Frame(ventanaPrincipal)
frame_inferior.pack(fill="both", expand=True)


boton1 = tk.Button(frame_inferior, text="Presione para utilizar\nel sistema")
boton1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

etiqueta3 = tk.Label(frame_inferior, text="Aca van las fotos de los \ndesarrolladores", bg="lightblue")
etiqueta3.pack(side="right", fill="both", expand=True, padx=10, pady=10)

ventanaPrincipal.mainloop()
