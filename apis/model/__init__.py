from sqlalchemy import MetaData, Table

metadata = MetaData()

card_category = Table('card_category', metadata)
inventory = Table('inventory', metadata)
