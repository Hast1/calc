from flask import Flask, jsonify, abort, make_response
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Quote(Resource):
    def get(self, operation, a, b):
        if operation in ('add'):
            try:
                c = float(a) + float(b)
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(c)
        elif operation in ('sub'):
            try:
                c = float(a) - float(b)
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(c)
        elif operation in ('mul'):
            try:
                c = float(a) * float(b)
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(c)
        elif operation in ('div'):
            try:
                c = float(a) / float(b)
            except:
                abort(make_response(jsonify({'error': 'Not found'}), 404))
            return jsonify(c)
        else:
            abort(make_response(jsonify({'error': 'Not found'}), 404))

api.add_resource(Quote, '/calc/<string:a>,<string:b>,<string:operation>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')