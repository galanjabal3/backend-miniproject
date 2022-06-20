
class UserScore:
    def __init__(self, id=0, score=0, point=0, school_id=0, user_id=0, materi_id=0, count_question=0, total_question_answer=0, create_date=None, update_date=None):
        self.id = id
        self.score = score
        self.point = point
        self.school_id = school_id
        self.user_id = user_id
        self.materi_id = materi_id
        self.count_question = count_question
        self.total_question_answer = total_question_answer
        self.create_date = create_date
        self.update_date = update_date
    
    def to_json(self):
        return {
            'id' : self.id,
            'score' : self.score,
            'point' : self.point,
            'school_id' : self.school_id,
            'user_id' : self.user_id,
            'materi_id' : self.materi_id,
            'count_question' : self.count_question,
            'total_question_answer' : self.total_question_answer,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }
        
    def to_response(self):
        return {
            'id' : self.id,
            'score' : self.score,
            'point' : self.point,
            'school_id' : self.school_id,
            'user_id' : self.user_id,
            'materi_id' : self.materi_id,
            'count_question' : self.count_question,
            'total_question_answer' : self.total_question_answer,
            'create_date' : str(self.create_date),
            'update_date' : str(self.update_date)
        }        