import sys
import os

# Agregar la carpeta 'src' al sys.path para que Python encuentre 'gestorAplicacion'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pickle
from gestorAplicacion.gestion.Cliente import Cliente
from gestorAplicacion.gestion.Conductor import Conductor
from gestorAplicacion.gestion.CuentaBancaria import CuentaBancaria
from gestorAplicacion.gestion.Factura import Factura
from gestorAplicacion.gestion.Operario import Operario
from gestorAplicacion.gestion.Persona import Persona
from gestorAplicacion.gestion.Vendedor import Vendedor
from gestorAplicacion.gestion.Meta import Meta
from gestorAplicacion.produccion.Fabrica import Fabrica
from gestorAplicacion.produccion.Transporte import Transporte



with open("Clientes.pkl", "wb") as archivo:
    pickle.dump(Cliente.listaClientes, archivo)

with open("Conductores.pkl", "wb") as archivo:
    pickle.dump(Conductor.listaConductores, archivo)

with open("Facturas.pkl", "wb") as archivo:
    pickle.dump(Factura.getListaFacturas(), archivo)

with open("Metas.pkl", "wb") as archivo:
    pickle.dump(Meta.listaMetas, archivo)

with open("Operarios.pkl", "wb") as archivo:
    pickle.dump(Operario.listaOperarios, archivo)

with open("Personas.pkl", "wb") as archivo:
    pickle.dump(Persona.listaPersonas, archivo)

with open("Vendedores.pkl", "wb") as archivo:
    pickle.dump(Vendedor.listaVendedores, archivo)

with open("Fabrica.pkl", "wb") as archivo:
    pickle.dump(Fabrica.listaFabrica, archivo)

with open("Transporte.pkl", "wb") as archivo:
    pickle.dump(Transporte.listaTransportes, archivo)

with open("Tiendas.pkl", "wb") as archivo:
    pickle.dump(Fabrica.getListaTienda(), archivo)

with open("ProductosDisponibles.pkl", "wb") as archivo:
    pickle.dump(Fabrica.getProductosDisponibles(), archivo)

