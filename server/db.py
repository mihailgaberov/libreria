from pymongo import MongoClient
from flask import jsonify
import uuid

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
         'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

class DB:
    def __init__(self):
        print('[*] Initializing DB object')
        client = MongoClient('mongodb://localhost:27017/')
        self.db = client.libreria
        
    def get_all(self):
        print('[*] Getting all books from DB')
        resp = {'status': 'success'}
        cursor = self.db.books.find({})
        books = []
        for doc in cursor:
          print('[*] Adding a book to the array to be returned: ', doc['title'])
          book = {}
          book['title'] = doc['title']
          book['author'] = doc['author']
          books.append(book)

        #resp['books'] = BOOKS
        resp['books'] = books
        return jsonify(resp)
        # cursor = self.db.books.find({})
        # books = []
        
        # for doc in cursor:
        #     print('[*] Adding a book to the array to be returned: ', doc['title'])
        #     books.append(doc)

        # resp = {'status': 'success'}
        # resp['books'] = books
        # return resp
