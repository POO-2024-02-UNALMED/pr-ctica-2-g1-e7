import sys
import os
import pickle

# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Obtener la ruta del directorio donde está este script
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa al archivo de datos
ruta_datos = os.path.join(ruta_base, "datos.pkl")


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
        print(f"Clientes: {Cliente.listaClientes}")
        print(f"Conductores: {Conductor.listaConductores}")
        print(f"Facturas: {Factura.listaFacturas}")
        print(f"Metas: {Meta.listaMetas}")
        print(f"Operarios: {Operario.listaOperarios}")
        print(f"Personas: {Persona.listaPersonas}")
        print(f"Vendedores: {Vendedor.listaVendedores}")
        print(f"Fabrica: {Fabrica.listaFabrica}")
        print(f"Transportes: {Transporte.listaTransportes}")
        print(f"Tiendas: {Fabrica._listaTienda}")
        print(f"Productos Disponibles: {Fabrica._productosDisponibles}")
        print(f"Cuenta Bancaria Fabrica: {Fabrica._cuentaBancaria}")

    except (EOFError, pickle.UnpicklingError) as e:
        print("⚠️ Error al cargar los datos. El archivo puede estar corrupto.", e)