from flask import Flask, jsonify, request, abort
from flask_migrate import Migrate
from models import db, Author, Book, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([
        {
            'id': book.id,
            'title': book.title,
            'publication_year': book.publication_year,
            'author': book.author.name,
            'reviews': [
                {'rating': r.rating, 'comment': r.comment} for r in book.reviews
            ]
        } for book in books
    ])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({
        'id': book.id,
        'title': book.title,
        'publication_year': book.publication_year,
        'author': book.author.name,
        'reviews': [{'rating': r.rating, 'comment': r.comment} for r in book.reviews]
    })

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    try:
        new_book = Book(
            title=data['title'],
            publication_year=data['publication_year'],
            author_id=data['author_id']
        )
        db.session.add(new_book)
        db.session.commit()
        return jsonify({'message': 'Book added'}), 201
    except Exception as e:
        abort(400, description=str(e))

@app.route('/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    if 'title' in data:
        book.title = data['title']
    if 'publication_year' in data:
        book.publication_year = data['publication_year']
    db.session.commit()
    return jsonify({'message': 'Book updated'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book and reviews deleted'})