from flask import Flask, request
import json

from apis.model.saffron import card_category as cc
from apis.api.engine import Engine

endpoint = Flask(__name__)
endpoint.debug = True

@endpoint.route('/api/cardCategory/get', methods=['GET'])
def getCardCategory():
    """
    /cardCategory/get?category=category_name&code=code

    Parameters
    [[category : name of the category to get]
    [code : code of the category to get]]

    Returns
    {"success": [list of categories and code]} on success
    {"error": reason for failure} on failure
    """
    args = {}
    category = request.args.get('category','')
    code = request.args.get('code','')

    if category:
        args['category'] = category
    if code:
        args['code'] = code

    return json.dumps({"success": _get_category(args)})

def _get_category(args):
    """
    Underlying implementation to get the category to the database
    """
    e = Engine()
    engine = e.getEngine()
    where = ''

    if args.get('category'):
        where = (cc.c.category == args['category'])
    elif args.get('code'):
        where = (cc.c.code == args['code'])

    query = cc.select().where(where). \
            with_only_columns([
                cc.c.category,
                cc.c.code])

    result = engine.execute(query)
    return dict(result.fetchall())

if __name__ == '__main__':
    endpoint.run()
