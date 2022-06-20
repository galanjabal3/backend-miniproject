
class TrafficRecap:
    def __init__(self, id=0, visitors=0, this_date=None, school_id=0, create_date=None, update_date=None):
        self.id = id
        self.visitors = visitors
        self.this_date = this_date
        self.school_id = school_id
        self.create_date = create_date
        self.update_date = update_date
    
    def to_json(self):
        return {
            'id' : self.id,
            'visitors' : self.visitors,
            'this_date' : str(self.this_date),
            'school_id' : self.school_id,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'visitors' : self.visitors,
            'this_date' : str(self.this_date),
            'school_id' : self.school_id,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }