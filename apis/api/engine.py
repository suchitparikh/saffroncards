from sqlalchemy import create_engine
from apis.model.saffron import card_category as cc

HOST=''
SCHEMA=''
_username=''
_passwd=''

class Engine(object):

    def __init__(self):
        CONNECTION_STRING = "mysql://{host}/{schema}?user={username}&passwd={passwd}"
        self.conn_str = CONNECTION_STRING.format(host=HOST,
                                            schema=SCHEMA,
                                            username=_username,
                                            passwd=_passwd
                                           )

    def getEngine(self):
        return create_engine(self.conn_str)
