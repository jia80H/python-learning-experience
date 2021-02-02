import hashlib


def encrypt_password(password, x = 'avsbtrbdscsd'):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))  # 加密
    h.update(x.encode('utf8'))  # 再加密
    return h.hexdigest()