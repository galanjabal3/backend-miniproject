import hashlib
import random


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def raise_error(msg=""):
    import falcon
    raise falcon.HTTPBadRequest(msg)

def get_random_string(length):
    sample_letters = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join((random.choice(sample_letters) for i in range(length)))