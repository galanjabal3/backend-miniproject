from entitas.user_answer import repositoriesDB
from util.other_util import raise_error

def find_user_answer_db_by_id(id=0,to_model=False):
    user_answer = repositoriesDB.find_by_id(id=id, to_model=True)
    if user_answer is None:
        raise_error(msg='user_answer id not found')
    if to_model:
        return user_answer
    return user_answer.to_response()
    
def get_user_answer_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_user_answer_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_user_answer_db(json_object={}):
    user_answer = repositoriesDB.find_by_id(id=json_object['id'], to_model=True)
    if user_answer is None:
        raise_error(msg='user_answer id not found')
    return repositoriesDB.update(json_object=json_object)

def insert_user_answer_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_user_answer_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)

def checking_question_answer(question_id=0, user_id=None, json_object={}):
    from entitas.user_score.services import insert_user_score_db
    from entitas.question.services import find_question_db_by_id, update_question_count_used_by_id, get_question_db_with_pagination
    from entitas.materi.services import find_materi_db_by_id, update_materi_question_by_id
    from entitas.user.services import find_user_db_by_id
    question = find_question_db_by_id(id=question_id, to_model=True)
    if question is None:
        raise_error(msg='Question Id not found')
    user = find_user_db_by_id(id=user_id, to_model=True)
    if user.school_id != question.school_id:
        raise_error(msg='User berbeda sekolah')
    user_answer = repositoriesDB.find_by_user_id_and_question_id(user_id=user_id, question_id=question_id, to_model=True)
    if user_answer is not None:
        raise_error(msg='Kamu sudah pernah menjawab question ini')
    count_used = question.count_used + 1
    update_question_count_used_by_id(json_object={'id': question_id, 'count_used': count_used}, to_model=False)
    json_object['answer'] = json_object['answer']
    json_object['user_id'] = user_id
    json_object['school_id'] = question.school_id
    json_object['question_id'] = question.id
    json_object['materi_id'] = question.materi_id
    count_answer_false = 0
    score = 0
    point = 0
    for item in question.answer_list:
        if json_object['answer'] == item:
            if json_object['answer'] == question.answer_true:
                point += 1
                json_object['is_correct'] = True
            if json_object['answer'] != question.answer_true:
                count_answer_false += 1
                json_object['is_correct'] = False
    datas = repositoriesDB.insert(json_object=json_object)
    data_question, _ = get_question_db_with_pagination(
        limit=0, 
        filters=[{'field': 'materi_id' , 'value': datas['materi_id']}]) 
    score = round((100 / len(data_question)) * (len(data_question) - count_answer_false))
    insert_user_score_db(json_object={
        'score' : score,
        'point' : point,
        'school_id': datas['school_id'],
        'user_id' : datas['user_id'],
        'materi_id' : datas['materi_id'],
        'count_question' : len(data_question),
        'total_question_answer' : len(question.answer_list) 
    })
    return datas

def check_user_answer_question_answer(materi_id=None, user_id=None, to_model=False):
    user = repositoriesDB.find_by_user_id_and_materi_id(user_id=user_id, materi_id=materi_id, to_model=to_model)
    if user is not None:
        return 'Kamu sudah pernah mengerjakan materi ini..'
    return