from entitas.user_score import services
from entitas.base_response.models import BaseResponse
import json
import falcon

class UserScoreResource:
    def on_get(self, req, resp):
        base_response = BaseResponse()
        filters = []
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=100))
        if req.get_param('id', required=False, default='') != '':
            filters.append({'field': 'id', 'value': req.get_param('id', required=False, default=0)})
        if req.get_param('user_id', required=False, default='') != '':
            filters.append({'field': 'user_id', 'value': req.get_param('user_id', required=False, default='')})
        if req.get_param('question_id', required=False, default='') != '':
            filters.append({'field': 'head_master', 'value': req.get_param('head_master', required=False, default='')})
        base_response.data, base_response.pagination = \
            services.get_user_score_db_with_pagination(page=page, limit=limit, filters=filters)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
    def on_post(self, req, resp):
        base_response = BaseResponse()
        body = req.media
        base_response.data = services.insert_user_score_db(json_object=body)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        
        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
class UserScoreWithIdResource:
    def on_get(self, req, resp, id: int):
        base_response = BaseResponse()
        base_response.data = services.find_user_score_db_by_id(id=int(id))
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
        
    def on_put(self, req, resp, id: int):
        base_response = BaseResponse()
        body = req.media
        body['id'] = int(id)
        base_response.data = services.update_user_score_db(json_object=body)
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
        
    def on_delete(self, req, resp, id: int):
        base_response = BaseResponse()
        base_response.data = services.delete_user_score_by_id(id=int(id))
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

class UserScoreByUserIdResource:
    def on_get(self, req, resp):
        base_response = BaseResponse()
        filters = []
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=100))
        if req.get_param('id', required=False, default='') != '':
            filters.append({'field': 'id', 'value': req.get_param('id', required=False, default=0)})
        if req.get_param('question_id', required=False, default='') != '':
            filters.append({'field': 'head_master', 'value': req.get_param('head_master', required=False, default='')})
        filters.append({'field': 'user_id', 'value': req.context['user']['id']})        
        base_response.data, base_response.pagination = \
            services.get_user_score_db_with_pagination(page=page, limit=limit, filters=filters)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
class UserScoreByUserIdAndMateriIdResource:
    def on_get(self, req, resp, materi_id: int):
        base_response = BaseResponse()
        base_response.data = services.get_user_score_by_materi_id(materi_id=int(materi_id), user_id=req.context['user']['id'])
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