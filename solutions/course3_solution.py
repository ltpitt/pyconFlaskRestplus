"""Module for the solutions of course3.py"""

import os

from flask import request
from flask import jsonify
from flask_restplus import Resource
from flask_restplus import Api, Resource, fields
from werkzeug.exceptions import BadRequest


from solutions import create_api, create_app, mainTitle, API_MODEL_COURSE3, \
     awesome_dictionary_to_return

app = create_app()  # pylint: disable=invalid-name
api = create_api(app, mainTitle, 'Description')  # pylint: disable=invalid-name
API_MODEL = api.model('AwesomeDictionary', {
    'Original request': fields.String(required=True, min_length=1, max_length=200, description='Original request')})


@api.expect(API_MODEL, validate=True)
@api.route('/jsonify')
class Jsonify(Resource):
    """Endpoint for /jsonify"""
    @staticmethod
    @api.doc(responses={200: 'Ok'})
    def get():
        """GET endpoint for /jsonify"""
        return jsonify(awesome_dictionary_to_return)

    @staticmethod
    @api.doc(responses={200: 'Ok'})
    def post():
        """POST endpoint for /jsonify"""
        try:
            data = request.json
            awesome_dictionary_to_return["Original request"] = data["Original request"]
            return jsonify(awesome_dictionary_to_return)
        except Exception as error:
            raise BadRequest


if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='127.0.0.1', port=PORT)
