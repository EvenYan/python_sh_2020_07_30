import hashlib


def gen_secret(passwd):
    md5 = hashlib.md5()
    md5.update(passwd.encode("utf-8"))
    return md5.hexdigest()