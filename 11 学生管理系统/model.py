import Tools


class Teachers(object):
    def __init__(self, username, password):
        self.username = username
        self.password = Tools.encrypt_password(password)


class Students(object):
    def __init__(self, name, age, gender, tel):
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
