from tkinter import Tk, Label,messagebox, ttk
from gestorAplicacion.gestion.Factura import Factura
class Admin:
    pagina_actual = 0

    @staticmethod
    def destruirVentanaPrincipal(ventanaPrincipal:Tk): 
        from seleccionFuncionalidad import VentanaSecundaria
        ventanaPrincipal.destroy()
        nuevaVentana=VentanaSecundaria()
    @staticmethod
    def volverVentanaInicio(ventanaSecundaria:Tk): 
        from ventanaInicio import VentanaInicio
        ventanaSecundaria.destroy()
        ventana_inicio=VentanaInicio()

    @staticmethod
    def salirDelSistema(): 
        pass #Este es el método que se encarga de serializar los objetos cuando se cierre el programa. Implementacion pendiente 
        

    @staticmethod
    def obtenerFacturas():
        """Devuelve todas las facturas en una lista formateada."""
        facturas = []
        n = 1
        for factura in Factura.listaFacturas:
            facturas.append(f"{n}. {factura.getCliente().getNombre()} - Tienda: {factura.getTienda()} - ID: {factura.getID()}")
            n += 1
        return facturas

    @classmethod
    def mostrarFacturas(cls):
        """Devuelve un subconjunto de 10 facturas según la página actual."""
        facturas = cls.obtenerFacturas()
        inicio = cls.pagina_actual * 10
        fin = inicio + 10
        return facturas[inicio:fin]  # Devuelve solo las facturas de la página actual

    @classmethod
    def avanzarPagina(cls):
        """Avanza a la siguiente página si hay más facturas."""
        if (cls.pagina_actual + 1) * 10 < len(cls.obtenerFacturas()):
            cls.pagina_actual += 1

    @classmethod
    def retrocederPagina(cls):
        """Retrocede a la página anterior si no está en la primera."""
        if cls.pagina_actual > 0:
            cls.pagina_actual -= 1
    @staticmethod
   
    def obtenerFactura(num, frameInteraccion): 
        try:
            num_factura = int(num)  # Convertir a entero
            factura = Factura.seleccionarFactura(num_factura)  # Obtener la factura 
            Admin.mostrarProductosFactura(factura, frameInteraccion)  # Llamar a otro método para mostrar productos
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
        except IndexError:
            messagebox.showerror("Error", "Número de factura inválido.")

    @staticmethod
    def mostrarProductosFactura(factura, frameInteraccion):
        # Limpiar solo los widgets relacionados con productos (NO eliminar todo el frame)
        for widget in frameInteraccion.winfo_children():
                widget.destroy()

        # Obtener la lista de productos en formato de lista para el combobox
        productos = factura.mostrarProductosFactura().split("\n")

        # Crear y mostrar el combobox
        Label(frameInteraccion,text="Selecciona el producto de la factura que deseas cambiar: ",font=("Arial",12)).pack(pady=10)
        combobox = ttk.Combobox(frameInteraccion)
        combobox["values"] = productos
        combobox.current(0)  
        combobox["state"] = "readonly"  
        combobox.pack()


