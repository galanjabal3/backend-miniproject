from database.schema import MateriDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in MateriDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error MateriDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in MateriDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])
            elif item['field'] == 'school_id':
                data_in_db = data_in_db.filter(school_id=item['value'])

        data_in_db.order_by(desc(MateriDB.id))
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
        print('error MateriDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in MateriDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById MateriDB: ', e)
        return None
    
@db_session
def update(json_object={},to_model=False):
    try:
        update_materi = MateriDB[json_object['id']]
        update_materi.description = json_object['description']
        update_materi.question_total = json_object['question_total']
        update_materi.teacher = json_object['teacher']
        update_materi.materi = json_object['materi']
        update_materi.school_id = json_object['school_id']
        commit()
        if to_model:
            update_materi.to_model()
        else:
            return update_materi.to_model().to_response()
    
    except Exception as e:
        print('error update MateriDB: ', e)
        return None

@db_session
def insert(json_object={}, to_model=False):
    try:
        new_materi = MateriDB(
            description = json_object['description'],
            question_total = json_object['question_total'],
            teacher = json_object['teacher'],
            materi = json_object['materi'],
            school_id = json_object['school_id']
        )
        commit()
        if to_model:
            return new_materi.to_model()
        else:
            return new_materi.to_model().to_response()
    
    except Exception as e:
        print('error insert MateriDB: ', e)
        return None
    
@db_session
def delete_by_id(id=None):
    try:
        MateriDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById MateriDB: ', e)
    return