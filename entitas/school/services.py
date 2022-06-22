from entitas.school import repositoriesDB
from util.other_util import raise_error

def find_school_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)

def get_school_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_school_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_school_db(json_object={}):
    school = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if school is None:
        raise_error(msg='School id not found')
    return repositoriesDB.update(json_object=json_object)

def insert_school_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_school_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def update_school_registration_db(json_object={}, user_id=None):
    from entitas.user.services import find_user_db_by_id
    school = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if school is None:
        raise_error(msg='School id not found')
    user = find_user_db_by_id(id=user_id, to_model=True)
    if school.id != user.school_id:
        raise_error(msg='School id not the same')
    json_object['update_by'] = user.username
    return repositoriesDB.update(json_object=json_object)