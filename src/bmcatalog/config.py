from aumbry import YamlConfig, GenericConfig, Attr


class DatabaseConfig(YamlConfig):
    __mapping__ = {
        'connection': Attr('connection', str)
    }


class AppConfig(YamlConfig):
    __mapping__ = {
        'db': Attr('db', DatabaseConfig),
        'gunicorn': Attr('gunicorn', dict)
    }

    def __init__(self):
        self.db = DatabaseConfig()
        self.gunicorn = {}
