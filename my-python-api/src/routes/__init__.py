from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/example', methods=['GET'])
def example():
    return {"message": "This is an example endpoint."}