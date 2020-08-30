from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Quote(Resource):
    def get(self, operation, a, b):
        if operation in ('add'):
            try:
                c = a + b
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(a+b)
        elif operation in ('sub'):
            try:
                c = a - b
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(a-b)
        elif operation in ('mul'):
            try:
                c = a * b
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(a*b)
        elif operation in ('div'):
            try:
                c = a / b
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(a/b)
        else:
            abort(make_response(jsonify({'error': 'Not found'}), 404))

api.add_resource(Quote, '/calc/<int:a>,<int:b>,<string:operation>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')