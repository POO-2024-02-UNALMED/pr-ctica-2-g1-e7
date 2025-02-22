import sys
import os
import pickle


# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle
import os


def cargar_datos():

    from gestorAplicacion.gestion.Cliente import Cliente
    from gestorAplicacion.gestion.Conductor import Conductor
    from gestorAplicacion.gestion.Factura import Factura
    from gestorAplicacion.gestion.Operario import Operario
    from gestorAplicacion.gestion.Persona import Persona
    from gestorAplicacion.gestion.Vendedor import Vendedor
    from gestorAplicacion.gestion.Meta import Meta
    from gestorAplicacion.produccion.Fabrica import Fabrica
    from gestorAplicacion.produccion.Transporte import Transporte
    if not os.path.exists("datos.pkl"):
        print("⚠️ Archivo de datos no encontrado. Se inicializarán listas vacías.")
        return

    try:
        with open("datos.pkl", "rb") as archivo:
            datos = pickle.load(archivo)

        # ✅ Asignación directa en lugar de extend() para evitar duplicados
        Cliente.listaClientes = datos.get("Clientes", [])
        Conductor.listaConductores = datos.get("Conductores", [])
        Factura._listaFacturas = datos.get("Facturas", [])
        Meta.listaMetas = datos.get("Metas", [])
        Operario.listaOperarios = datos.get("Operarios", [])
        Persona.listaPersonas = datos.get("Personas", [])
        Vendedor.listaVendedores = datos.get("Vendedores", [])
        Fabrica.listaFabrica = datos.get("Fabrica", [])
        Transporte.listaTransportes = datos.get("Transporte", [])
        Fabrica._listaTienda = datos.get("Tiendas", [])
        Fabrica._productosDisponibles = datos.get("ProductosDisponibles", [])

        print("✅ Datos cargados correctamente.")

    except (EOFError, pickle.UnpicklingError):
        print("⚠️ Error al cargar los datos. El archivo puede estar corrupto.")

