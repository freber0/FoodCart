import flask
from foodcart.persistance import UserRepository
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from foodcart.forms.LoginForm import LoginForm

app = flask.Flask(__name__)
app.secret_key = 'tDo4f]$QQa#mk,gyL+(+BsNQp'
login_manager = LoginManager()


@app.route('/')
@login_required
def hello():
    print(current_user.get_id())
    return flask.render_template('accueil.html')


@app.route('/cart/<id>')
@login_required
def add_to_cart(id):
    return f"Ajout du produit avec le id {id} au panier"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    return flask.render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(flask.request.form)
    if form.validate_on_submit():
        user = user_loader(form.username.data)
        if user and user.check_pwd(form.password.data):
            login_user(user)
            flask.flash('Logged in successfully.')
            return flask.redirect(flask.url_for('hello'))
        else:
            flask.flash('Invalid username or password. Please try again')
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


if __name__ == '__main__':
    login_manager.init_app(app)
    app.run(debug=True)
