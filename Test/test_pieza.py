from game.pieza import Pieza

import unittest


import unittest

class TestPieza(unittest.TestCase):
    
    def setUp(self):
        
        self.pieza = Pieza("blanco", (1, 1))

    def test_dame_color(self):
        """Prueba si el color es devuelto correctamente."""
        self.assertEqual(self.pieza.dame_color(), "blanco")

    def test_dame_posicion(self):
        """Prueba si la posición es devuelta correctamente."""
        self.assertEqual(self.pieza.dame_posicion(), (1, 1))

    def test_setear_posicion(self):
        """Prueba si se puede actualizar la posición correctamente."""
        self.pieza.setear_posicion((2, 3))
        self.assertEqual(self.pieza.dame_posicion(), (2, 3))

   


if __name__ == '__main__':
    unittest.main()
