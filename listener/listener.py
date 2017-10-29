from robot.running.model import TestSuite
import threading
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import json
import urlparse
import subprocess
import sys
import os
import psutil

SUITE_DATA = None
SUITE_RESULT = None
TESTS_DATA = []
TESTS_RESULT = []
KEYWORDS = []
VARIABLES = []

class listener():
    ROBOT_LISTENER_API_VERSION = 2

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
    def __init__(self):
        self._process = None

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self, name=None):
        global SUITE_DATA
        global SUITE_RESULT

        self._set_headers()
        parsed_path = urlparse.urlparse(self.path)

        if parsed_path.path == '/':
            response = json.dumps([SUITE_DATA, SUITE_RESULT])
            self.wfile.write(response)
        
        # TODO: Regex this to find /``any string``
        if parsed_path.path == '/test':
            test_name = parsed_path.path.lstrip('//')
            self._start_test(test_name)

        if parsed_path.path == '/pause':
            pass

        if parsed_path.path == '/continue':
            pass

    def do_HEAD(self):
        self._set_headers()

    def _start_test(self, name):
        dir_path = sys.path[0]
        test = subprocess.call(["robot",
                        "--listener",
                        os.path.abspath(dir_path + "/../listener/listener.py"),
                        os.path.abspath(dir_path + "/../tests/" + name + ".robot")])
        self._process = psutil.Process(test.pid)

    def _pause_test(self):
        if self._process.status() == 'running':
            self._process.suspend()

    def _stop_test(self):
        status = self._process.status()
        if status == 'running' or status == 'suspended':
            self._process.terminate()

    def _step(self):
        pass

    def stop_server(self):
        if not self.server:
            return
        self.server.shutdown()

if __name__ == "__main__":
    # Start the server to listen for command from the front end
    print 'Listening on Port 3002'
    addr = ('localhost', 3002)
    server = HTTPServer(addr, RequestHandler)
    thread = threading.Thread(target = server.serve_forever)
    thread.daemon = True
    thread.start()
