import sys
import os
import pickle


# Obtener la ruta absoluta de la carpeta donde está este script
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

# Ruta del archivo de datos.pkl
ruta_datos = os.path.join(BASE_DIR, "datos.pkl")


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

    print("🔄 Ejecutando cargar_datos()")
    print(f"🔍 Buscando archivo en: {ruta_datos}")

    if not os.path.exists(ruta_datos):
        print(f"⚠️ Archivo de datos no encontrado en {ruta_datos}. Se inicializarán listas vacías.")
        return

    try:
        with open(ruta_datos, "rb") as archivo:
            datos = pickle.load(archivo)        

        # ✅ Asignación de listas
        Cliente.listaClientes = datos.get("Clientes", [])
        Conductor.listaConductores = datos.get("Conductores", [])
        Factura.listaFacturas = datos.get("Facturas", [])
        Meta.listaMetas = datos.get("Metas", [])
        Operario.listaOperarios = datos.get("Operarios", [])
        Persona.listaPersonas = datos.get("Personas", [])
        Vendedor.listaVendedores = datos.get("Vendedores", [])
        Fabrica.listaFabrica = datos.get("Fabrica", [])
        Transporte.listaTransportes = datos.get("Transporte", [])
        Fabrica._listaTienda = datos.get("Tiendas", [])
        Fabrica._productosDisponibles = datos.get("ProductosDisponibles", [])
        Fabrica._cuentaBancaria = datos.get("CuentaBancariaFabrica", None)  # ✅ Cargar la cuenta bancaria

        print("✅ Datos cargados correctamente.")

    except (EOFError, pickle.UnpicklingError) as e:
        print("⚠️ Error al cargar los datos. El archivo puede estar corrupto.", e)