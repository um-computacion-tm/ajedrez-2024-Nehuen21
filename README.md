

# CircleCI
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/ajedrez-2024-Nehuen21/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/ajedrez-2024-Nehuen21/tree/main)

# Maintainability
[![Maintainability](https://api.codeclimate.com/v1/badges/cfce0e3e97bd529639dd/maintainability)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Nehuen21/maintainability)

# Test Coverage
[![Test Coverage](https://api.codeclimate.com/v1/badges/cfce0e3e97bd529639dd/test_coverage)](https://codeclimate.com/github/um-computacion-tm/ajedrez-2024-Nehuen21/test_coverage)


# Autor
- Nehuen Donozo ing informatica
- legajo 62325
- @Nehuen21

# Observaciones

- Este Ajedrez al ejecutarlo y jugar, recien toma la victoria de la pieza ganadora despues de hacer otro movimiento al haberse comido al rey, no supe como solucionar esto asi que quedo asi

- Este Ajedrez no tienen en cuenta el jaquemate, tablas,promocion de peones, ni el enroque
- Se me hizo una breve confusion entre la terminal y los iconos provocando una leve confusion entre las peizas blancas y negras. Las piezas blancas en este caso son las que estan por encima del tablero por ejemplo la torre blanca estaria en  A8 mientras que la negra A1

# Comandos para DOCKER

1- docker buildx build -t ajedrez-2024-Nehuen21 .

2- docker run -i ajedrez-2024-Nehuen21
