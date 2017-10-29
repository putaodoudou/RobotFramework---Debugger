from robot.running.model import TestSuite
import threading
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class listener():
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        print 'Listening on Port 3002'
        addr = ('localhost', 3002)
        self.server = HTTPServer(addr, SimpleHTTPRequestHandler)
        thread = threading.Thread(target = self.server.serve_forever)
        thread.daemon = True
        thread.start()

    def start_suite(self, data, result):
        #suite = jsonify([data, result])
        print 'Start Suite'
        pass

    def end_suite(self, data, result):
        #suite = jsonify([data, result])
        print 'end_suite'
        if not self.server._webserver_thread:
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