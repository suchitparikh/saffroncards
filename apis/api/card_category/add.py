from flask import Flask, request
import json

from apis.model.saffron import card_category as cc
from apis.api.engine import Engine

endpoint = Flask(__name__)
endpoint.debug = True

@endpoint.route('/api/cardCategory/add', methods=['GET','POST'])
def addCardCategory():
    """
    /cardCategory/add?category=category_name&code=code

    Parameters
    category : name of the category to add
    code : code to assign

    Returns
    {"success": number of inserts} on success
    {"error": reason for failure} on failure
    """
    error = None
    category = request.args.get('category')
    if not category:
        return json.dumps({"error":"category name required to add category"})

    code = request.args.get('code', category[0].upper())

    return json.dumps({"success":_add_category(category, code)})

def _add_category(category, code):
    """
    Underlying implementation to add the category to the database
    """
    engine = Engine().getEngine()
    values = {}

    values['category'] = category
    values['code'] = code.strip("'")

    query = cc.insert().values(values)
    result = engine.execute(query)

    return 1

if __name__ == '__main__':
    endpoint.run()
