from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('accueil.html')


@app.route('/cart/<id>')
def add_to_cart(id):
    return f"Ajout du produit avec le id {id} au panier"

if __name__ == '__main__':
    app.run(debug=True) #pas besoin de reboot Flask
