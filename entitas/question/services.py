from entitas.question import repositoriesDB
from util.other_util import raise_error

def find_question_db_by_id(id=0,to_model=False, materi_id=None, school_id=None):
    question = repositoriesDB.find_by_id(id=id, to_model=True)
    if question is None:
        raise_error(msg='Question Id not found')
    if materi_id is not None and question.materi_id != materi_id:
        raise_error(msg='Materi Id not found')
    if school_id is not None and question.school_id != school_id:
        raise_error(msg='School id not found')
    if to_model:
        return question
    return question.to_response()

def get_question_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_question_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_question_db(json_object={}, materi_id=None, school_id=None):
    import base64
    question = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if question is None:
        raise_error(msg='question id not found')
    if materi_id is not None and question.materi_id != materi_id:
        raise_error(msg='Materi id not match')
    if school_id is not None and question.school_id != school_id:
        raise_error(msg='School id not match')
    return repositoriesDB.update(json_object=json_object)

def insert_question_db(json_object={}):
    from entitas.materi.services import update_materi_db_question_total
    question = repositoriesDB.insert(json_object=json_object)
    data = repositoriesDB.get_question_by_materi_id(materi_id=question['materi_id'], school_id=question['school_id'], to_model=True)
    update_materi_db_question_total(id=question['materi_id'], question_total=len(data))
    return question

def delete_question_by_id(id=0, materi_id=None, school_id=None):
    question = repositoriesDB.find_by_id(id=id, to_model=True)
    if question is None:
        raise_error(msg='question id not found')
    if materi_id is not None and question.materi_id != materi_id:
        raise_error(msg='Materi id not match')
    if school_id is not None and question.school_id != school_id:
        raise_error(msg='School id not match')
    return repositoriesDB.delete_by_id(id=id)

def update_question_from_materi(json_object={}, to_model=False):
    return repositoriesDB.update_from_materi(json_object=json_object, to_model=to_model)

def update_question_count_used_by_id(json_object={}, to_model=False):
    return repositoriesDB.update_count_used_by_id(json_object=json_object, to_model=to_model)
