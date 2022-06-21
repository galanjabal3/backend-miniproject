from database.schema import SchoolDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in SchoolDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error SchoolDB get_all: ', e)
    return result

@db_session   
def get_all_with_pagination(page=1,limit=9,filters=[],to_model=False):
    result = []
    total_record = 0
    try:
        data_in_db = select(s for s in SchoolDB)
        for item in filters:
            if item['field'] == 'id':
                data_in_db = data_in_db.filter(id=item['value'])
            elif item['field'] == 'name':
                data_in_db = data_in_db.filter(name= item['value'])
            elif item['field'] == 'head_master':
                data_in_db = data_in_db.filter(head_master = item['value'])

        data_in_db.order_by(desc(SchoolDB.id))
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
        print('error SchoolDB getAllWithPagination: ', e)
    return result, {'total': total_record, 'page': page, 'total_page': (total_record + limit - 1)//limit if limit >0 else 1}

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in SchoolDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById SchoolDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    try:
        update_school = SchoolDB[json_object['id']]
        update_school.head_master = json_object['head_master']
        update_school.name = json_object['name']
        update_school.phone_number = json_object['phone_number']
        update_school.address = json_object['address']
        update_school.update_by = json_object['update_by']
        commit()
        if to_model:
            update_school.to_model()
        else:
            return update_school.to_model().to_response()
    
    except Exception as e:
        print('error update SchoolDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    try:
        new_school = SchoolDB(
            head_master = json_object['head_master'],
            name = json_object['name'],
            phone_number = json_object['phone_number'],
            address = json_object['address']
        )
        commit()
        if to_model:
            return new_school.to_model()
        else:
            return new_school.to_model().to_response()
    
    except Exception as e:
        print('error insert SchoolDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        SchoolDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById SchoolDB: ', e)
    return