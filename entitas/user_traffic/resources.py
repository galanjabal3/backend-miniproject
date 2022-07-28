from entitas.user_traffic import services
from entitas.base_response.models import BaseResponse
import json
import falcon

class TrafficGlobalUserConnect:
    auth = {
        'auth_disabled': True
    }
    def on_get(self, req, resp,):
        base_response = BaseResponse()
        base_response.data = services.get_traffic_global_user()
        if base_response.data is not None:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = 'success'
        else:
            base_response.status = falcon.HTTP_404
            base_response.code = 404
            base_response.message = 'error'

        resp.media = base_response.toJSON()
        resp.status = base_response.status