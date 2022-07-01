from database.schema import UserScoreDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in UserScoreDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error UserScoreDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserScoreDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])
            elif item['field'] == 'user_id':
                data_in_db = data_in_db.filter(user_id=item['value'])
            elif item['field'] == 'school_id':
                data_in_db = data_in_db.filter(school_id=item['value'])
            elif item['field'] == 'materi_id':
                data_in_db = data_in_db.filter(materi_id=item['value'])

        data_in_db.order_by(desc(UserScoreDB.id))
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
        print('error UserScoreDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in UserScoreDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById UserScoreDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    try:
        update_user_score = UserScoreDB[json_object['id']]
        update_user_score.score = json_object['score']
        update_user_score.point = json_object['point']
        update_user_score.user_id = json_object['user_id']
        update_user_score.school_id = json_object['school_id']
        update_user_score.count_question = json_object['count_question']
        update_user_score.materi_id = json_object['materi_id']
        update_user_score.total_question_answer = json_object['total_question_answer']
        commit()
        if to_model:
            update_user_score.to_model()
        else:
            return update_user_score.to_model().to_response()
    
    except Exception as e:
        print('error update UserScoreDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    try:
        new_user_score = UserScoreDB(
            score = json_object['score'],
            point = json_object['point'],
            user_id = json_object['user_id'],
            school_id = json_object['school_id'],
            count_question = json_object['count_question'],
            materi_id = json_object['materi_id'],
            total_question_answer = json_object['total_question_answer']
        )
        commit()
        if to_model:
            return new_user_score.to_model()
        else:
            return new_user_score.to_model().to_response()
    
    except Exception as e:
        print('error insert UserScoreDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        UserScoreDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById UserScoreDB: ', e)
    return

@db_session
def get_all_by_materi_id_and_user_id(materi_id=0, user_id=None, to_model=False):
    result = []
    try:
        for item in select(s for s in UserScoreDB if s.materi_id == materi_id and s.user_id == user_id):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error get_all_by_materi_id_and_user_id: ', e)
    return result