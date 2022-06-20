# from config import config
from entitas.echo.resources import *

from falcon_swagger_ui import register_swaggerui_app
from util.db_util import db2
import os

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
if db2.schema is None:
    db2.generate_mapping(create_tables=False)
    
api = falcon.App(cors_enable=True)

api.req_options.auto_parse_form_urlencoded = True

print('Mini Project Backend Running...')
api.add_route('/api/echo', EchoResource())

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