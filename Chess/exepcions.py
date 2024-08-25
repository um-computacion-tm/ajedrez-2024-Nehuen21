class ChessError(Exception):
    """Clase base para otras excepciones específicas de ajedrez"""
    pass

class MovimientoIlegalError(ChessError):
    """Se lanza cuando un movimiento no es legal"""
    def __init__(self, message="Movimiento ilegal para esta pieza."):
        self.message = message
        super().__init__(self.message)

class PiezaNoEncontradaError(ChessError):
    """Se lanza cuando no se encuentra una pieza en la posición indicada"""
    def __init__(self, posicion, message="No se encontró una pieza en la posición indicada."):
        self.posicion = posicion
        self.message = f"{message} Posición: {self.posicion}"
        super().__init__(self.message)
