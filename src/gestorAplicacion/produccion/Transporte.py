
from TipoTransporte import TipoTransporte

class Transporte:
    montoEnvioGratis = 100000

    def __init__(self, tipoTransporte=None, capacidad=None, costo=None):
        if tipoTransporte is not None and capacidad is not None and costo is not None:
            self.tipoTransporte = tipoTransporte  # Se espera que sea una instancia de TipoTransporte
            self.capacidad = capacidad
            self.costo = costo
            self.listaTransportes = []  # Lista de transportes
            self.listaDeProductos = []  # Lista de productos a transportar
            self.conductor = None
            self.tienda = None
        else:
            # Constructor vacío
            self.listaTransportes = []
            self.listaDeProductos = []
    def abastecerProducto(self, tiendaSeleccionada, productosSeleccionados):
        """
        Carga productos en el transporte y asigna la tienda de destino.
        """
        self.listaDeProductos.extend(productosSeleccionados)
        self.tienda = tiendaSeleccionada
