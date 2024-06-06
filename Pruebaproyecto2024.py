from flask import Flask, render_template_string, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Clave secreta para la sesión

# Usuario y contraseña permitidos hasta el momento
USUARIO_PERMITIDO = "Michael"
CONTRASENA_PERMITIDA = "Proyecto777"

# Inventario inicial
inventario = {"Pollo": 20, "Carne": 15, "Pescado": 10}

# Función para verificar las credenciales
def verificar_credenciales(usuario, contrasena):
    return usuario == USUARIO_PERMITIDO and contrasena == CONTRASENA_PERMITIDA

# Funciones para generar los menús
def generar_menu_sabado():
    menu_sabado = ["Pollo a las finas hierbas con ensalada y vino blanco",
                   "Carne asada con plátanos al carbón y vino tinto",
                   "Pescado a la parrilla con papas asadas y vino rosado"]
    opciones = "\n".join(random.sample(menu_sabado, 3))
    return "Menús del sábado:\n" + opciones

def generar_menu_domingo():
    menu_domingo = ["Sopa de verduras con pollo y vino blanco",
                    "Lomo de cerdo glaseado con puré de batatas y vino tinto",
                    "Ensalada César con camarones y vino rosado"]
    opciones = "\n".join(random.sample(menu_domingo, 3))
    return "Menús del domingo:\n" + opciones

# Función para agregar un ingrediente al inventario
def actualizar_inventario(ingrediente, cantidad):
    global inventario
    inventario[ingrediente] = inventario.get(ingrediente, 0) + int(cantidad)
    return inventario

@app.route('/agregar_ingrediente', methods=['POST'])
def ruta_agregar_ingrediente():
    if 'logged_in' in session:
        ingrediente = request.form['ingrediente']
        cantidad = request.form['cantidad']
        # Actualizar el inventario
        inventario_actualizado = actualizar_inventario(ingrediente, cantidad)
        # Redirigir a la página de inicio con el inventario actualizado
        return render_template_string('''
            <html>
            <head>
                <title>Inventario Actualizado</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container mt-5">
                    <h1>Restaurante La Esquina</h1>
                    <p>Inventario actualizado:</p>
                    <pre>{{ inventario }}</pre>
                    <form method="post" action="/inicio">
                        <button type="submit" class="btn btn-primary">Volver al Inicio</button>
                    </form>
                </div>
            </body>
            </html>
        ''', inventario=inventario_actualizado)
    else:
        return redirect(url_for('home'))

# Rutas de la aplicación
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        contrasena = request.form.get('contrasena')
        if usuario and contrasena:
            if verificar_credenciales(usuario, contrasena):
                session['logged_in'] = True
                return redirect(url_for('inicio'))
            else:
                return "Credenciales incorrectas. Inténtalo de nuevo."
        else:
            return "Faltan credenciales. Inténtalo de nuevo."
    else:
        return render_template_string('''
            <html>
            <head>
                <title>Login</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container mt-5">
                    <h1>Restaurante La Esquina</h1>
                    <form method="post">
                        <div class="form-group">
                            <label for="usuario">Usuario:</label>
                            <input type="text" class="form-control" id="usuario" name="usuario">
                        </div>
                        <div class="form-group">
                            <label for="contrasena">Contraseña:</label>
                            <input type="password" class="form-control" id="contrasena" name="contrasena">
                        </div>
                        <button type="submit" class="btn btn-primary">Iniciar Sesión</button>
                    </form>
                </div>
            </body>
            </html>
        ''')

@app.route('/inicio', methods=['GET', 'POST'])
def inicio():
    if 'logged_in' in session:
        return render_template_string('''
            <html>
            <head>
                <title>Home</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container mt-5">
                    <h1>Restaurante La Esquina</h1>
                    <form method="post" action="/menu_sabado">
                        <button type="submit" class="btn btn-primary">Generar Menús del Sábado</button>
                    </form>
                    <form method="post" action="/menu_domingo">
                        <button type="submit" class="btn btn-primary">Generar Menús del Domingo</button>
                    </form>
                    <form method="post" action="/agregar_ingrediente">
                        <div class="form-group">
                            <label for="ingrediente">Ingrediente:</label>
                            <input type="text" class="form-control" id="ingrediente" name="ingrediente">
                        </div>
                        <div class="form-group">
                            <label for="cantidad">Cantidad:</label>
                            <input type="text" class="form-control" id="cantidad" name="cantidad">
                        </div>
                        <button type="submit" class="btn btn-primary">Agregar al Inventario</button>
                    </form>
                </div>
            </body>
            </html>
        ''')
    else:
        return redirect(url_for('home'))

@app.route('/menu_sabado', methods=['POST'])
def menu_sabado():
    if 'logged_in' in session:
        return render_template_string('''
            <html>
            <head>
                <title>Menú del Sábado</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container mt-5">
                    <h1>Restaurante La Esquina</h1>
                    <form method="post" action="/inicio">
                        <button type="submit" class="btn btn-primary">Volver al Inicio</button>
                    </form>
                    <p>{{ menu }}</p>
                </div>
            </body>
            </html>
        ''', menu=generar_menu_sabado())
    else:
        return redirect(url_for('home'))

@app.route('/menu_domingo', methods=['POST'])
def menu_domingo():
    if 'logged_in' in session:
        return render_template_string('''
            <html>
            <head>
                <title>Menú del Domingo</title>
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container mt-5">
                    <h1>Restaurante La Esquina</h1>
                    <form method="post" action="/inicio">
                        <button type="submit" class="btn btn-primary">Volver al Inicio</button>
                    </form>
                    <p>{{ menu }}</p>
                </div>
            </body>
            </html>
        ''', menu=generar_menu_domingo())
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)




