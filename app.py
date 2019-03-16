from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/cart')
def get_cart_info():
    return f"Retourne les éléments du cart du user"


@app.route('/cart/<id>', methods=['POST'])
def add_to_cart(id):
    return f"Ajout du produit avec le id {id} au panier"


@app.route('/cart/<id>', methods=['DELETE'])
def remove_from_cart(id):
    return f"Supprime l'item du panier avec le id {id}"


@app.route('/cart/<id>', methods=['PUT'])
def change_item_from_cart(id):
    return f"changed quantity of item {id} to "


if __name__ == '__main__':
    app.run(debug=True)
