import json
from pony.orm import *
from util.db_util import db2
from entitas.flyway_schema_history.models import FlywaySchemaHistory
from entitas.materi.models import Materi
from entitas.question.models import Question
from entitas.school.models import School
from entitas.traffic_recap.models import TrafficRecap
from entitas.user.models import User
from entitas.user_answer.models import UserAnswer
from entitas.user_score.models import UserScore
from entitas.user_traffic.models import UserTraffic
from datetime import date, datetime

class FlywaySchemaHistoryDB(db2.Entity):
    _table_ = 'flyway_schema_history'
    installed_rank = PrimaryKey(int, auto=True)
    version = Optional(str, nullable=True)
    description = Optional(str, nullable=True)
    type = Optional(str, nullable=True)
    script = Optional(str, 1000, nullable=True)
    checksum = Optional(int, nullable=True)
    installed_by = Optional(str, nullable=True)
    installed_on = Optional(datetime, nullable=True)
    execution_time = Optional(int, nullable=True)
    success = Optional(bool, nullable=True)
    
    def to_model(self):
        item = FlywaySchemaHistory()
        item.installed_rank = self.installed_rank
        item.version = self.version
        item.description = self.description
        item.type = self.type
        item.script = self.script
        item.checksum = self.checksum
        item.installed_by = self.installed_by
        item.installed_on = self.installed_on
        item.execution_time = self.execution_time
        item.success = self.success
        return item
    
class MateriDB(db2.Entity):
    _table_ = 'materi'
    id = PrimaryKey(int, auto=True)
    school_id = Optional(int, nullable=True)
    description = Optional(str, 1000, nullable=True)
    question_total = Optional(int, nullable=True)
    teacher = Optional(str, nullable=True)
    materi = Optional(str, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = Materi()
        item.id = self.id
        item.description = self.description
        item.question_total = self.question_total
        item.teacher = self.teacher
        item.materi = self.materi
        item.school_id = self.school_id
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item
    
class QuestionDB(db2.Entity):
    _table_ = 'question'
    id = PrimaryKey(int, auto=True)
    image = Optional(str, 1000, nullable=True)
    question = Optional(str, nullable=True)
    answer_true = Optional(str, nullable=True)
    answer_list = Optional(str, nullable=True)
    count_used = Optional(int, nullable=True)
    publish = Optional(bool, nullable=True)
    materi_id = Optional(int, nullable=True)
    school_id = Optional(int, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = Question()
        item.id = self.id
        item.image = self.image
        item.question = self.question
        item.answer_true  = self.answer_true
        item.answer_list = self.answer_list
        item.count_used = self.count_used
        item.publish = self.publish
        item.school_id = self.school_id
        item.materi_id = self.materi_id
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item
    
class SchoolDB(db2.Entity):
    _table_ = 'school'
    id = PrimaryKey(int, auto=True)
    head_master = Optional(str, nullable=True)
    phone_number = Optional(str, nullable=True)
    name = Optional(str, nullable=True)
    address = Optional(str, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    update_by = Optional(str, nullable=True)
    
    def to_model(self):
        item = School()
        item.id = self.id
        item.head_master = self.head_master
        item.name = self.name
        item.phone_number = self.phone_number
        item.address = self.address
        item.create_date = self.create_date
        item.update_date = self.update_date
        item.update_by = self.update_by
        return item

class TrafficRecapDB:
    _table_ = 'traffic_recap'
    id = PrimaryKey(int, auto=True)
    visitors = Optional(int, nullable=True)
    this_date = Optional(date, nullable=True)
    school_id = Optional(int, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = TrafficRecap()
        item.id = self.id
        item.visitors = self.visitors
        item.this_date = self.this_date
        item.school_id = self.school_id
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item
    
class UserDB(db2.Entity):
    _table_ = 'user'
    id = PrimaryKey(int, auto=True)
    avatar = Optional(str, nullable=True)
    username = Optional(str, nullable=True)
    password = Optional(str, nullable=True)
    email = Optional(str, nullable=True)
    device = Optional(str, nullable=True)
    blocked = Optional(bool, nullable=True)
    guest = Optional(bool, nullable=True)
    school_id = Optional(int, nullable=True)
    token = Optional(str, nullable=True)
    role = Optional(str, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = User()
        item.id = self.id
        item.username = self.username
        item.password = self.password
        item.email = self.email
        item.avatar = self.avatar
        item.school_id = self.school_id
        item.device = self.device 
        item.blocked = self.blocked
        item.guest = self.guest
        item.token = self.token
        item.role = self.role
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item
    
class UserAnswerDB(db2.Entity):
    _table_ = 'user_answer'
    id = PrimaryKey(int, auto=True)
    is_correct = Optional(bool, nullable=True)
    answer = Optional(str, nullable=True)
    user_id = Optional(int, nullable=True)
    question_id = Optional(int, nullable=True)
    materi_id = Optional(int, nullable=True)
    school_id = Optional(int, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = UserAnswer()
        item.id = self.id
        item.is_correct = self.is_correct
        item.answer = self.answer
        item.user_id = self.user_id
        item.school_id = self.school_id
        item.question_id = self.question_id
        item.materi_id = self.materi_id
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item
    
class UserScoreDB(db2.Entity):
    _table_ = 'user_score'
    id = PrimaryKey(int, auto=True)
    score = Optional(int, nullable=True)
    point = Optional(int, nullable=True)
    school_id = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    materi_id = Optional(int, nullable=True)
    count_question = Optional(int, nullable=True)
    total_question_answer = Optional(int, nullable=True) 
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = UserScore()
        item.id = self.id
        item.score = self.score
        item.point = self.point
        item.school_id = self.school_id
        item.user_id = self.user_id
        item.materi_id = self.materi_id
        item.count_question = self.count_question
        item.total_question_answer = self.total_question_answer
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item
    
class UserTrafficDB(db2.Entity):
    _table_ = 'user_traffic'
    id = PrimaryKey(int, auto=True)
    visitors = Optional(int, nullable=True)
    user_id = Optional(int, nullable=True)
    school_id = Optional(int, nullable=True)
    users = Optional(str, 1000, nullable=True)
    create_date = Optional(datetime, nullable=True)
    update_date = Optional(datetime, nullable=True)
    
    def to_model(self):
        item = UserTraffic()
        item.id = self.id
        item.visitors = self.visitors
        item.user_id = self.user_id
        item.school_id = self.school_id
        item.users = json.loads(self.users),
        item.create_date = self.create_date
        item.update_date = self.update_date
        return item

if db2.schema is None:
    db2.generate_mapping(create_tables=False)