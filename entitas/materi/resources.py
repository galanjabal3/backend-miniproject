from entitas.materi import services
from entitas.base_response.models import BaseResponse
import json
import falcon


class MateriResource:
    def on_get(self, req, resp):
        base_response = BaseResponse()
        filters = []
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=100))
        if req.get_param('id', required=False, default='') != '':
            filters.append({'field': 'id', 'value': req.get_param('id', required=False, default=0)})
        if req.get_param('school_id', required=False, default='') != '':
            filters.append({'field': 'school_id', 'value': req.get_param('school_id', required=False, default='')})
        base_response.data, base_response.pagination = \
            services.get_materi_db_with_pagination(page=page, limit=limit, filters=filters)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        resp.media = base_response.toJSON()
        resp.status = base_response.status
        
    def on_post(self, req, resp):
        base_response = BaseResponse()
        body = req.media
        base_response.data = services.insert_materi_db(json_object=body)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        
        resp.media = base_response.toJSON()
        resp.status = base_response.status

class MateriWithIdResource:
    def on_get(self, req, resp, id: int):
        base_response = BaseResponse()
        base_response.data = services.find_materi_db_by_id(id=int(id))
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
        base_response.data = services.update_materi_db(json_object=body)
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
        base_response.data = services.delete_materi_by_id(id=int(id))
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
        
class QuestionMateriAdminResource:
    def on_post(self, req, resp, school_id: int):
        base_response = BaseResponse()
        body = req.media
        base_response.data = services.create_materi_db(json_object=body, roles=req.context['user']['roles'], school_id=int(school_id))
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        
        resp.media = base_response.toJSON()
        resp.status = base_response.status

class QuestionMateriUpdateResource:
    def on_put(self, req, resp, id: int):
        base_response = BaseResponse()
        body = req.media
        body['id'] = int(id)
        base_response.data = services.update_question_from_materi(json_object=body, roles=req.context['user']['roles'])
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
    
class QuestionMateriUserResource:
    def on_get(self, req, resp, id: int):
        base_response = BaseResponse()
        base_response.data = services.find_question_materi_from_user(id=int(id))
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
        
class GetQuestionMateriAdminResource:
    def on_get(self, req, resp, id: int):
        base_response = BaseResponse()
        base_response.data = services.find_materi_db_by_id(id=int(id))
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
        
class MateriUserResource:
    def on_get(self, req, resp):
        base_response = BaseResponse()
        filters = []
        page = int(req.get_param('page', required=False, default=1))
        limit = int(req.get_param('limit', required=False, default=100))
        if req.get_param('id', required=False, default='') != '':
            filters.append({'field': 'id', 'value': req.get_param('id', required=False, default=0)})
        if req.get_param('materi', required=False, default='') != '':
            filters.append({'field': 'materi', 'value': req.get_param('materi', required=False, default='')})
        filters.append({'field': 'school_id', 'value': req.context['user']['school_id']})
        base_response.data, base_response.pagination = \
            services.get_materi_db_with_pagination(page=page, limit=limit, filters=filters)
        base_response.status = falcon.HTTP_200
        base_response.code = 200
        base_response.message = 'success'
        resp.media = base_response.toJSON()
        resp.status = base_response.status