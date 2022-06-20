
class School:
    def __init__(self, id=0, head_master='', name='', phone_number='', address='', create_date=None, update_date=None, update_by=''):
        self.id = id
        self.head_master = head_master
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.create_date = create_date
        self.update_date = update_date
        self.update_by = update_by
        
    def to_json(self):
        return {
            'id' : self.id,
            'head_master': self.head_master,
            'name' : self.name,
            'phone_number' : self.phone_number,
            'address' : self.address,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date),
            'update_by' : self.update_by
        }
    
    def to_response(self):
        return {
            'id' : self.id,
            'head_master': self.head_master,
            'name' : self.name,
            'phone_number' : self.phone_number,
            'address' : self.address,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date),
            'update_by' : self.update_by
        }