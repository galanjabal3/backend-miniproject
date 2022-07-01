
class UserAnswer:
    def __init__(self, id=0, is_correct=False, answer='', user_id=0, school_id=0, question_id=0, materi_id=0, questions='', create_date=None, update_date=None):
        self.id = id
        self.is_correct = is_correct
        self.answer = answer
        self.user_id = user_id
        self.school_id = school_id
        self.question_id = question_id
        self.materi_id = materi_id
        self.questions = questions
        self.create_date = create_date
        self.update_date = update_date
    
    def to_json(self):
        return {
            'id' : self.id,
            'is_correct' : self.is_correct,
            'answer' : self.answer,
            'user_id' : self.user_id,
            'school_id' : self.school_id,
            'materi_id' : self.materi_id,
            'question_id' : self.question_id,
            'questions' : self.questions,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'is_correct' : self.is_correct,
            'answer' : self.answer,
            'user_id' : self.user_id,
            'school_id' : self.school_id,
            'materi_id' : self.materi_id,
            'question_id' : self.question_id,
            'questions' : self.questions,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }