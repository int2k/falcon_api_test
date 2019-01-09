import falcon
from falcon import api_helpers

from bmcatalog.middleware.context import ContextMiddleware
from bmcatalog.db.manager import DBManager
from bmcatalog.middleware.negotiation import NegotiationMiddleware
from bmcatalog.resources import index, product
from bmcatalog.router import AppRouter


class BMCatalogService(falcon.API):
    def __init__(self, cfg):
        super(BMCatalogService, self).__init__(
            middleware=[ContextMiddleware(),
                        NegotiationMiddleware()],
        )

        self.cfg = cfg

        mgr = DBManager(self.cfg.db.connection)
        mgr.setup()

        # hello_world_res = index.HelloWorldResource(mgr)
        # product_res = product.ProductResource(mgr)
        #
        # self.add_route('/', hello_world_res)
        # self.add_route('/products', product_res)

        router = AppRouter(file_path='bmcatalog/schemas/products.yaml', db_manager=mgr)

        self._router = router
        self._router_search = api_helpers.make_router_search(self._router)

    def start(self):
        pass

    def stop(self, signal):
        pass

