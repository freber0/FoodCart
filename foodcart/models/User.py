class User(object):
    def __init__(self, username, password, lastname, firstname, email, address):
        self.address = address
        self.lastname = lastname
        self.firstname = firstname
        self.password = password
        self.email = email
        self.username = username

