from game.pieza import Pieza
class Caballo(Pieza):
    def __init__(self, color, position):
        super().__init__(color, position)
        
    def move(self,new_position):
        pass