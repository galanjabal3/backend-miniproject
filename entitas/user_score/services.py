from entitas.user_score import repositoriesDB
from util.other_util import raise_error

def find_user_score_db_by_id(id=0,to_model=False):
    user_score = repositoriesDB.find_by_id(id=id, to_model=True)
    if user_score is None:
        raise_error(msg='user_score id not found')
    if to_model:
        return user_score
    return user_score.to_response()
    
def get_user_score_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    from entitas.materi.services import find_materi_db_by_id
    datas, pagination = repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)
    for data in datas:
        materi = find_materi_db_by_id(id=data['materi_id'], to_model=True)
        data['materi'] = materi.to_response()
    return datas, pagination

def get_all_user_score_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_user_score_db(json_object={}):
    user_score = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if user_score is None:
        raise_error(msg='user_score id not found')
    return repositoriesDB.update(json_object=json_object)

def insert_user_score_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_user_score_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def get_user_score_by_materi_id(materi_id=None, user_id=None, to_model=False):
    from entitas.materi.services import find_materi_db_by_id
    datas = repositoriesDB.get_all_by_materi_id_and_user_id(materi_id=materi_id, user_id=user_id, to_model=to_model)
    for item in datas:
        materi = find_materi_db_by_id(id=item['materi_id'], to_model=True)
        item['materi'] =  materi.to_response()
    return datas
