from database.schema import TrafficRecapDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in TrafficRecapDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error TrafficRecapDB get_all: ', e)
    return result

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in TrafficRecapDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById TrafficRecapDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    try:
        update_traffic_recap = TrafficRecapDB[json_object['id']]
        update_traffic_recap.visitors = json_object['visitors']
        update_traffic_recap.this_date = json_object['this_date']
        update_traffic_recap.school_id = json_object['school_id']
        commit()
        if to_model:
            update_traffic_recap.to_model()
        else:
            return update_traffic_recap.to_model().to_response()
    
    except Exception as e:
        print('error update TrafficRecapDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    try:
        new_traffic_recap = TrafficRecapDB(
            visitors = json_object['visitors'],
            this_date = json_object['this_date'],
            school_id = json_object['school_id']
        )
        commit()
        if to_model:
            return new_traffic_recap.to_model()
        else:
            return new_traffic_recap.to_model().to_response()
    
    except Exception as e:
        print('error insert TrafficRecapDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        TrafficRecapDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById TrafficRecapDB: ', e)
    return