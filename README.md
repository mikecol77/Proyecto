# MANUAL TÉCNICO

## Introducción
Este manual técnico describe el funcionamiento de la aplicación web "Restaurante La Esquina", desarrollada en Python utilizando el framework Flask. La aplicación permite a los usuarios autenticarse, generar menús para los días sábado y domingo, y actualizar el inventario de ingredientes del restaurante.

## Requisitos del Sistema
- Python 3.x
- Flask 2.x
- Navegador web compatible (Chrome, Firefox, Edge)

## Instalación
- Se deben instalar las respectivas dependencias
- Ejecutar la aplicación

## Estructura del código
- `app = Flask(__name__)`: Inicializa la aplicación Flask.
- `app.secret_key = 'supersecretkey'`: Clave secreta para la gestión de sesiones.
- `USUARIO_PERMITIDO` y `CONTRASENA_PERMITIDA`: Credenciales permitidas para iniciar sesión.
- `inventario`: Diccionario que almacena el inventario inicial de ingredientes.

## Funciones principales

### verificar_credenciales(usuario, contrasena)
- Verifica las credenciales de inicio de sesión.
- **Parámetros**: `usuario` (str), `contrasena` (str).
- **Retorna**: `True` si las credenciales son correctas, `False` en caso contrario.

### generar_menu_sabado()
- Genera y retorna un menú aleatorio para el sábado.
- Sin parámetros.

### generar_menu_domingo()
- Genera y retorna un menú aleatorio para el domingo.
- Sin parámetros.

### actualizar_inventario(ingrediente, cantidad)
- Actualiza el inventario con un nuevo ingrediente o incrementa la cantidad de uno existente.
- **Parámetros**: `ingrediente` (str), `cantidad` (int).
- **Retorna**: Inventario actualizado.

## Rutas de la Aplicación

### '/' (home)
- Ruta principal de la aplicación.
- **Métodos**: GET, POST.
- Muestra un formulario de inicio de sesión.

### '/inicio' (inicio)
- Ruta de inicio después de la autenticación.
- **Métodos**: GET, POST.
- Muestra opciones para generar menús y agregar ingredientes al inventario.

### '/menu_sabado' (menu_sabado)
- Genera y muestra el menú del sábado.
- **Método**: POST.

### '/menu_domingo' (menu_domingo)
- Genera y muestra el menú del domingo.
- **Método**: POST.

### '/agregar_ingrediente' (ruta_agregar_ingrediente)
- Permite agregar un ingrediente al inventario.
- **Método**: POST.

## Templates
Los templates están incrustados directamente en las rutas utilizando `render_template_string` de Flask. Se utiliza Bootstrap para el diseño de la interfaz de usuario.

## Ejecución

### Iniciar la aplicación:
- Ejecutar el script `app.py`.
- La aplicación estará disponible en `http://127.0.0.1:5000/`.

### Inicio de sesión:
- Ingresar el usuario `Michael` y la contraseña `Proyecto777`.

### Generación de Menús:
- En la página de inicio, seleccionar la opción para generar menús de sábado o domingo.

### Actualización de Inventario:
- Completar el formulario para agregar un nuevo ingrediente y su cantidad.

## Seguridad
- **Gestión de Sesiones**: Utiliza `session` para mantener el estado de autenticación.
- **Clave Secreta**: Definida en `app.secret_key` para la gestión segura de sesiones.
