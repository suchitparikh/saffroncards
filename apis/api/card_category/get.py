from flask import Flask, request
import json

endpoint = Flask(__name__)
endpoint.debug = True

@endpoint.route('/api/cardCategory/get', methods=['GET'])
def getCardCategory():
    """
    /cardCategory/get?name=category_name&code=code

    Parameters
    [[name : name of the category to get]
    [code : code of the category to get]]

    Returns
    {"success": [list of categories and code]} on success
    {"error": reason for failure} on failure
    """
    args = {}
    name = request.args.get('name','')
    code = request.args.get('code','')

    if name:
        args['name'] = name
    if code:
        args['code'] = code

    return json.dumps(_get_category(args))

def _get_category(args):
    """
    Underlying implementation to get the category to the database
    """
    return {'name':name, 'code': code}

if __name__ == '__main__':
    endpoint.run()
