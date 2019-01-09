from decimal import Decimal, ROUND_HALF_UP

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from decimal import getcontext, Decimal

# Set the precision.
getcontext().prec = 3

SAModel = declarative_base()


class Product(SAModel):
    __tablename__ = 'products'
    id = sa.Column(sa.Integer, primary_key = True)
    name = sa.Column(sa.String(255), nullable=False, index=True)
    description = sa.Column(sa.Text)
    price = sa.Column(sa.Numeric(precision=4), default=0)

    def __init(self, name: str, description: str, price: Decimal):
        self.name = name
        self.description = description
        self.price = price

    @property
    def as_dict(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price.quantize(exp=Decimal('0.01'), rounding=ROUND_HALF_UP)
        }

    def save(self, session):
        with session.begin():
            session.add(self)

    @classmethod
    def get_list(cls, session):
        models = []

        with session.begin():
            query = session.query(cls)
            models = query.all()

        return models

