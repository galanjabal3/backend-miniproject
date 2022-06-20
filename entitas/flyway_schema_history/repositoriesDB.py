from database.schema import FlywaySchemaHistoryDB
from pony.orm import *

@db_session
def get_all(to_model=False):
    result = []
    try:
        for item in select(s for s in FlywaySchemaHistoryDB):
            if to_model:
                result.append(item.to_model())
            else:
                result.append(item.to_model().to_response())
    except Exception as e:
        print('error FlywaySchemaHistoryDB get_all: ', e)
    return result

@db_session
def find_by_id(id=None, to_model=False):
    try:
        data_in_db = select(s for s in FlywaySchemaHistoryDB if s.id == id)
        if data_in_db.count() == 0:
            return None
        if to_model:
            return data_in_db.first().to_model()
        else:
            return data_in_db.first().to_model().to_response()
    
    except Exception as e:
        print('error findById FlywaySchemaHistoryDB: ', e)
        return None

@db_session
def update(json_object={},to_model=False):
    try:
        update_flyway_schema_history = FlywaySchemaHistoryDB[json_object['id']]
        update_flyway_schema_history.version = json_object['version']
        update_flyway_schema_history.description = json_object['description']
        update_flyway_schema_history.type = json_object['type']
        update_flyway_schema_history.script = json_object['script']
        update_flyway_schema_history.checksum = json_object['checksum']
        update_flyway_schema_history.installed_by = json_object['installed_by']
        update_flyway_schema_history.installed_on = json_object['installed_on']
        update_flyway_schema_history.execution_time = json_object['execution_time']
        update_flyway_schema_history.success = json_object['success']
        commit()
        if to_model:
            update_flyway_schema_history.to_model()
        else:
            return update_flyway_schema_history.to_model().to_response()
    
    except Exception as e:
        print('error update FlywaySchemaHistoryDB: ', e)
        return None
    
@db_session
def insert(json_object={}, to_model=False):
    try:
        new_flyway_schema_history = FlywaySchemaHistoryDB(
            version = json_object['version'],
            description = json_object['description'],
            type = json_object['type'],
            script = json_object['script'],
            checksum = json_object['checksum'],
            installed_by = json_object['installed_by'],
            installed_on = json_object['installed_on'],
            execution_time = json_object['execution_time'],
            success = json_object['success']
        )
        commit()
        if to_model:
            return new_flyway_schema_history.to_model()
        else:
            return new_flyway_schema_history.to_model().to_response()
    
    except Exception as e:
        print('error insert FlywaySchemaHistoryDB: ', e)
        return None

@db_session
def delete_by_id(id=None):
    try:
        FlywaySchemaHistoryDB[id].delete()
        commit()
        return True
    except Exception as e:
        print('error deleteById FlywaySchemaHistoryDB: ', e)
    return