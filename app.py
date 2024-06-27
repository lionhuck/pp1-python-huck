import requests

from flask import (
    Flask, 
    render_template,
    request,
)


listado_productos = [
    dict(
        product = 'Escoba',
        category = 'limpieza',
    ),
    dict(
        product = 'Lampazo',
        category = 'limpieza',
    ),
]

app = Flask(__name__)

@app.route('/', methods =['get'])
def index():
    return render_template('index.html')

@app.route('/products')
def product():
    listado = listado_productos
    return render_template(
        'products.html',
        listado = listado
        )
    

@app.route('/add_products', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        product = request.form['product']
        category = request.form['category']
        
        new = dict(
            product = product,
            category = category,
        )


        listado_productos.append(new)
    
    return render_template('add_products.html')



