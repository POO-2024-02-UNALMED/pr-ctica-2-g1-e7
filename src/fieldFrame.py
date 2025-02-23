import tkinter as tk
from tkinter import ttk, Frame

class FieldFrame(Frame):
    

    def __init__(self, parent, tituloCriterios, criterios, tituloValores, valores=None, habilitado=None):
        """
        Constructor de la clase FieldFrame.
        
        :param parent: Frame o ventana donde se coloca este componente.
        :param tituloCriterios: Título para la columna "Criterio".
        :param criterios: Lista con los nombres de los criterios.
        :param tituloValores: Título para la columna "Valor".
        :param valores: Lista con valores iniciales. Si es None, los campos estarán vacíos.
        :param habilitado: Lista de booleanos indicando qué campos son editables. Si es None, todos son editables.
        """
        super().__init__(parent)
        self.criterios = criterios
        self.entradas = []  

        # 🔹 Encabezados de la tabla
        tk.Label(self, text=tituloCriterios, font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10, pady=5)
        tk.Label(self, text=tituloValores, font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10, pady=5)

        # 🔹 Crear los campos dinámicamente
        for i, criterio in enumerate(criterios):
            # Etiqueta de criterio
            tk.Label(self, text=criterio, font=("Arial", 10)).grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

            # Valor del criterio
            valor_inicial = valores[i] if valores and i < len(valores) else ""
            es_editable = habilitado is None or (i < len(habilitado) and habilitado[i])

            entry = tk.Entry(self)
            entry.insert(0, valor_inicial)  # Insertar valor inicial
            if not es_editable:
                entry.config(state="readonly")  # Bloquear campo si no es editable

            entry.grid(row=i + 1, column=1, padx=10, pady=5)
            self.entradas.append(entry)  # Guardar referencia en la lista

    def getValue(self, criterio):
        """
        
        :param criterio: El criterio cuyo valor se quiere obtener.
        :return: El valor del criterio o None si el criterio no existe.
        """
        try:
            index = self.criterios.index(criterio)  # Buscar índice del criterio en la lista
            return self.entradas[index].get()  # Obtener el valor correspondiente
        except ValueError:
            return None  # Si el criterio no existe, devolver None
