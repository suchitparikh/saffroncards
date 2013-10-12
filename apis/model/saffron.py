from sqlalchemy import *
from sqlalchemy.dialects.mysql import INTEGER as INT, BIGINT, BINARY

from apis.model import metadata

card_category = Table('card_category', metadata,
                Column('id', INTEGER(3), primary_key=True, nullable=False),
                Column(u'category', VARCHAR(50), primary_key=False),
                Column(u'code', VARCHAR(2), primary_key=False)
               )
Index(u'id', card_category.c.id, unique=True)

inventory = Table('inventory', metadata,
            Column(u'id', INTEGER(5), primary_key=True, nullable=False),
            Column(u'category_id', INTEGER(3), primary_key=False, nullable=False),
            Column(u'other_category_id', VARCHAR(25), primary_key=False),
            Column(u'cost', DECIMAL(precision=5, scale=2), primary_key=False),
            Column(u'suggested_selling_price', DECIMAL(precision=5, scale=2), primary_key=False),
            Column(u'minimum_selling_price', DECIMAL(precision=5, scale=2), primary_key=False),
            Column(u'available', INTEGER(3), primary_key=False),
            Column(u'sold', INTEGER(3), primary_key=False)
           )
