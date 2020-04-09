from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
from db import DB

db = DB()

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

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
def test():
    return jsonify('Miki stana...')
app.add_url_rule('/', 'test', test)

# Get all books
app.add_url_rule('/books', 'get_all', db.get_all)

# Add a new books
@app.route('/books/add', methods=['POST'])
def add_book():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        db.add_book(post_data)
        response_object['message'] = 'Book added!'
    return jsonify(response_object)

# Update or delete a book
@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        db.remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        db.remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
