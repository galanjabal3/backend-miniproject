from entitas.school import repositoriesDB


def find_school_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)

def get_school_db_with_pagination(page=1, limit=9, filters=[], to_model=False):
    return repositoriesDB.get_all_with_pagination(page=page, limit=limit, filters=filters, to_model=to_model)

def get_all_school_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)

def update_school_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)

def insert_school_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data

def delete_school_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)