from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from sqlalchemy import create_engine
from json import dump
from robot.running.model import TestSuite
from multiprocessing import Process

APP = Flask(__name__)
CORS(APP)

suite_data = None
suite_result = None


class listener(Resource):
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        global APP
        APP.run(host='localhost', port=3002, debug=True)
        self.server = Process(target=APP.run)

    @APP.route('/')
    def index():
        global suite_data
        return jsonify([suite_data, suite_result])

    def start_suite(self, data, result):
        global suite_data
        global suite_result
        suite_data = data
        suite_result = data

    def end_suite(self, name, attrs):
        self.server.terminate()

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
    APP.run(host='localhost', port='3002', debug=True)
    