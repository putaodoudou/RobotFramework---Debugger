from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

app = Flask(__name__)
api = Api(app)

class Start_Test_Suite(Resource):
    def get(self, test_suite_name):
        return {'message': 'Started a Test Suite: %s' % test_suite_name}

api.add_resource(Start_Test_Suite, '/start-test-suite/<string:test_suite_name>')

if __name__ == '__main__':
    app.run()
