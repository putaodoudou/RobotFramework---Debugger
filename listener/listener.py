from robot.running.model import TestSuite
import threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
import urlparse

SUITE_DATA = None
SUITE_RESULT = None
TESTS_DATA = []
TESTS_RESULT = []
KEYWORDS = []
VARIABLES = []

class listener():
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        print 'Listening on Port 3002'
        addr = ('localhost', 3002)
        self.server = HTTPServer(addr, RequestHandler)
        thread = threading.Thread(target = self.server.serve_forever)
        thread.daemon = True
        thread.start()

    def start_suite(self, data, result):
        #suite = json.jsonify([data, result])
        global SUITE_DATA
        global SUITE_RESULT
        SUITE_DATA = data
        SUITE_RESULT = result
        pass

    def end_suite(self, data, result):
        #suite = json.jsonify([data, result])
        print 'end_suite'
        if not self.server:
            return
        self.server.shutdown()

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

class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Conten-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        global SUITE_DATA
        global SUITE_RESULT

        self._set_headers()
        parsed_path = urlparse.urlparse(self.path)

        if parsed_path.path == '/':
            pass
        if parsed_path.path == '/':
            pass
        print parsed_path
        response = json.dumps([SUITE_DATA, SUITE_RESULT])
        self.wfile.write(response)

    def do_HEAD(self):
        self._set_headers()