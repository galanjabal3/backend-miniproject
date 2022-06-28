
class Question:
    def __init__(self, id=0, image='', question='', answer_true='', answer_list=[], count_used=0, publish=False, school_id=0, materi_id=0, create_date=None, update_date=None):
        self.id = id
        self.image = image
        self.question = question
        self.answer_true  = answer_true
        self.answer_list = answer_list
        self.count_used = count_used
        self.publish = publish
        self.school_id = school_id
        self.materi_id = materi_id
        self.create_date = create_date
        self.update_date = update_date
    
    def to_json(self):
        return {
            'id' : self.id,
            'image' : self.image,
            'question' : self.question,
            'answer_true' : self. answer_true,
            'answer_list' : self.answer_list,
            'count_used' : self.count_used,
            'publish' : self.publish,
            'school_id' : self.school_id,
            'materi_id' : self.materi_id,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'image' : self.image,
            'question' : self.question,
            'answer_true' : self. answer_true,
            'answer_list' : self.answer_list,
            'count_used' : self.count_used,
            'publish' : self.publish,
            'school_id' : self.school_id,
            'materi_id' : self.materi_id,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }