from entitas.flyway_schema_history import repositoriesDB


def find_flyway_schema_history_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)


def get_all_flyway_schema_history_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)


def update_flyway_schema_history_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_flyway_schema_history_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data


def delete_flyway_schema_history_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)