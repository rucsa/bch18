from flask import Flask
from flask.ext.cors import CORS
from simple_flask.core.core import say_hallo
from simple_flask_blueprint.rest.blueprint_rest import bp


class RootREST:

    def __init__(self, host, run_flask):
        self.host = host
        self.run_flask = run_flask
        self.app = Flask(__name__)
        CORS(self.app,
             resources={
                 r'/*': {
                     'origins': '*',
                     'headers': ['Content-Type']
                 }
             }
        )
        self.app.register_blueprint(bp, url_prefix='/blueprint')

        # Root service.
        @self.app.route('/', methods=['GET'])
        def say_hello_service():
            return say_hallo()

        # Root service.
        @self.app.route('/<name>/', methods=['GET'])
        def say_hello_to_guest_service(name):
            return say_hallo(name)

        # Run Flask.
        if self.run_flask:
            self.app.run(host=self.host, debug=True)


def run_engine(host):
    RootREST(host, True)

if __name__ == '__main__':
    run_engine('localhost')
