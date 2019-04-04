from werkzeug.security import generate_password_hash, check_password_hash

class User(object):
    def __init__(self, username, password, lastname, firstname, email, address):
        self.address = address
        self.lastname = lastname
        self.firstname = firstname
        self.password = password
        self.email = email
        self.username = username
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False

    def set_pwd(self, pwd):
        self.password = generate_password_hash(pwd)

    def check_pwd(self, pwd):
        return check_password_hash(self.password, pwd)

    def get_id(self):
        return self.username

    def is_authenticaed(self):
        return self.is_authenticated

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return self.is_anonymous