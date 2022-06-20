import falcon

class EchoResource:
    auth = {
        'auth_disable': True
    }
    def on_get(self, req, resp):
        resp.media = 'echo'
        resp.status = falcon.HTTP_200