class   AjedrezError(Exception):
    def __init__ (self,mensaje = "ocurrio un error en el juego"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class MovimientoInvalido(AjedrezError):
    def __init__ (self,mensaje = "Movimiento invalido"):
        self.mensaje = mensaje
        super().__init__(mensaje)

class MovimientoErrorPieza(MovimientoInvalido):
    def __init__(self, mensaje="Esta pieza no puede realizar este movimiento"):
        super().__init__(mensaje)

class MismoColorError(AjedrezError):
    def __init__(self,mensaje = "No se puede mover la pieza, ya tienes una pieza en ese lugar"):
        self.mensaje = mensaje
        super().__init__(mensaje)

class PiezaInexistente(AjedrezError):
    def __init__(self, mensaje="No se encuentra ninguna pieza en la celda seleccionada"):
        super().__init__(mensaje)


class PosicionError(AjedrezError):
  
    def __init__(self, message="Posicion invalida"):
        super().__init__(message)



