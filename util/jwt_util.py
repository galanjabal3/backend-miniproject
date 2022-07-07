from datetime import datetime, timedelta
import jwt
from config.config import secret_jwt
def portprq_auth(payload):
    window = timedelta(seconds=3)
    now = datetime.utcnow()
    if now - datetime.utcfromtimestamp(payload['exp']) >= window:
        return None
    return payload

def jwt_encode(user_info=None):
    if user_info['token'] != '':
        # user_info['exp'] = int((datetime.utcnow() + timedelta(days=300)).timestamp())
        # user_info['token'] = jwt.encode(user_info, secret_jwt,algorithm='HS512').decode("utf-8")
        user_info['exp'] = int((datetime.utcnow() + timedelta(days=300)).timestamp())
        try:
            user_info['token'] = jwt.encode(user_info,secret_jwt,algorithm='HS512').decode("utf-8")
        except:
            user_info['token'] = jwt.encode(user_info, secret_jwt, algorithm='HS512')
    return user_info

def check_valid_email(email=''):
    import re
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    return re.search(regex, email)

