import sys
import os
import pickle
import traceback


# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

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
        "Facturas": Factura.listaFacturas,
        "Metas": Meta.listaMetas,
        "Operarios": Operario.listaOperarios,
        "Personas": Persona.listaPersonas,
        "Vendedores": Vendedor.listaVendedores,
        "Fabrica": Fabrica.listaFabrica,
        "Transporte": Transporte.listaTransportes,
        "Tiendas": Fabrica.getListaTienda(),
        "ProductosDisponibles": Fabrica.getProductosDisponibles(),
        "CuentaBancariaFabrica": Fabrica._cuentaBancaria  # ✅ Guardar la cuenta bancaria
    }

    with open(ruta_datos, "wb") as archivo:
        pickle.dump(datos, archivo)
    traceback.print_stack()
    print("✅ Datos guardados correctamente.")
    
    # Imprimir el contenido de las listas para verificar
    
    print(f"Clientes: {Cliente.listaClientes}")
    print(f"Conductores: {Conductor.listaConductores}")
    print(f"Facturas: {Factura.getListaFacturas()}")
    print(f"Metas: {Meta.listaMetas}")
    print(f"Operarios: {Operario.listaOperarios}")
    print(f"Personas: {Persona.listaPersonas}")
    print(f"Vendedores: {Vendedor.listaVendedores}")
    print(f"Fabrica: {Fabrica.listaFabrica}")
    print(f"Transportes: {Transporte.listaTransportes}")
    print(f"Tiendas: {Fabrica.getListaTienda()}")
    print(f"Productos Disponibles: {Fabrica.getProductosDisponibles()}")
    print(f"Cuenta Bancaria Fabrica: {Fabrica._cuentaBancaria}")
