from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine
from json import dump

APP = Flask(__name__)
CORS(APP)

current_suite_name = ''

class listener(Resource):
    ROBOT_LISTENER_API_VERSION = 2
    
    def __init__(self):
        current_suite_name = None

    def put(self, test_suite_name):
        print test_suite_name
        return
    
    @APP.route('/')
    @APP.route('/<name>')
    def index(name=None):
        global current_suite_name
        if name is not None:
            current_suite_name = name
            return 'Set the name'
        else:
            return current_suite_name

    def start_suite(self, name, attrs):
        pass

    def end_suite(self, name, attrs):
        pass

    def start_test(self, name, attrs):
        pass

    def end_test(self, name, attrs):
        pass

    def start_keyword(self, name, attrs):
        pass

    def end_keyword(self, name, attrs):
        pass

    def message(self, message):
        pass

    def log_message(self, message):
        pass

    def log_file(self, path):
        pass

    def output_file(self, path):
        pass

    def report_file(self, path):
        pass

    def summary_file(self, path):
        pass

    def debug_file(self, path):
        pass

if __name__ == '__main__':
    APP.run(debug=True)
    