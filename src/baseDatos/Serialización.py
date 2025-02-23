import sys
import os

# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import pickle
import os
# Obtener la ruta del directorio donde está este script
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta relativa al archivo de datos
ruta_datos = os.path.join(ruta_base, "datos.pkl")


def guardar_datos():
    from gestorAplicacion.gestion.Cliente import Cliente
    from gestorAplicacion.gestion.Conductor import Conductor
    from gestorAplicacion.gestion.Factura import Factura
    from gestorAplicacion.gestion.Operario import Operario
    from gestorAplicacion.gestion.Persona import Persona
    from gestorAplicacion.gestion.Vendedor import Vendedor
    from gestorAplicacion.gestion.Meta import Meta
    from gestorAplicacion.produccion.Fabrica import Fabrica
    from gestorAplicacion.produccion.Transporte import Transporte

    datos = {
        "Clientes": Cliente.listaClientes,
        "Conductores": Conductor.listaConductores,
        "Facturas": Factura.getListaFacturas(),
        "Metas": Meta.listaMetas,
        "Operarios": Operario.listaOperarios,
        "Personas": Persona.listaPersonas,
        "Vendedores": Vendedor.listaVendedores,
        "Fabrica": Fabrica.listaFabrica,
        "Transporte": Transporte.listaTransportes,
        "Tiendas": Fabrica.getListaTienda(),
        "ProductosDisponibles": Fabrica.getProductosDisponibles()
    }

    # Verificar que las listas no estén vacías antes de guardar
    for key, value in datos.items():
        print(f"📌 {key}: {len(value)} elementos guardados")

    with open("datos.pkl", "wb") as archivo:
        pickle.dump(datos, archivo)

    print("✅ Datos guardados correctamente.")