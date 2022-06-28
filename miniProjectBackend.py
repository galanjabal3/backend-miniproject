from config import config
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from util.jwt_util import portprq_auth

from entitas.echo.resources import *
from entitas.school.resources import *
from entitas.user.resources import *
from entitas.user_traffic.resources import *
from entitas.materi.resources import *
from entitas.question.resources import *
from falcon_swagger_ui import register_swaggerui_app
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
api.add_route('/api/echo', EchoResource())
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
api.add_route('/api/admin/question/{school_id}', QuestionMateriAdminResource())
# update question-materi
api.add_route('/api/admin/question/materi/{id}', QuestionMateriUpdateResource())
# get all question-materi
api.add_route('/api/question/materi', MateriResource())
# get question by id and materi_id
api.add_route('/api/question/{id}/materi/{materi_id}', QuestionMateriResource())
# get question-materi by materi_id role user
api.add_route('/api/question/materi/{id}/user', QuestionMateriUserResource())
# get question-materi by materi_id role admin
api.add_route('/api/question/materi/{id}/admin', GetQuestionMateriAdminResource())
# post cek answer
api.add_route('/api/question/{id}/answer', QuestionCheckAnswerResource())


SWAGGERUI_URL = "/docs"
SCHEMA_URL = "/static/openapi.yaml"
# STATIC_PATH = pathlib.Path(__file__).parent / "res"
# favicon_url = "https://falconframework.org/favicon-32x32.png"
register_swaggerui_app(
    api,
    SWAGGERUI_URL,
    SCHEMA_URL,
    page_title="Mini Project Backend API",
    # favicon_url=favicon_url,
    config={
        "supportedSubmitMethods": ["get", "post", "put", "delete", "patch"],
    },
)