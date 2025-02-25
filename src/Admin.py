import sys, os

# Agrega la carpeta 'src' a sys.path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
sys.path.insert(0, src_path)


from Excepciones.EnteroFueraDeRango import OpcionNoValida
from tkinter import Tk, Label,messagebox, ttk, Button, Frame



from tkinter import messagebox
from ventanaInicio import centrar_ventana

class Admin:
    from gestorAplicacion.gestion.Factura import Factura
    from gestorAplicacion.gestion.Meta import Meta
    from gestorAplicacion.produccion.Producto import Producto
    pagina_actual = 0
    productoSeleccionado:Producto=None
    facturaSeleccionada:Factura=None 

    @staticmethod
    def destruirVentanaPrincipal(ventanaPrincipal:Tk):
        from seleccionFuncionalidad import VentanaSecundaria
        ventanaPrincipal.destroy()
        nuevaVentana=VentanaSecundaria()
        #centrar_ventana(nuevaVentana)

    @staticmethod
    def volverVentanaInicio(ventanaSecundaria:Tk):
        from ventanaInicio import VentanaInicio
        ventanaSecundaria.destroy()
        ventana_inicio=VentanaInicio()
        #centrar_ventana(ventana_inicio)

    @staticmethod
    def salirDelSistema(): 
        pass #Este es el método que se encarga de serializar los objetos cuando se cierre el programa. Implementacion pendiente

    @staticmethod
    def obtenerFacturas():
        from gestorAplicacion.gestion.Factura import Factura
        facturas = []
        n = 1
        for factura in Factura.listaFacturas:
            facturas.append(f"{n}. {factura.getCliente().getNombre()} - Tienda: {factura.getTienda().getNombre()}")
            n += 1
        return facturas

    @classmethod
    def mostrarFacturas(cls):
        facturas = cls.obtenerFacturas()
        inicio = cls.pagina_actual * 10
        fin = inicio + 10
        return facturas[inicio:fin]

    @classmethod
    def avanzarPagina(cls):
        if (cls.pagina_actual + 1) * 10 < len(cls.obtenerFacturas()):
            cls.pagina_actual += 1

    @classmethod
    def retrocederPagina(cls):
        if cls.pagina_actual > 0:
            cls.pagina_actual -= 1

    @staticmethod
    def obtenerFactura(num, frame_interaccion=None):
        from gestorAplicacion.gestion.Factura import Factura
        try:
            num_factura = int(num)
            if num_factura > len(Factura.getListaFacturas()):
                raise OpcionNoValida(num_factura)
            else:
                factura = Factura.seleccionarFactura(num_factura)
            return factura
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")
        except OpcionNoValida as ONV:
            messagebox.showerror("Error", ONV.mensaje_error_inicial)
        return None

    @staticmethod
    def evaluarMotivo(motivoDevolucion, frame_interaccion):
        from gestorAplicacion.produccion.Producto import Producto
        motivos = Producto.getMotivosDevolucion()
        if motivoDevolucion in (motivos[0], motivos[1], motivos[2]):
            return 0
        else: 
            return 1
    @classmethod
    def procesarCambioProducto(cls, carrito, excedente):
        from gestorAplicacion.produccion.Tienda import Tienda
        from gestorAplicacion.gestion.Cliente import Cliente
        from gestorAplicacion.produccion.Fabrica import Fabrica
        tienda = cls.facturaSeleccionada.getTienda()
        cliente = cls.facturaSeleccionada.getCliente()

        # Si hay excedente, se transfiere el dinero correspondiente
        if excedente > 0:
            cliente.getCuentaBancaria().transferirDinero(excedente, Fabrica.getCuentaBancaria())
        # Se remueve el producto original y se marca como devuelto
        cliente.removerProducto(cls.productoSeleccionado)
        cls.productoSeleccionado.setDevuelto(True)
        # Se agregan los productos seleccionados al cliente y se actualiza el inventario de la tienda
        for p in carrito:
            cliente.getListaProductos().append(p)
            for producto in tienda.getListaProducto():
                if producto.getId() == p.getId():
                    tienda.getListaProducto().remove(producto)
                    break
        

    @classmethod
    def procesarReembolso(cls):
        from gestorAplicacion.produccion.Tienda import Tienda
        from gestorAplicacion.gestion.Cliente import Cliente
        from gestorAplicacion.produccion.Fabrica import Fabrica
        tienda = Admin.facturaSeleccionada.getTienda()
        cliente = tienda.devolverProducto(Admin.facturaSeleccionada, Admin.productoSeleccionado)
        valorADevolver = Fabrica.descontarDineroCuenta(Admin.productoSeleccionado)
        Fabrica.getCuentaBancaria().devolverDinero(valorADevolver, cliente)
        cliente.removerProducto(Admin.productoSeleccionado)
    # 🔹 Nuevos métodos para el pago de trabajadores
    @staticmethod
    def obtenerListaTrabajadores(tipo):
        from gestorAplicacion.gestion.Operario import Operario
        from gestorAplicacion.gestion.Vendedor import Vendedor
        from gestorAplicacion.gestion.Conductor import Conductor



        """
        Devuelve la lista de trabajadores según el tipo especificado.
        :param tipo: 1 para Operarios, 2 para Conductores, 3 para Vendedores.
        :return: Lista de trabajadores.
        """
        if tipo == 1:
            return Operario.getListaOperarios()
        elif tipo == 2:
            return Conductor.getListaConductores()
        elif tipo == 3:
            return Vendedor.getListaVendedores()
        else:
            return []

    @staticmethod
    def calcularPagoTrabajador(trabajador):
        """
        Calcula el pago potencial de un trabajador (salario base + pago por trabajo realizado).
        :param trabajador: El trabajador al que se le calculará el pago.
        :return: El pago potencial.
        """
        return trabajador.getCuentaBancaria().calcularPago(trabajador) + trabajador.getSalarioBase()

    @staticmethod
    def revisarMetasTrabajador(trabajador):
        """
        Devuelve las metas no pagadas de un trabajador.
        :param trabajador: El trabajador cuyas metas se revisarán.
        :return: Lista de metas no pagadas.
        """
        return [meta for meta in trabajador.getMeta() if not meta.getVerificador()]

    @staticmethod
    def cumplirMeta(trabajador, meta):
        """
        Marca una meta como cumplida y agrega el pago correspondiente.
        :param trabajador: El trabajador al que pertenece la meta.
        :param meta: La meta que se marcará como cumplida.
        :return: True si la meta fue cumplida, False en caso contrario.
        """
        if meta.cumpleMeta(trabajador.getIndiceMeta()):
            meta.setVerificador(True)
            return True
        return False

    @staticmethod
    def realizarPago(trabajador, pago_total):
        from gestorAplicacion.produccion.Fabrica import Fabrica

        """
        Realiza el pago al trabajador y actualiza la cuenta bancaria de la fábrica.
        :param trabajador: El trabajador al que se le realizará el pago.
        :param pago_total: El monto total a pagar.
        """
        Fabrica._cuentaBancaria.descontarDinero(pago_total)
        trabajador.recibirSueldo(pago_total)
    

    @staticmethod
    def mostrarTiendas():
        """
        Retorna y muestra las tiendas disponibles con sus productos.
        Importa Fabrica dentro del método para evitar dependencias circulares.
        """
        from gestorAplicacion.produccion.Fabrica import Fabrica
        
        tiendas = Fabrica.getListaTienda()
        if not tiendas:
            return []
        
        # Imprime el estado de las tiendas para depuración
        print("Listado de Tiendas:")
        for i, tienda in enumerate(tiendas, start=1):
            print(f"{i}. {tienda.getNombre()}:")
            print(tienda.cantidadProductos())
        
        return tiendas

