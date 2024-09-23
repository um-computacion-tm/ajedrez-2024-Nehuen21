from game.pieza import Pieza


class Peon(Pieza):
    
    def __init__(self,color, position,):
        super().__init__(color,position)
        self.has_moved = False
        
    def __str__(self):
        return "♙" if self.__color__ == "white" else "♟"
    
    
    def move(self, new_position):
        # Lógica para mover el peón
        pass

    
