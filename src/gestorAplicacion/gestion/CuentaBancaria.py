from . import Cliente 
class CuentaBancaria:
    def __init__(self, numeroCuenta, saldo=0):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        
    def añadirDinero(self, monto: float):
        self.saldo += monto

    def devolverDinero(self, total: float, cliente: 'Cliente'):
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de reembolsar el dinero a la cuenta bancaria del cliente cuando se realiza una devolución.
        """
        cliente.getCuentaBancaria().añadirDinero(total)