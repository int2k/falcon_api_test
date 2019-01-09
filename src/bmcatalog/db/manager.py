import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.orm import scoping

from bmcatalog.db import models


class DBManager(object):
    def __init__(self, connection=None):
        self.connection = connection

        self.engine = sqlalchemy.create_engine(self.connection)
        self.db_session = scoping.scoped_session(
            orm.sessionmaker(
                bind=self.engine,
                autocommit=True
            )
        )

    @property
    def session(self):
        return self.db_session

    def setup(self):
        try:
            models.SAModel.metadata.create_all(self.engine)
        except Exception as exc:
            print('Could not init DB: {}'.format(exc))

