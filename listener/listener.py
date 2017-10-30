from Queue import Queue
import json
from robot.running.model import *

class listener():
    ROBOT_LISTENER_API_VERSION = 3

    def __init__(self):
        commands = Queue()

    def start_suite(self, suite, result):
        print 'Start Suite'
        suite_json = json.dumps(suite)
        print suite_json
        result_json = json.dumps(result)
        print result_json

    def end_suite(self, suite, result):
        print 'End Suite'
        suite_json = json.dumps(suite)
        print suite_json
        result_json = json.dumps(result)
        print result_json

    def start_test(self, test, result):
        print 'Start Test'
        keywords = json.dumps(test.keywords)
        print keywords
        test_result = json.dumps(result)
        print test_result

    def end_test(self, test, result):
        print 'End Test'
        test_json = json.dumps(test)
        print test_json
        test_result = json.dumps(result)
        print test_result

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

    def debug_file(self, path):
        pass

    def close(self):
        pass