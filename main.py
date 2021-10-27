class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    

    def cambiarColor(self, col):
        if col=='rojo':
           self.color=col
        if col=='verde':
           self.color=col   
        if col=='amarillo':
           self.color=col
        if col=='negro':
           self.color=col
        if col=='blanco':
           self.color=col

class Motor:
    def __init__(self,numeroCilindros,tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro

    def cambiarRegistro(self,regis):
       self.registro=regis
    def asignarTipo(self, estilo):
        if estilo=='electrico':
            self.tipo=estilo
        if estilo=='gasolina':
            self.tipo=estilo   


class Auto:
    cantidadCreados=0
    def __init__(self,modelo,precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        n=0
        for i in range(len(self.asientos)):
            if self.asientos[i] is not None:
                n+=1
        return n        

    def verificarIntegridad(self):
        a=[]
        for i in range(len(self.asientos)):
            if self.asientos[i] is not None:
                a+=self.asientos[i].registro
        x=a[0]
        verdad=True
        for i in a:
            if i!=x:
                verdad=False
                break
        if x==Motor.registro and x==Asiento.registro and verdad==True:
            print('Las piezas no son originales')
        else:
            print('Auto original')    



    