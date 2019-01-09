import os

import aumbry
from docopt import docopt
from waitress import serve

from bmcatalog.app import BMCatalogService
from bmcatalog.config import AppConfig

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENVIRONMENT = os.environ.get('ENVIRONMENT', 'develop')
CONFIG_FILE_PATH = os.path.join(BASE_DIR, 'configuration', f'config_{ENVIRONMENT}.yaml')


cfg = aumbry.load(
    aumbry.FILE,
    AppConfig,
    {
        'CONFIG_FILE_PATH': CONFIG_FILE_PATH
    }
)

api_app = BMCatalogService(cfg)

serve(api_app, host='127.0.0.1', port=8000)
