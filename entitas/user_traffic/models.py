
class UserTraffic:
    def __init__(self, id=0, visitors=0, user_id=0, school_id=0, users={}, create_date=None, update_date=None):
        self.id = id
        self.visitors = visitors
        self.user_id = user_id
        self.school_id = school_id
        self.users = users
        self.create_date = create_date
        self.update_date = update_date
    
    def to_json(self):
        return {
            'id' : self.id,
            'visitors' : self.visitors,
            'user_id' : self.user_id,
            'school_id' : self.school_id,
            'users': self.users,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'visitors' : self.visitors,
            'user_id' : self.user_id,
            'school_id' : self.school_id,
            'users': self.users,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }