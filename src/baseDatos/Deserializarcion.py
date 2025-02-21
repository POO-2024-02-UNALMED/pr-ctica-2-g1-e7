import sys
import os
import pickle


# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Cargar los datos desde los archivos serializados
with open("Clientes.pkl", "rb") as archivo:
    listaClientes = pickle.load(archivo)

with open("Conductores.pkl", "rb") as archivo:
    listaConductores = pickle.load(archivo)

with open("Facturas.pkl", "rb") as archivo:
    listaFacturas = pickle.load(archivo)

with open("Metas.pkl", "rb") as archivo:
    listaMetas = pickle.load(archivo)

with open("Operarios.pkl", "rb") as archivo:
    listaOperarios = pickle.load(archivo)

with open("Personas.pkl", "rb") as archivo:
    listaPersonas = pickle.load(archivo)

with open("Vendedores.pkl", "rb") as archivo:
    listaVendedores = pickle.load(archivo)

with open("Fabrica.pkl", "rb") as archivo:
    listaFabrica = pickle.load(archivo)

with open("Transporte.pkl", "rb") as archivo:
    listaTransportes = pickle.load(archivo)

with open("Tiendas.pkl", "rb") as archivo:
    listaTiendas = pickle.load(archivo)

with open("ProductosDisponibles.pkl", "rb") as archivo:
    productosDisponibles = pickle.load(archivo)

# Imprimir para verificar la carga
print("Clientes:", listaClientes)
print("Conductores:", listaConductores)
print("Facturas:", listaFacturas)
print("Metas:", listaMetas)
print("Operarios:", listaOperarios)
print("Personas:", listaPersonas)
print("Vendedores:", listaVendedores)
print("Fábricas:", listaFabrica)
print("Transportes:", listaTransportes)
print("Tiendas:", listaTiendas)
print("Productos Disponibles:", productosDisponibles)