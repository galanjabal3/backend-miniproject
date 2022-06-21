
class User:
    def __init__(self, id=0, username='', password='', email='', avatar='', school_id=0, device='', blocked=False, guest=False, token='', role='', create_date=None, update_date=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.avatar = avatar
        self.school_id = school_id
        self.device = device 
        self.blocked = blocked
        self.guest = guest
        self.token = token
        self.role = role
        self.create_date = create_date
        self.update_date = update_date
    
    def to_json(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email,
            'avatar' : self.avatar,
            'school_id' : self.school_id,
            'device' : self.device, 
            'blocked' : self.blocked,
            'guest' : self.guest,
            'token': self.token,
            'role' : self.role,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'password' : self.password,
            'email' : self.email,
            'avatar' : self.avatar,
            'school_id' : self.school_id,
            'device' : self.device, 
            'blocked' : self.blocked,
            'guest' : self.guest,
            'token': self.token,
            'role' : self.role,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }   

    def to_response_login(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'avatar' : self.avatar,
            'school_id' : self.school_id,
            'device' : self.device, 
            'blocked' : self.blocked,
            'guest' : self.guest,
            'token': self.token,
            'role' : self.role,
        }    
    
    def to_response_profile(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email' : self.email,
            'avatar' : self.avatar,
            'role' : self.role,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }    