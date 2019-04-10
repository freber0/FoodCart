import flask
from foodcart.persistance import UserRepository, OrderRepository, ProductRepository
from foodcart.models.User import User
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from foodcart.forms.LoginForm import LoginForm
from foodcart.forms.SignupForm import SignupForm
from foodcart.forms.UpdateForm import UpdateForm
from foodcart.forms.SearchForm import search

app = flask.Flask(__name__)
app.secret_key = 'tDo4f]$QQa#mk,gyL+(+BsNQp'
login_manager = LoginManager()


@app.route('/')
@login_required
def root_page():
    return flask.redirect(flask.url_for('home_page'))


@app.route('/home')
@login_required
def home_page():
    products = ProductRepository.get_all()
    return flask.render_template('accueil.html', data=products)


@app.route('/search', methods=['GET', 'POST'])
@login_required
def search_page():
    products = search()
    return flask.render_template('results.html', data=products)


@app.route('/about')
@login_required
def about_page():
    return flask.render_template('about.html')


@app.route('/cart')
@login_required
def cart_page():
    cart_list = []
    quantity_info = []
    sous_total = 0
    total = 0
    for item in flask.session['cart']:
        for item_id, item_qty in item.items():
            info = ProductRepository.get_info_cart_item(item_id)
            cart_list += info
            price = ProductRepository.get_price_item(item_id)
            sous_total = price[0][0] * int(item_qty)
            total += sous_total
            quantity_info.append(item_qty)
    if not cart_list:
        flask.flash('Votre panier est vide!')
    return flask.render_template('cart.html', data=cart_list, quantity=quantity_info, total=total)


@app.route('/account', methods=['GET', 'POST'])
@login_required
def account_page():
    form = UpdateForm(flask.request.form)

    if form.validate_on_submit():
        user = User(current_user.get_id(), None, form.last_name.data, form.first_name.data, form.email.data,
                    form.address.data)
        user.set_pwd(form.password.data)
        UserRepository.update_user(user)
        flask.flash('Vos informations ont été mises à jour!')
        return flask.redirect(flask.url_for('account_page'))

    return flask.render_template('account.html')


@app.route('/cart/<id>', methods=['POST'])
@login_required
def add_to_cart(id):
    if current_user.is_authenticated:
        if 'cart' in flask.session:
            if any(id in item for item in flask.session['cart']):
                for item in flask.session['cart']:
                    for item_id, item_qty in item.items():
                        if item_id == id:
                            item.update({item_id: flask.request.get_json()['quantity'] + item_qty})
            else:
                flask.session['cart'].append({id: flask.request.get_json()['quantity']})
        else:
            flask.session['cart'] = [{id: flask.request.get_json()['quantity']}]
    else:
        return flask.redirect(flask.url_for('login'))
    flask.session.modified = True
    print(flask.session['cart'])
    return 'Success', 200


@app.route('/cart/<id>', methods=['DELETE'])
@login_required
def remove_from_cart(id):
    if current_user.is_authenticated:
        if 'cart' in flask.session:
            for item in flask.session['cart']:
                for item_id, item_qty in item.items():
                    if item_id == id:
                        flask.session['cart'].remove(item)
    else:
        return flask.redirect(flask.url_for('login'))
    flask.session.modified = True
    print(flask.session['cart'])
    return 'Succes', 200


@app.route('/checkout', methods=['GET'])
@login_required
def checkout():
    OrderRepository.add_checkout_items(user_loader(current_user.get_id()), flask.session['cart'])
    flask.session['cart'] = []
    return 'Success', 200


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('root_page'))

    form = SignupForm(flask.request.form)
    if form.validate_on_submit():
        user = user_loader(form.username.data)
        print(user)
        if not user:
            user = User(form.username.data, None, form.last_name.data, form.first_name.data, form.email.data,
                        form.address.data)
            user.set_pwd(form.password.data)
            UserRepository.add_user(user)
            return flask.redirect(flask.url_for('login'))
        else:
            flask.flash('Ce mot de passe est déjà utilisé. Veuillez en choisir un autre')
    return flask.render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return flask.redirect(flask.url_for('root_page'))

    form = LoginForm(flask.request.form)
    if form.validate_on_submit():
        user = user_loader(form.username.data)
        if user and user.check_pwd(form.password.data):
            login_user(user)
            return flask.redirect(flask.url_for('root_page'))
        else:
            flask.flash("Mauvais mot de passe ou nom d'usager")
    return flask.render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return flask.redirect("login")


@login_manager.user_loader
def user_loader(user_id):
    return UserRepository.get_user_from_username(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return flask.redirect("login")


@app.route('/fruits')
def show_fruit():
    fruits = ProductRepository.get_fruit()
    return flask.render_template('fruits.html', data=fruits)


@app.route('/legumes')
def show_legume():
    legumes = ProductRepository.get_legume()
    return flask.render_template('legume.html', data=legumes)


@app.route('/viandes')
def show_viandes():
    viandes = ProductRepository.get_viande()
    return flask.render_template('viandes.html', data=viandes)


@app.route('/boulangerie')
def show_pains():
    pains = ProductRepository.get_pains()
    return flask.render_template('boulangerie.html', data=pains)


@app.route('/produit_laitier')
def show_lait():
    lait = ProductRepository.get_produit_laitier()
    return flask.render_template('produit_laitier.html', data=lait)


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run(debug=True)
