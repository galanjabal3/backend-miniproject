import json
from database.schema import UserAnswerDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in UserAnswerDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error UserAnswerDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserAnswerDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])
            elif item['field'] == 'user_id':
                data_in_db = data_in_db.filter(user_id=item['value'])
            elif item['field'] == 'school_id':
                data_in_db = data_in_db.filter(school_id=item['value'])
            elif item['field'] == 'materi_id':
                data_in_db = data_in_db.filter(materi_id=item['value'])
            elif item['field'] == 'question_id':
                data_in_db = data_in_db.filter(question_id=item['value'])

        data_in_db.order_by(desc(UserAnswerDB.id))
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
        print('error UserAnswerDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in UserAnswerDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById UserAnswerDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    try:
        update_user_answer = UserAnswerDB[json_object['id']]
        update_user_answer.is_correct = json_object['is_correct']
        update_user_answer.answer = json_object['answer']
        update_user_answer.user_id = json_object['user_id']
        update_user_answer.school_id = json_object['school_id']
        update_user_answer.question_id = json_object['question_id']
        update_user_answer.materi_id = json_object['materi_id']
        commit()
        if to_model:
            update_user_answer.to_model()
        else:
            return update_user_answer.to_model().to_response()
    
    except Exception as e:
        print('error update UserAnswerDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    try:
        new_user_answer = UserAnswerDB(
            is_correct = json_object['is_correct'],
            answer = json_object['answer'],
            user_id = json_object['user_id'],
            school_id = json_object['school_id'],
            question_id = json_object['question_id'],
            materi_id = json_object['materi_id']
        )
        commit()
        if to_model:
            return new_user_answer.to_model()
        else:
            return new_user_answer.to_model().to_response()
    
    except Exception as e:
        print('error insert UserAnswerDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        UserAnswerDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById UserAnswerDB: ', e)
    return

@db_session
def find_by_user_id_and_question_id(user_id=0, question_id=0, to_model=False):
    try:
        for item in select(s for s in UserAnswerDB if s.user_id == user_id and s.question_id == question_id):
            if to_model:
                return item.to_model()
            else:
                return item.to_model().to_response()
    except Exception as e:
        print('error find_by_user_id_and_question_id: ', e)
        return None
    
@db_session
def get_all_by_question_id(question_id=0):
    result = []
    try:
        for item in select(s for s in UserAnswerDB if s.question_id == question_id):
            result.append(item.to_model())
    except Exception as e:
        print('error get_all_by_question_id: ', e)
        return None
    
@db_session
def find_by_user_id_and_materi_id(user_id=0, materi_id=0, to_model=False):
    try:
        for item in select(s for s in UserAnswerDB if s.user_id == user_id and s.materi_id == materi_id):
            if to_model:
                return item.to_model()
            else:
                return item.to_model().to_response()
    except Exception as e:
        print('error find_by_user_id_and_materi_id: ', e)
        return None