import uuid
from entitas.user_traffic import repositoriesDB
from util.jwt_util import jwt_encode
from util.other_util import raise_error, get_random_string

def find_user_traffic_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)

def get_user_traffic_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_user_traffic_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_user_traffic_db(json_object={}):
    user_traffic = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if user_traffic is None:
        raise_error(msg='user_traffic id not found')
    return repositoriesDB.update(json_object=json_object)

def insert_user_traffic_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_user_traffic_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def get_traffic_global_user():
    from entitas.user.services import insert_user_db, find_user_db_by_device, login_user
    import socket
    json_object = {}
    device = socket.gethostname()
    user_auth = find_user_db_by_device(device=device, to_model=True)
    if user_auth is None:
        visitors = repositoriesDB.get_all(to_model=True)
        roles = []
        roles.append("USER")
        user = insert_user_db(json_object={
            'username': 'guest_' + get_random_string(6),
            'password': '',
            'avatar': '',
            'email': '',
            'roles': roles,
            'guest': True,
            'token': str(uuid.uuid4),
            'school_id': 0,
            'blocked': False,
            'device': device
        }, to_model=True)
        users = jwt_encode(user.to_response_login())
        json_object['user_id'] = users['id']
        json_object['school_id'] = 0
        json_object['visitors'] = len(visitors) + 1
        json_object['users'] = users
        data = repositoriesDB.insert(json_object=json_object)
        return data['users']
    else:
        return jwt_encode(user_auth.to_response_login())