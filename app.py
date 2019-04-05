from flask import Flask, render_template, request
from foodcart.Connection import *
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('accueil.html')


@app.route('/cart/<id>')
def add_to_cart(id):
    return f"Ajout du produit avec le id {id} au panier"

@app.route('/signup')
def signup_page():
    return render_template('Signup.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

@app.route('/account')
def account_page():
    return render_template('account.html')

@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def authentication():

    username = request.form['u']
    password = request.form['p']
    cursor.execute("USE FoodCart;")
    cursor.execute("SELECT * FROM user WHERE username='" + username + "' AND password='" + password + "';")
    data = cursor.fetchone()
    if data is None:
        return "Mauvais Username ou Mot de Passe"
    else:
        return "Vous êtes connecté"

@app.route('/fruits')
def show_fruit():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='fruit' ")
    fruits= cursor.fetchall()
    return render_template('fruits.html', data=fruits)

@app.route('/legumes')
def show_legume():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='legume' ")
    legumes = cursor.fetchall()
    return render_template('legume.html', data=legumes)

@app.route('/viandes')
def show_viandes():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='viande' ")
    viandes = cursor.fetchall()
    return render_template('viandes.html', data=viandes)

@app.route('/boulangerie')
def show_pains():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='pain' ")
    pains = cursor.fetchall()
    return render_template('boulangerie.html', data=pains)

@app.route('/produit_laitier')
def show_lait():
    cursor.execute("USE FoodCart")
    cursor.execute("SELECT * FROM products where class_name ='produit_laitier' ")
    lait = cursor.fetchall()
    return render_template('produit_laitier.html', data=lait)

if __name__ == '__main__':
    app.run(debug=True)  # pas besoin de reboot Flask
