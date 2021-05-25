1. pip install flask
--- app.py:
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return 'Hola mundo!'
---

2. set FLASK_ENV=development
3. flask run

4. para ejecutar la aplicacción:
en app.py:
   if __name__ == '__main__':
    app.run()
   

5.pip install flask-sqlalchemy
   
