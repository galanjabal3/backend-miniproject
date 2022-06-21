from config import config
from falcon_auth import FalconAuthMiddleware, JWTAuthBackend
from util.jwt_util import portprq_auth

from entitas.echo.resources import *
from entitas.school.resources import *
from entitas.user.resources import *
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
api.add_route('/api/login', UserLoginResource())
api.add_route('/api/signup', UserSignupResource())
api.add_route('/api/user/profile', UserProfileResource())
api.add_route('/api/admin/user', UserAdminResource())
api.add_route('/api/admin/guest/list', UserGuestListResource())
api.add_route('/api/admin/school', SchoolResource())
api.add_route('/api/admin/school/{id}', SchoolWithIdResource())

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