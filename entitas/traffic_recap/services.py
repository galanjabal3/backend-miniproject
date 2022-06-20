from entitas.traffic_recap import repositoriesDB


def find_traffic_recap_db_by_id(id=0,to_model=False):
    return repositoriesDB.find_by_id(id=id, to_model=to_model)


def get_all_traffic_recap_db(to_model=False):
    return repositoriesDB.get_all(to_model=to_model)


def update_traffic_recap_db(json_object={}):
    return repositoriesDB.update(json_object=json_object)


def insert_traffic_recap_db(json_object={}):
    data = repositoriesDB.insert(json_object=json_object)
    return data


def delete_traffic_recap_by_id(id=0):
    return repositoriesDB.delete_by_id(id=id)