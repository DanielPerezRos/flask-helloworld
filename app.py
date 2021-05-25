from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuración acceso a BD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost:3306/flask_database'

db = SQLAlchemy(app)

migrate = Migrate(app)




# Modelos
class Film(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    sinopsis = db.Column(db.String(300))
    release_year = db.Column(db.Integer)
    ticket_price = db.Column(db.Float)
    published = db.Column(db.Boolean)




# Vistas
@app.route('/')
def hola_mundo():
    return 'Hola mundo!'

@app.route('/bye', methods=['POST'])
def bye_mundo():
    return 'Hasta luego!'

@app.route('/films/<int:pk>')
def id_peli(pk):
    return 'el id introducido es: ' + str(pk)


@app.route('/films/filter/<string:name>')
def filtro(name):
    return 'el name introducido es: ' + name


@app.route('/temp')
def hola_template():
    return render_template('hello.html', message='mensaje como parámetro: Hola a tod@s!', message2='mensaje 2')

@app.route('/temp2')
def hola_template2():
    names = ['Ariel', 'Aroa', 'Dani']
    return render_template('hello.html',
                           message='mensaje como parámetro: Hola a tod@s!',
                           message2='mensaje 2',
                           names=names
                           )



if __name__ == '__main__':
    app.run()
