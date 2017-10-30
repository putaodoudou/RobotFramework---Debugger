from robot.running.model import TestSuite
import threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
import urlparse
from queue import Queue
import cgi

commands = Queue()
suites = None
suites_result = None
tests = []
tests_results = []
keywords = []
keywords_result = []
variables = []

current_suite = None
current_suite_result = None
current_test = None
current_test_result
current_keyword = None
current_keyword_result = None

class listener():
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        print 'Listening on Port 3002'
        addr = ('localhost', 3002)
        self.server = HTTPServer(addr, RequestHandler)
        thread = threading.Thread(target = self.server.serve_forever)
        thread.daemon = True
        thread.start()

    def start_suite(self, suite, result):
        global commands
        global current_suit
        global current_suit_result

        self._clear_currents('suite')

        if not commands.empty():
            for command in commands:
                if command.type == 'add_keyword':
                    suite.tests.pop().keywords.create(command.args, command.kwargs)

        current_suit = suite
        current_suit_result = result

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

    def _clear_currents(self, command_type):
        global current_suite
        global current_suite_result
        global current_test
        global current_test_result 
        global current_keyword
        global current_keyword_result

        if command_type == 'suite':
            current_suite = None
            current_suite_result = None
            current_test = None
            current_test_result = None
            current_keyword = None
            current_keyword_result = None

        elif command_type == 'test':
            current_test = None
            current_test_result = None
            current_keyword = None
            current_keyword_result = None

        #TODO keywords and stuff

    
class RequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        global suites
        global suites_result

        self._set_headers()
        parsed_path = urlparse.urlparse(self.path)

        if parsed_path.path == '/update':
            response = json.dumps([suites, suites_result])
            self.wfile.write(response)

        if parsed_path.path == '/pause':
            pass

        if parsed_path.path == '/stop':
            pass
    
    def do_POST(self):
        global suites
        global suites_result
        global commands

        self._set_headers()
        parsed_path = urlparse.urlparse(self.path)
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        data = json.loads(self.data_string)
        print data

        if parsed_path.path == '/keyword':
            global commands
            commands.put(data)

    def do_HEAD(self):
        self._set_headers()