class CuentaBancaria:
    def __init__(self, numeroCuenta, saldo=0):
        self.numeroCuenta = numeroCuenta
        self.saldo = saldo
        
    def añadirDinero(self, monto: float):
        self.saldo += monto

    def devolverDinero(self, total: float, cliente):
        from gestorAplicacion.gestion.Cliente import Cliente
        cliente: Cliente = cliente
        """
        Funcionalidad a la que pertenece: Devoluciones
        Método que se encarga de reembolsar el dinero a la cuenta bancaria del cliente cuando se realiza una devolución.
        """
        cliente.getCuentaBancaria().añadirDinero(total)
    def transferirDinero(self, valor: float, cuentaDestino: 'CuentaBancaria'):
        """
        Método que transfiere dinero de esta cuenta a la cuenta de destino.
        """
        self.saldo -= valor
        cuentaDestino.añadirDinero(valor)
    #setters y getters 
    def setSaldo(self,saldo): 
        self.saldo=saldo
    def getSaldo(self): 
        return self.saldo
