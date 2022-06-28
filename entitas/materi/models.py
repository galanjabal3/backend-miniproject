
class Materi:
    def __init__(self, id=0, description='', question_total=0, teacher='', school_id=0, materi='', question=[], create_date=None, update_date=None):
        self.id = id
        self.description = description
        self.question_total = question_total
        self.teacher = teacher
        self.materi = materi
        self.school_id = school_id
        self.question = question
        self.create_date = create_date
        self.update_date = update_date

    def to_json(self):
        return {
            'id' : self.id,
            'school_id' : self.school_id,
            'description' : self.description,
            'question_total' : self.question_total,
            'teacher' : self.teacher,
            'materi' : self.materi,
            'question' : self.question, 
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'school_id' : self.school_id,
            'description' : self.description,
            'question_total' : self.question_total,
            'teacher' : self.teacher,
            'materi' : self.materi,
            'question' : self.question, 
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }