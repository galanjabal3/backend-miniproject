from entitas.materi import repositoriesDB
from util.other_util import raise_error

def find_materi_db_by_id(id=0,to_model=False):
    materi = repositoriesDB.find_by_id(id=id, to_model=True)
    if materi is None:
        raise_error(msg='Materi Id not found')
    if to_model:
        return materi
    return materi.to_response()

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

def create_question_from_materi(json_object={}, roles='', school_id=None):
    from entitas.school.services import find_school_db_by_id
    from entitas.question.services import insert_question_db
    if roles != 'ADMIN':
        raise_error(msg='Kamu tidak admin')
    school = find_school_db_by_id(id=school_id, to_model=True)
    if school is None:
        raise_error(msg='School id tidak ditemukan')
    json_object['school_id'] = school.id
    json_object['question_total'] = len(json_object['question'])
    materi = repositoriesDB.insert(json_object=json_object)
    questions = []
    for item in materi['question']:
        question = insert_question_db(json_object={
            'image': item['image'],
            'question': item['question'],
            'answer_true': item['answer_true'],
            'answer_list': item['answer_list'],
            'materi_id': materi['id'],
            'school_id': materi['school_id']
        }) 
        questions.append(question)
        materi['question'] = questions
    repositoriesDB.update(json_object=materi)
    return materi

def update_question_from_materi(json_object={}, roles=''):
    from entitas.question.services import update_question_from_materi
    if roles != 'ADMIN':
        raise_error(msg='Kamu tidak admin')
    data = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if data is None:
        raise_error(msg='Materi Id not found')
    json_object['question_total'] = len(json_object['question'])
    json_object['school_id'] = data.school_id
    materi = repositoriesDB.update(json_object=json_object)
    questions = []
    for item in materi['question']:
        question = update_question_from_materi(json_object={
            'id': item['id'],
            'image': item['image'],
            'question': item['question'],
            'answer_true': item['answer_true'],
            'answer_list': item['answer_list']
        })
        
        questions.append(question)
        materi['question'] = questions
    repositoriesDB.update(json_object=materi)
    return materi

def find_question_materi_from_user(id=0, to_model=False):
    materi = repositoriesDB.find_by_id(id=id, to_model=True)
    if materi is None:
        raise_error(msg='Materi Id not found')
    for item in materi.question:
        item['answer_true'] = ''
    if to_model:
        return materi
    return materi.to_response()