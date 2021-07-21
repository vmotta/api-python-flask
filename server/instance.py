from  flask import Flask
from flask_restplus import Api

class Server():
    def __init__(self) -> Flask:
        self.app = Flask(__name__)
        self.api = Api(self.app,
                    version='1.0.0',
                    title='Instance of the Server API',
                    description='books API',
                    doc='/docs')
    def run(self):
        self.app.run(debug=True)