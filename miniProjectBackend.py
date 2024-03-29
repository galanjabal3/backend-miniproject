from config import config
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from util.jwt_util import portprq_auth

from entitas.echo.resources import *
from entitas.school.resources import *
from entitas.user.resources import *
from entitas.user_traffic.resources import *
from entitas.materi.resources import *
from entitas.question.resources import *
from entitas.user_answer.resources import *
from entitas.user_score.resources import *
from util.db_util import db2
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
if db2.schema is None:
    db2.generate_mapping(create_tables=False)
    
auth_middleware = FalconAuthMiddleware(
    JWTAuthBackend(
        portprq_auth,
        secret_key=config.secret_jwt,
        algorithm="HS512",
        required_claims=["exp", "token"],
    ),
    # exempt_routes=["/docs", "/metrics", "/api/certificate/code"],
    # exempt_methods=["OPTIONS", "HEAD"],
)    

api = falcon.App(cors_enable=True, middleware=[auth_middleware])

api.req_options.auto_parse_form_urlencoded = True

print('Mini Project Backend Running...')
api.add_route('/', EchoResource())
# login
api.add_route('/api/login', UserLoginResource())
# signup admin
api.add_route('/api/signup', UserSignupResource())
# Get dan Put User profile
api.add_route('/api/user/profile', UserProfileResource())
# Get All User
api.add_route('/api/admin/user', UserAdminResource())
# Get Guest = True
api.add_route('/api/admin/guest/list', UserGuestListResource())
# CRUD School
api.add_route('/api/admin/school', SchoolResource())
api.add_route('/api/admin/school/{id}', SchoolWithIdResource())
# user school
api.add_route('/api/user/school', SchoolResource())
api.add_route('/api/user/school/{id}', SchoolWithIdResource())
# update school id user
api.add_route('/api/user/update_school/{school_id}', UpdateSchoolIdUserResource())
# school-registration
api.add_route('/api/school/registration', SchoolResource())
api.add_route('/api/school/registration/{id}', SchoolRegistrationUpdateResource())
api.add_route('/api/school/registration/list', SchoolListResource())
api.add_route('/api/school/registration/search', SchoolListResource())
# signup-user-admin-school
api.add_route('/api/signup_admin_school/{id}', UserSignupAdminSchoolResource())
# traffic
api.add_route('/api/traffic_global_user/connect', TrafficGlobalUserConnect())
# question-materi
# post question-materi
api.add_route('/api/admin_school/materi/question/{school_id}', QuestionMateriAdminResource())
# update question-materi
api.add_route('/api/admin/question/materi/{id}', QuestionMateriUpdateResource())
# get all question-materi
# api.add_route('/api/question/materi', MateriResource())
api.add_route('/api/admin_school/question/materi', MateriUserResource())
# question by id and materi_id
api.add_route('/api/admin_school/materi/{materi_id}/question', QuestionAdminSchoolResource())
api.add_route('/api/admin_school/materi/{materi_id}/question/{id}', QuestionAdminSchoolWithIdResource())
# get question-materi by materi_id role user
api.add_route('/api/question/materi/{id}/user', QuestionMateriUserResource())
# get question-materi by materi_id role admin
api.add_route('/api/question/materi/{id}/admin', GetQuestionMateriAdminResource())
# post cek answer
api.add_route('/api/question/{id}/answer', QuestionCheckAnswerResource())
# get user_score
api.add_route('/api/user_score', UserScoreByUserIdResource())
api.add_route('/api/user_score/materi/{materi_id}', UserScoreByUserIdAndMateriIdResource())
# cek apakah user sudah pernah mengerjakan materi ini
api.add_route('/api/user/materi/{materi_id}/checking', CheckUserAnswerFromUserResource())
