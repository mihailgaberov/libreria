from pymongo import MongoClient
from flask import jsonify
from bson.objectid import ObjectId

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
            print('[*] Getting a record from database: ', doc['title'])
            book = {}
            book['id'] = str(doc['_id'])
            book['title'] = doc['title']
            book['author'] = doc['author']
            book['read'] = doc['read']
            books.append(book)

        resp['books'] = books
        return jsonify(resp)

    def add_book(self, payload):
        print('[*] Adding a record to database: ', payload)
        self.db.books.insert_one(payload)

    def update_book(self, id, payload):
        print('[*] Updating a record with id: ', id)
        query = { '_id': ObjectId(id) }
        self.db.books.replace_one(query, payload)


    def remove_book(self, id):
        print('[*] Removing a record with id: ', id)
        self.db.books.delete_one({ '_id': ObjectId(id) })
