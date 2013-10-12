from flask import Flask, request
import json

from apis.model.saffron import card_category as cc
from apis.api.engine import Engine

endpoint = Flask(__name__)
endpoint.debug = True

@endpoint.route('/api/cardCategory/edit', methods=['GET','POST'])
def addCardCategory():
    """
    /cardCategory/edit?edit=category_or_code&category=category_name&code=code

    Parameters
    edit        : [category or code to be edited]
    category    : name of the category to edit
    code        : code to assign

    Returns
    {"success": number of rows updated} on success
    {"error": reason for failure} on failure
    """

    error = None

    edit = request.args.get('edit')
    if not edit or edit.lower() not in ['category','code']:
        return json.dumps({'error':'Edit is required parameter and should be one of\
                            category or code'})

    category = request.args.get('category')
    code = request.args.get('code', category[0].upper())
    if not (category or code):
        return json.dumps({'error':'category and code are required parameters for an edit'})

    return json.dumps({"success":_edit_category(edit, category, code)})

def _edit_category(edit, category, code):
    """
    Underlying implementation to add the category to the database
    """
    engine = Engine().getEngine()
    values = {}

    if edit == 'category':
        where = (cc.c.code == code)
        values['category'] = category
    else:
        where = (cc.c.category == category)
        values['code'] = code.strip("'")

    query = cc.update().where(where).values(values)
    result = engine.execute(query)

    return result.rowcount

if __name__ == '__main__':
    endpoint.run()
