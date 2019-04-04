from flask import Flask, render_template, request
from foodcart.Connection import cursor, mydb
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('accueil.html')

@app.route('/pain')
def pain():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='viande' ")
    data = cursor.fetchall()
    return render_template('pain.html', data=data)


@app.route('/cart/<id>')
def add_to_cart(id):
    return f"Ajout du produit avec le id {id} au panier"

if __name__ == '__main__':
    app.run(debug=True) #pas besoin de reboot Flask
