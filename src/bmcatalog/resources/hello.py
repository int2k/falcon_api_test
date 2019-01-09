import falcon


class HelloResource(object):

    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200
        resp.body = '{"message": "Hello world!"}'
