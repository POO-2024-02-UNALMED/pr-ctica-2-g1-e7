import sys
import os
import pickle


# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pickle
import os
import traceback

if "baseDatos.Deserializarcion" in sys.modules:
    print("❌ Módulo ya importado, evitando recarga.")
else:
    print("✅ Importando módulo Deserializarcion")


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
    traceback.print_stack()
    print("🔄 Ejecutando cargar_datos()")

    if not os.path.exists("datos.pkl"):
        print("⚠️ Archivo de datos no encontrado. Se inicializarán listas vacías.")
        return

    try:
        with open("datos.pkl", "rb") as archivo:
            datos = pickle.load(archivo)

        # Verificar lo que se está cargando
        print("📂 Datos cargados desde el archivo:")
        for key, value in datos.items():
            print(f"🔹 {key}: {len(value)} elementos")

        # ✅ Asignación de listas
        print(f"📂 Antes de cargar: {Cliente.listaClientes}")

        Cliente.listaClientes = datos.get("Clientes", [])

        print(f"📂 Después de cargar: {Cliente.listaClientes}")
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

        print("✅ Datos cargados correctamente.")

    except (EOFError, pickle.UnpicklingError) as e:
        print("⚠️ Error al cargar los datos. El archivo puede estar corrupto.", e)