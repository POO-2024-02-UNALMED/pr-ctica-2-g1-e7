from ventanaInicio import VentanaInicio
from seleccionFuncionalidad import VentanaSecundaria
from tkinter import Tk 
class Admin:
    
    @staticmethod
    def destruirVentanaPrincipal(ventanaPrincipal:Tk): 
        ventanaPrincipal.destroy()
        nuevaVentana=VentanaSecundaria()
    @staticmethod
    def volverVentanaInicio(ventanaSecundaria:Tk): 
        ventanaSecundaria.destroy()
        ventana_inicio=VentanaInicio()