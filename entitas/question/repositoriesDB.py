import json
from database.schema import QuestionDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in QuestionDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error QuestionDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in QuestionDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])
            elif item['field'] == 'school_id':
                data_in_db = data_in_db.filter(school_id=item['value'])
            elif item['field'] == 'materi_id':
                data_in_db = data_in_db.filter(materi_id=item['value'])

        data_in_db.order_by(desc(QuestionDB.id))
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
        print('error QuestionDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in QuestionDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById QuestionDB: ', e)
        return None
    
@db_session
def update(json_object={},to_model=False):
    try:
        update_question = QuestionDB[json_object['id']]
        update_question.image = json_object['image']
        update_question.question = json_object['question']
        update_question.answer_true = json_object['answer_true']
        update_question.answer_list = json.dumps(json_object['answer_list'])
        update_question.count_used = json_object['count_used']
        update_question.publish = json_object['publish'] 
        update_question.materi_id = json_object['materi_id']
        update_question.school_id = json_object['school_id']
        commit()
        if to_model:
            update_question.to_model()
        else:
            return update_question.to_model().to_response()
    
    except Exception as e:
        print('error update QuestionDB: ', e)
        return None

@db_session
def insert(json_object={}, to_model=False):
    if 'count_used' not in json_object:
        json_object['count_used'] = 0
    if 'publish' not in json_object:
        json_object['publish'] = True
    try:
        new_materi = QuestionDB(
            image = json_object['image'],
            question = json_object['question'],
            answer_true = json_object['answer_true'],
            answer_list = json.dumps(json_object['answer_list']),
            count_used = json_object['count_used'],
            publish = json_object['publish'], 
            materi_id = json_object['materi_id'],
            school_id = json_object['school_id']
        )
        commit()
        if to_model:
            return new_materi.to_model()
        else:
            return new_materi.to_model().to_response()
    
    except Exception as e:
        print('error insert QuestionDB: ', e)
        return None
    
@db_session
def delete_by_id(id=None):
    try:
        QuestionDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById QuestionDB: ', e)
    return

@db_session
def update_from_materi(json_object={},to_model=False):
    try:
        update_question = QuestionDB[json_object['id']]
        update_question.image = json_object['image']
        update_question.question = json_object['question']
        update_question.answer_true = json_object['answer_true']
        update_question.answer_list = json.dumps(json_object['answer_list'])
        commit()
        if to_model:
            update_question.to_model()
        else:
            return update_question.to_model().to_response()
    
    except Exception as e:
        print('error update_from_materi QuestionDB: ', e)
        return None