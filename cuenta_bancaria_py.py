from principal import Cuenta_bancaria

cuenta_uno=Cuenta_bancaria(100000,0.02)
cuenta_dos=Cuenta_bancaria(250000,0.02)

cuenta_uno.deposito(50000).deposito(35000).deposito(12000).retiro(15000).generar_interes().mostrar_info_cuenta()
cuenta_dos.deposito(520000).retiro(100000).retiro(30000).retiro(20000).retiro(15000).generar_interes().mostrar_info_cuenta()
Cuenta_bancaria.todas_las_cuentas()
