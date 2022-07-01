from entitas.user import services
from entitas.base_response.models import BaseResponse
import json
import falcon

class UserAdminResource:
    def on_get(self, req, resp):
        base_response = BaseResponse()
        filters = []
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=100))
        if req.get_param('id', required=False, default='') != '':
            filters.append({'field': 'id', 'value': req.get_param('id', required=False, default=0)})
        if req.get_param('school_id', required=False, default='') != '':
            filters.append({'field': 'school_id', 'value': req.get_param('school_id', required=False, default='')})
        if req.get_param('username', required=False, default='') != '':
            filters.append({'field': 'username', 'value': req.get_param('username', required=False, default='')})
        if req.get_param('email', required=False, default='') != '':
            filters.append({'field': 'email', 'value': req.get_param('email', required=False, default='')})
        base_response.data, base_response.pagination = \
            services.get_user_db_with_pagination(page=page, limit=limit, filters=filters)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        resp.media = base_response.toJSON()
        resp.status = base_response.status

class UserProfileResource:
    def on_get(self, req, resp):
        base_response = BaseResponse()
        base_response.data = services.get_profile_user_db(json_object={'user': req.context['user']})
        if base_response.data is not None:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = 'success'
        else:
            base_response.status = falcon.HTTP_404
            base_response.code = 404
            base_response.message = 'Data not found'
        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
    def on_put(self, req, resp):
        base_response = BaseResponse()
        body = req.media
        body['user'] = req.context['user']
        body['id'] = req.context['user']['id']
        base_response.data = services.update_profile_user_db(json_object=body)
        if base_response.data is not None:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = 'success'
        else:
            base_response.status = falcon.HTTP_404
            base_response.code = 404
            base_response.message = 'Data not found'
        resp.media = base_response.toJSON()
        resp.status = base_response.status

class UserLoginResource:
    auth = {
        'auth_disabled': True
    }
    def on_post(self, req, resp):
        base_response = BaseResponse()
        body = req.media
        base_response.data, base_response.message = services.login_user(json_object=body)
        if base_response.data is None or base_response.data['token'] == '':
            base_response.status = falcon.HTTP_403
            base_response.code = 403
            base_response.message = base_response.message
            base_response.data = {}
        else:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = 'success'

        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
class UserSignupResource:
    auth = {
        'auth_disabled': True
    }
    def on_post(self, req, resp):
        base_response = BaseResponse()
        body = req.media
        body['roles'] = 'ADMIN'
        base_response.data = services.signup_user_db(json_object=body)
        if base_response.data['token'] == '':
            base_response.status = falcon.HTTP_403
            base_response.code = 403
            base_response.message = 'forbiden'
            if base_response.data['message'] != '':
                base_response.message = base_response.data['message']
        else:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = 'success'

        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
class UserGuestListResource:
    auth = {
        'auth_disabled': True
    }
    def on_get(self, req, resp):
        base_response = BaseResponse()
        filters = []
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=100))
        filters.append({'field': 'guest', 'value': True})
        base_response.data, base_response.pagination = \
            services.get_user_db_with_pagination(page=page, limit=limit, filters=filters)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
class UserSignupAdminSchoolResource:
    auth = {
        'auth_disabled': True
    }
    def on_post(self, req, resp, id: int):
        base_response = BaseResponse()
        body = req.media
        body['school_id'] = int(id)
        body['roles'] = 'ADMIN_SCHOOL'
        base_response.data = services.signup_user_db(json_object=body)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'

        resp.media = base_response.toJSON()
        resp.status = base_response.status

class UpdateSchoolIdUserResource:
    def on_put(self, req, resp, school_id: int):
        base_response = BaseResponse()
        base_response.data = services.update_school_id_user_by_user_id(id=req.context['user']['id'], school_id=int(school_id))
        if base_response.data is not None:
            base_response.status = falcon.HTTP_200
            base_response.code = 200
            base_response.message = 'success'
        else:
            base_response.status = falcon.HTTP_404
            base_response.code = 404
            base_response.message = 'Data not found'
        resp.media = base_response.toJSON()
        resp.status = base_response.status