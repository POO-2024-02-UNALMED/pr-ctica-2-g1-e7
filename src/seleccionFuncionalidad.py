import tkinter as tk
from tkinter import ttk, messagebox

# Funciones para los menús
def mostrar_info_aplicacion():
    messagebox.showinfo("Aplicación", "Esta aplicación gestiona procesos y consultas del sistema.")

def mostrar_autores():
    messagebox.showinfo("Acerca de", "Autores: Equipo de Desarrollo JJAYC")

def salir():
    ventana.quit()

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry("700x500")
ventana.title("Nombre de la Aplicación")

# 🔹 ZONA 0 - Título de la aplicación
frame_titulo = tk.Frame(ventana, relief="solid", bd=1)
frame_titulo.pack(fill="x", padx=5, pady=5)

titulo = tk.Label(frame_titulo, text="Nombre de la aplicación", font=("Arial", 14, "bold"))
titulo.pack(pady=5)

# 🔹 ZONA 1 - Menú superior
frame_menu = tk.Frame(ventana, relief="solid", bd=1)
frame_menu.pack(fill="x", padx=5, pady=5)

# Menú de opciones
menubar = tk.Menu(ventana)

# Menú Archivo
menu_archivo = tk.Menu(menubar, tearoff=0)
menu_archivo.add_command(label="Aplicación", command=mostrar_info_aplicacion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir)
menubar.add_cascade(label="Archivo", menu=menu_archivo)

# Menú Procesos y Consultas (debes agregar funcionalidades aquí)
menu_procesos = tk.Menu(menubar, tearoff=0)
menu_procesos.add_command(label="Opción 1")
menu_procesos.add_command(label="Opción 2")
menu_procesos.add_command(label="Opción 3")
menu_procesos.add_command(label="Opción 4")
menu_procesos.add_command(label="Opción 5")
menubar.add_cascade(label="Procesos y Consultas", menu=menu_procesos)

# Menú Ayuda
menu_ayuda = tk.Menu(menubar, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=mostrar_autores)
menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

# Asignar menú a la ventana
ventana.config(menu=menubar)

# 🔹 ZONA 2 - Zona de interacción con el usuario
frame_interaccion = tk.Frame(ventana, relief="solid", bd=1)
frame_interaccion.pack(fill="both", expand=True, padx=10, pady=10)

# Descripción de la consulta/proceso
descripcion = tk.Label(frame_interaccion, text="Descripción del proceso o consulta:", font=("Arial", 12))
descripcion.pack(pady=5)

# Área de resultados
frame_resultados = tk.Frame(frame_interaccion, relief="solid", bd=1)
frame_resultados.pack(fill="both", expand=True, padx=5, pady=5)

texto_resultados = tk.Text(frame_resultados, wrap="word", height=10)
texto_resultados.pack(fill="both", expand=True, padx=5, pady=5)

# Botones de acción
frame_botones = tk.Frame(ventana, relief="solid", bd=1)
frame_botones.pack(fill="x", padx=10, pady=5)

boton_aceptar = tk.Button(frame_botones, text="Ejecutar Proceso")
boton_aceptar.pack(side="left", padx=10, pady=5)

boton_borrar = tk.Button(frame_botones, text="Limpiar")
boton_borrar.pack(side="right", padx=10, pady=5)

ventana.mainloop()
