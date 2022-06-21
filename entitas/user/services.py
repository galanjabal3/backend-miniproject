from entitas.user import repositoriesDB

def find_user_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)

def get_user_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_user_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)


def update_user_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_user_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_user_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def update_profile_user_db(json_object={}):
    user = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if user is None:
        return None, 'User tidak di temukan'
    return repositoriesDB.update_profile_user(json_object=json_object)

def get_profile_user_db(json_object={}):
    user = repositoriesDB.find_by_id(id=json_object['user']['id'], to_model=True)
    if user is None:
        return None
    return user.to_response_profile()
    
def login_user(json_object={}):
    from util.jwt_util import jwt_encode
    user_info = repositoriesDB.post_login(json_object=json_object)
    if user_info is None:
        return None, 'Email atau password tidak sesuai'
    user = user_info.to_response_login()
    return jwt_encode(user), 'success'

def signup_user_db(json_object={}):
    from util.constant import EMAIL_MUST_FILL
    from util.jwt_util import jwt_encode, check_valid_email
    import uuid
    if 'email' not in json_object:
        return {'token': '', 'message': EMAIL_MUST_FILL }
    
    if 'school_id' not in json_object:
        json_object['school_id'] = 0
    json_object['token'] = str(uuid.uuid4())
    if 'role' not in json_object:
        json_object['role'] = 'ADMIN'
    if not check_valid_email(email=json_object['email']):
        return {'token': '', 'message': 'Email tidak valid'}
    email = repositoriesDB.find_by_email(email=json_object['email'], to_model=True)
    
    if email is None:
        account_info = repositoriesDB.insert(json_object=json_object, to_model=True)
        return jwt_encode(account_info.to_response_login())
    else:
        return {'token': '', 'message': 'Email sudah dipakai'}
    