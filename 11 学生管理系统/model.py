import Tools


class Teachers(object):
    def __init__(self, username, password):
        self.username = username
        self.password = Tools.encrypt_password(password)
