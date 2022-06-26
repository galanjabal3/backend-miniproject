from entitas.materi import repositoriesDB
from util.other_util import raise_error

def find_materi_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)

def get_materi_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_materi_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_materi_db(json_object={}):
    materi = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if materi is None:
        raise_error(msg='materi id not found')
    return repositoriesDB.update(json_object=json_object)

def insert_materi_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_materi_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)