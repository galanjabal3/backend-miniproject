import json
from database.schema import UserTrafficDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in UserTrafficDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error UserTrafficDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in UserTrafficDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])

        data_in_db.order_by(desc(UserTrafficDB.id))
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
        print('error UserTrafficDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in UserTrafficDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById UserTrafficDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    try:
        update_user_traffic = UserTrafficDB[json_object['id']]
        update_user_traffic.visitors = json_object['visitors']
        update_user_traffic.user_id = json_object['user_id']
        update_user_traffic.school_id = json_object['school_id']
        commit()
        if to_model:
            update_user_traffic.to_model()
        else:
            return update_user_traffic.to_model().to_response()
    
    except Exception as e:
        print('error update UserTrafficDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    try:
        new_user_traffic = UserTrafficDB(
            visitors = json_object['visitors'],
            user_id = json_object['user_id'],
            school_id = json_object['school_id'],
            users = json.dumps(json_object['users'])
        )
        commit()
        if to_model:
            return new_user_traffic.to_model()
        else:
            return new_user_traffic.to_model().to_response()
    
    except Exception as e:
        print('error insert UserTrafficDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        UserTrafficDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById UserTrafficDB: ', e)
    return