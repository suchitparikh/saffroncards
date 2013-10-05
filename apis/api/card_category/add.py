from flask import Flask, request
import json

endpoint = Flask(__name__)
endpoint.debug = True

@endpoint.route('/api/cardCategory/add', methods=['GET','POST'])
def addCardCategory():
    """
    /cardCategory/add?name=category_name&code=code

    Parameters
    name : name of the category to add
    code : code to assign

    Returns
    {"success": number of inserts} on success
    {"error": reason for failure} on failure
    """
    error = None
    name = request.args.get('name','')
    code = request.args.get('code', name[0].upper())

    return json.dumps(_add_category(name, code))

def _add_category(name, code):
    """
    Underlying implementation to add the category to the database
    """
    return {'name':name, 'code': code}

if __name__ == '__main__':
    endpoint.run()
