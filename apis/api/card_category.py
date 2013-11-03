from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource

from apis.model.saffron import card_category as cc
from apis.api.engine import Engine

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, action='append', help='The name of the category')
parser.add_argument('code', type=str, help='The 1 or 2 character code for the category')

class CardCategory(Resource):
    '''
    Encapsulates CRUD for card categories
    '''
    def get(self):
        args = parser.parse_args()
        return _get(args['name'], args['code']), 201

    def put(self):
        args = parser.parse_args()
        name = args.get('name')
        if not name:
            abort(400, message='Category name is a required parameter')
        code = args.get('code') or name[:1].upper()

        res = _put(name, code)
        return res, 201

    def delete(self):
        args = parser.parse_args()
        res = _delete(name)

""" HELPER METHODS """
def _get(name, code):
    where = ''

    if name:
        where = (cc.c.category.in_( name))
    elif code:
        where = (cc.c.code == code)

    query = cc.select().where(where). \
            with_only_columns([
                cc.c.category,
                cc.c.code])

    return dict(_exe(query).fetchall())

def _put(name, code):
    values = {}
    values['category'] = name
    values['code'] = code.strip("'")

    query = cc.insert().values(values)
    try:
        res = _exe(query)
    except Exception as e:
        abort(500, error=e.message)
    else:
        return {'success': res.rowcount}

def _exe(query):
    engine = Engine().getEngine()
    return engine.execute(query)

api.add_resource(CardCategory, '/cardcategory')

if __name__ == '__main__':
    app.run(debug=True)
