class cliente:
    Nombre = None
    Direccion =None
    Pedid = None

    def __init__(self, Nombrex,Direccionx,Pedidx ):
        self.Nombre = Nombrex
        self.Direccion = Direccionx
        self.Pedid=Pedidx

    def valorarCredito(self):
        print("Valorado trajeta de credito")

class Pedido:
    FechaRecibido = None
    ConPrepago = None
    Numero = None
    Importe = None
    Divisa = None
    lineaPedi=None

    def __init__(self, FechaRecibidox, ConPrepagox, Numerox, Importex,Divisax,lineaPedid):
        self.FechaRecibido=FechaRecibidox
        self.ConPrepago=ConPrepagox
        self.Numero=Numerox
        self.Importe=Importex
        self.Divisa=Divisax
        self.lineaPedi=lineaPedid

    def seleccionar(self):
        print("Se selecciono el pedido")

    def comprobar(self):
        print("comprobar")

    def servir(self):
        print("Servir")

    def cerrar(self):
        print("cerrar")


class lineaPedido:
    cantidad = None
    Importe = None
    Cumpli = None
    Product = None

    def __init__(self, cantx, impx, cumx, producto):
        self.cantidad = cantx
        self.Importe = impx
        self.Cumpli = cumx
        self.Product = producto

    def aceptar(self):
        print("Se acepto el pedido")

class producto:
    marca = None
    def __init__(self, marx):
        self.marca=marx


class clientePersonal(cliente):
    numTarjetaCredito=None
    def __init__(self, Nombre, direccion,Pedid,numTarjetaCredito):
        super().__init__(Nombre, direccion,Pedid)
        self.numTarjetaCredito = numTarjetaCredito


class clienteCoporativo(cliente):
    NombreContacto=None
    ValoracionCredito = None
    LimiteCredito= None
    representant = None
    def __init__(self, Nombre, direccion,Pedid,NombreContacto, ValoracionCredito,LimiteCredito,representantx):
        super().__init__(Nombre, direccion,Pedid)
        self.NombreContacto=NombreContacto
        self.ValoracionCredito=ValoracionCredito
        self.LimiteCredito=LimiteCredito
        self.representant = representantx

    def facturarMes(self):
        print("facturar")

    def recordar(self):
        print("Recordar")



class representante:
    Nombre_completo=None

    def __init__(self, Nombre_completox):
        self.Nombre_completo = Nombre_completox

    def nombre(self):
        print(self.Nombre_completo)


nombreC = "Manuel"
DireccC = "Chorrillos"


juan=representante("juan gallego")


pelota = producto("adidas")

lineadePe = lineaPedido(4,12,4,pelota)

pedid = Pedido("10/10/20", "si", "999999999", 45,2,lineadePe)

manuel = cliente(nombreC,DireccC,pedid)


clienteCor = clienteCoporativo(nombreC,DireccC,pedid,"juan",144,1000,juan)

clientePer = clientePersonal(nombreC,DireccC,pedid,"14421212121")

#metodos

lineadePe.aceptar()

pedid.seleccionar()

pedid.comprobar()

pedid.servir()

pedid.cerrar()

manuel.valorarCredito()

clienteCor.recordar()
clienteCor.facturarMes()

