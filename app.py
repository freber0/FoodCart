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


if __name__ == '__main__':
    app.run(debug=True)  # pas besoin de reboot Flask
