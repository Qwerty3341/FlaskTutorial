import os

from flask import Flask

# Aqui se crea y se configura la app


def create_app(test_config=None):
    '''
    * Creamos la instancia de Flask
        __name__ es el nombre actual del modulo de python
        instance_relative_config=True Le dice a la app que los archivos 
        de configuracion son relativos al instance folder
    '''
    app = Flask(__name__, instance_relative_config=True)

    # Coloca confuguracion por default que la app va a usar
    app.config.from_mapping(
        SECRET_KEY='dev', # Lo usan Flask y las extenciones para mantener los datos a salvo
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), # Ruta al archivo SQL
    )

    if test_config is None:
        # Carga la instancia de configuracion si existe
        app.config.from_pyfile('config.py', silent=True)
    else:  # Carga la configuracion del test si se esta logueado
        app.config.from_mapping(test_config)

    # Aseguramos que el paquete de instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Pagina de holamundo
    @app.route('/hello')
    def hello():
        return 'Hello World'
    

    from . import db
    db.init_app(app)

    return app
