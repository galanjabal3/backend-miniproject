from entitas.question import repositoriesDB
from util.other_util import raise_error

def find_question_db_by_id(id=0,to_model=False, materi_id=None):
    question = repositoriesDB.find_by_id(id=id, to_model=True)
    if question is None:
        raise_error(msg='Question Id not found')
    if materi_id is not None and question.materi_id != materi_id:
        raise_error(msg='Materi Id not found')
    if to_model:
        return question
    return question.to_response()

def get_question_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_question_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_question_db(json_object={}):
    question = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if question is None:
        raise_error(msg='question id not found')
    return repositoriesDB.update(json_object=json_object)

def insert_question_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_question_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def update_question_from_materi(json_object={}, to_model=False):
    return repositoriesDB.update_from_materi(json_object=json_object, to_model=to_model)

def update_question_count_used_by_id(json_object={}, to_model=False):
    return repositoriesDB.update_count_used_by_id(json_object=json_object, to_model=to_model)
