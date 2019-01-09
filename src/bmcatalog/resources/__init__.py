import os

import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape


class BaseResource(object):
    def __init__(self, db_manager):
        self.db = db_manager
        self.env = Environment(
            loader=PackageLoader('bmcatalog', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def load_template(self, name):
        return self.env.get_template(name)
        # base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # path = os.path.join(base_dir, 'templates', name)
        # with open(os.path.abspath(path), 'r') as fp:
        #     return jinja2.Template(fp.read())
