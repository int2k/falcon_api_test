import simplejson as json

import falcon

from bmcatalog.db import models
from bmcatalog.resources import BaseResource


class ProductResource(BaseResource):

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        """Handles GET requests"""
        model_list = models.Product.get_list(self.db.session)

        products = [model.as_dict for model in model_list]

        resp.status = falcon.HTTP_200
        # if req.content_type == 'application.json':
        media = {
            'products': products
        }
        resp.body = json.dumps(media, ensure_ascii=False, )

        # else:
        #     template = self.load_template('products/product_list.html')
        #     resp.content_type = 'text/html'
        #     resp.body = template.render(products=products)

