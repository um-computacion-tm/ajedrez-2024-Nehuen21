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



## [V 0.3.1] - 2024/10/08

### corregido 
- test_movimiento_horizontal, test_movimiento_vertical (test_pieza.py)

### anadido

- movimiento_valido(reina.py)
- archivo test_reina.py con sus respectivos test : movimiento_valido_diagonal, movimiento_valido_horizontal,movimiento_valido_vertical, test_iconos etc

### Cambiado
- metodo obtener_pieza de board.py

## [V 0.3.2] - 2024/10/09

### Añadido
- movimiento de caballo.py  (movimiento en L)
- test_caballo.py
### Cambiado

### [V 0.3.3] - 2024/10/10

### Añadido 
- validacion de movimientos de la torre
- añadido test de torre 

### [V 0.3.4] - 2024/10/12

### Añadido
- Validacion de movimiento rey
- Añadido test de rey

### [V 0.3.4] - 2024/10/14

### Añadido

- validacion de movimiento de peon
- test de peon con respectivos movimientos

### Borrado

- archivos del entorno virtual subidos accidentalmente

### [V 0.3.5] - 2024/10/15

###  Añadido
- metodo obtener pieza de chess
- Exepciones
- test de metodos cambio_de_turno , turno_actual y obtener_pieza_origen dentro de test_chess.py

### Modificado

- cambio de turno por errores
- cambiado 2 nombres de archivos para menor confusion
- test de torre por codigo similar
- test de piezas por codigo similar

### [V 0.3.6] - 2024/10/16
### Añadido
- Funcion para los test de pieza para limpiar el tablero una sola vez 
### Modificado
- movimiento del rey , ya que utilizaba logica parecida a la del caballo
- pieza.py, metodo camino_vertical_libre por codigo parecido a la del caminno horizontal
- test_pieza.py , test de logica de movimientos por codigo repetitivo
- cambiando test de peon por bloques similares
- cambiado test_reina.py
### [V 0.3.7] - 2024/10/17
### Añadido

- metodo board y test
- creacion de excepcion para no comerse al rey

### [V 0.3.6] - 2024/10/18
### Añadido
- board :metodo contar piezas con test
- board : metodo para obtener el color con su respectivo test

### [V 0.4.0] - 2024/10/19
### Añadido

- metodos en chess para validaciones y el estado del juego

### [V 0.4.1] - 2024/10/20
### Añadido

### Cambiado
- metodos y test corregidos