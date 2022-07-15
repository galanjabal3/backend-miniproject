import uuid
from database.schema import UserDB
from pony.orm import *
from util.other_util import encrypt_string

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in UserDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error UserDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])
            elif item['field'] == 'school_id':
                data_in_db = data_in_db.filter(school_id= item['value'])
            elif item['field'] == 'email':
                data_in_db = data_in_db.filter(email = item['value'])
            elif item['field'] == 'username':
                data_in_db = data_in_db.filter(username = item['value'])
            elif item['field'] == 'guest':
                data_in_db = data_in_db.filter(guest = item['value'])

        data_in_db.order_by(desc(UserDB.id))
        total_record = data_in_db.count()
        if limit >0:
            data_in_db = data_in_db.page(pagenum=page, pagesize=limit)
        else:
            data_in_db = data_in_db
        for item in data_in_db:
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())

    except Exception as e:
        print('error UserDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in UserDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById UserDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    if json_object is None:
        return None
    if json_object['guest'] not in json_object:
        json_object['guest'] = 0
    if json_object['blocked'] not in json_object:
        json_object['blocked'] = 0
    if json_object['device'] not in json_object:
        json_object['device'] = ''
    try:
        update_user = UserDB[json_object['id']]
        update_user.username = json_object['username']
        update_user.email = json_object['email']
        update_user.school_id = json_object['school_id']
        update_user.device = json_object['device']
        update_user.blocked = json_object['blocked']
        update_user.guest = json_object['guest']
        commit()
        if to_model:
            update_user.to_model()
        else:
            return update_user.to_model().to_response()
    
    except Exception as e:
        print('error update UserDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    if 'school_id' not in json_object:
        json_object['school_id'] = 0
    if 'guest' not in json_object:
        json_object['guest'] = False
    if 'blocked' not in json_object:
        json_object['blocked'] = False
    if 'device' not in json_object:
        json_object['device'] = ''
    if 'avatar' not in json_object:
        json_object['avatar'] = ''
    try:
        new_user = UserDB(
            username = json_object['username'],
            password = encrypt_string(json_object['password']),
            avatar = json_object['avatar'],
            email = json_object['email'],
            school_id = json_object['school_id'],
            roles = str(json_object['roles']),
            guest = json_object['guest'],
            device = json_object['device'],
            blocked = json_object['blocked'],
            token = str(uuid.uuid4())
        )
        commit()
        if to_model:
            return new_user.to_model()
        else:
            return new_user.to_model().to_response()
    
    except Exception as e:
        print('error insert UserDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        UserDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById UserDB: ', e)
    return

@db_session
def post_login(json_object={}):
    try:
        if json_object['email'] not in ['','-']:
            user_db = UserDB.get(email=json_object['email'], password=encrypt_string(json_object['password']))
        if user_db is not None:
            user_db.token = str(uuid.uuid4())
            commit()
            return user_db.to_model()

    except Exception as e:
        print('error UserDB post_login: ', e)
    return None

@db_session
def find_by_email(email='', to_model=False):
    try:
        account = UserDB.get(email=email)
        if account is None:
            return None
        if to_model:
            return account.to_model()
        else:
            return account.to_model().to_response()
    except Exception as e:
        print('error UserDB find_by_email: ', e)
        return None

@db_session
def reset_token(json_object=None, to_model=False):
    if json_object is None:
        return None
    try:
        updated_token_user = UserDB[json_object['id']]
        updated_token_user.token = ''
        commit()
        if to_model:
            updated_token_user.to_model()
        else:
            return updated_token_user.to_model().to_response()
    except Exception as e:
        print('error User reset Token: ', e)
        return None
    
@db_session
def update_profile_user(json_object={}, to_model=False):
    try:
        update_user = UserDB[json_object['id']]
        if 'username' in json_object:
            update_user.username = json_object['username'] 
        if 'avatar' in json_object:
            update_user.avatar = json_object['avatar']
        if 'email' in json_object:
            update_user.email = json_object['email']
        commit()
        if to_model:
            update_user.to_model()
        else:
            return update_user.to_model().to_response_profile()
    except Exception as e:
        print('error update_profile_user: ', e)
        return None
    
@db_session
def update_user_school_id_by_id(id=0, school_id=0, to_model=False):
    try:
        update_school_id = UserDB[id]
        update_school_id.school_id = school_id
        update_school_id.guest = False
        commit()
        if to_model:
            update_school_id.to_model()
        else:
            return update_school_id.to_model().to_response()
    except Exception as e:
        print('error update_user_school_id_by_id: ', e)
        return None
    
@db_session
def find_by_device(device='', to_model=False):
    try:
        data = select(s for s in UserDB if s.device == device)
        if data.count() == 0:
            return None
        if to_model:
            return data.first().to_model()
        else:
            return data.first().to_model()
    except Exception as e:
        print('error find_by_device: ', e)
        return None