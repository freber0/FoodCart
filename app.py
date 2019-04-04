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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(flask.request.form)
    if form.validate_on_submit():
        user = user_loader(form.username.data)
        if user and user.check_pwd(form.password.data):
            login_user(user)
            flask.flash('Logged in successfully.')
            return flask.redirect(flask.url_for('hello'))
    return flask.render_template('login.html', form=form)


@login_manager.user_loader
def user_loader(user_id):
    return UserRepository.get_user_from_username(user_id)


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run(debug=True)
