# Changelog

## [Unreleased]
### Añadido
- Clase `Chess` con la capacidad de mover piezas y cambiar de turno.
- Clase `Board` que inicializa el tablero con las posiciones iniciales de las torres (`Rook`).
- Clase `King` con función para verificar movimientos legales y manejar el estado de enroque.
- Clase `Pawn` con lógica básica para movimientos y promoción.
- Clase `Piece`, que sirve como base para las piezas de ajedrez, incluyendo métodos para mover piezas y verificar su color.

### Cambiado
- Logica del tablero (board.py)

### Corregido
- Atributos del constructor 

### Eliminado
- primer archivo de board

## [V 0.0.3] - 2024/08/29
### Añadido

- Verificaciones de movimientos en el tablero [WIP].


## [V 0.0.2] - 2024/08/15
### Añadido
- Clases `Pawn`, `bishop`, `queen`. Incluye funciones para verificar los movimientos en el tablero.

### Obsolecente
- Funciones de movimiento en la clase `pawn`, ya que no cumplen su objetivo de verificar los movimientos.

## [V 0.0.1] - 2024/08/15
### Añadido
- Clases `Ajedrez`, `Piezas`, `Tablero`, `Torres` para posibilitar el juego de ajedrez.

