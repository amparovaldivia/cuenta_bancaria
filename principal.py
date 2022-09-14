class Cuenta_bancaria:
    todas_cuentas = []
    def __init__(self,saldo_cuenta,interes):
        self.saldo_cuenta=saldo_cuenta
        self.interes=interes
        Cuenta_bancaria.todas_cuentas.append(self) 
        
    def deposito(self, monto):
        self.saldo_cuenta=self.saldo_cuenta+monto    
        return self
    def retiro(self, monto): 
        self.saldo_cuenta=self.saldo_cuenta-monto           
        return self
    def mostrar_info_cuenta(self):
        print(self.saldo_cuenta)
        return self
    def generar_interes(self): 
        self.saldo_cuenta=self.saldo_cuenta+self.interes*self.saldo_cuenta
        return self
    @classmethod
    def todas_las_cuentas(cls):
        for cuenta in cls.todas_cuentas:
            print(cuenta.__dict__)