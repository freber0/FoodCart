import flask
from foodcart.persistance import UserRepository
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from foodcart.forms.LoginForm import LoginForm

app = flask.Flask(__name__)
app.secret_key = 'tDo4f]$QQa#mk,gyL+(+BsNQp'
login_manager = LoginManager()


@app.route('/')
def hello():
    return flask.render_template('accueil.html')


@app.route('/cart/<id>')
def add_to_cart(id):
    return f"Ajout du produit avec le id {id} au panier"


# @app.route('/login')
# def login_page():
#     return render_template('login.html')
#
#
# @app.route('/login', methods=['POST'])
# def authentication():
#
#     username = request.form['u']
#     password = request.form['p']
#     cursor.execute("USE FoodCart;")
#     cursor.execute("SELECT * FROM user WHERE username='" + username + "' AND password='" + password + "';")
#     data = cursor.fetchone()
#
#     if data is None:
#         return "Mauvais Username ou Mot de Passe"
#     else:
#         return "Vous êtes connecté"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(flask.request.form)
    if form.validate_on_submit():
        user = UserRepository.get_user_from_username(form.username.data)
        login_user(user)

        flask.flash('Logged in successfully.')
        return flask.redirect(flask.url_for('hello'))
    return flask.render_template('login.html', form=form)


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run(debug=True)  # pas besoin de reboot Flask