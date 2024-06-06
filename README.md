# Restaurante La Esquina

Este proyecto es una aplicación web para el restaurante "La Esquina". La aplicación permite a los usuarios autenticarse, generar menús para los días sábado y domingo, y actualizar el inventario de ingredientes del restaurante.

## Características

- **Autenticación de Usuarios**: Solo los usuarios con credenciales correctas pueden acceder a la aplicación.
- **Generación de Menús**: Permite generar menús aleatorios para los días sábado y domingo.
- **Gestión de Inventario**: Permite agregar ingredientes al inventario.

## Requisitos

- Python 3.x
- Flask

## Instalación

1. Clona este repositorio:
    ```sh
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```sh
    cd tu_repositorio
    ```
3. Instala las dependencias necesarias:
    ```sh
    pip install Flask
    ```

## Uso

1. Ejecuta la aplicación:
    ```sh
    python nombre_del_archivo.py
    ```
2. Abre tu navegador web y navega a `http://127.0.0.1:5000/`.

## Rutas Principales

- `/`: Página de inicio de sesión.
- `/inicio`: Página principal después de iniciar sesión, donde se pueden generar los menús y actualizar el inventario.
- `/menu_sabado`: Genera y muestra el menú del sábado.
- `/menu_domingo`: Genera y muestra el menú del domingo.
- `/agregar_ingrediente`: Permite agregar un ingrediente al inventario.

## Ejemplos de Uso

### Iniciar Sesión

1. Ingresa el nombre de usuario y la contraseña permitidos:
    - **Usuario**: Michael
    - **Contraseña**: Proyecto777

2. Haz clic en "Iniciar Sesión".

### Generar Menús

- Desde la página principal, selecciona "Generar Menús del Sábado" o "Generar Menús del Domingo" para obtener un menú aleatorio.

### Actualizar Inventario

- En la página principal, llena los campos "Ingrediente" y "Cantidad" y haz clic en "Agregar al Inventario" para actualizar el inventario.

## Estructura del Código

- `app = Flask(__name__)`: Inicializa la aplicación Flask.
- `USUARIO_PERMITIDO` y `CONTRASENA_PERMITIDA`: Credenciales de usuario.
- `inventario`: Diccionario que almacena el inventario inicial.
- `verificar_credenciales`: Función para verificar las credenciales de inicio de sesión.
- `generar_menu_sabado` y `generar_menu_domingo`: Funciones para generar los menús de sábado y domingo.
- `actualizar_inventario`: Función para actualizar el inventario.
- Rutas de la aplicación (`home`, `inicio`, `menu_sabado`, `menu_domingo`, `agregar_ingrediente`): Definen las distintas páginas y funcionalidades de la aplicación.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor realiza un fork del repositorio y crea un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.
