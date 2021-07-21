from flask import Flask
from flask_restplus import Api, Resource

from server.instance import Server

app, api = Server.app, Server.api


books_db = {
                {'id': 0, 'title': 'War and Piece', 
                 'id': 1, 'title': 'Clean Code', }
}

@api.route('/books')
class BookList(Resource):

    def get(self):
        return books_db