from app import app, db
from models import Author, Book, Review

with app.app_context():
    db.drop_all()
    db.create_all()

    author1 = Author(name="George Orwell")
    author2 = Author(name="Jane Austen")

    book1 = Book(title="1984", publication_year=1949, author=author1)
    book2 = Book(title="Animal Farm", publication_year=1945, author=author1)
    book3 = Book(title="Pride and Prejudice", publication_year=1813, author=author2)
    book4 = Book(title="Emma", publication_year=1815, author=author2)

    r1 = Review(rating=5, comment="Amazing dystopia!")
    r2 = Review(rating=4, comment="Classic satire.")
    r3 = Review(rating=5, comment="Loved the characters.")
    r4 = Review(rating=3, comment="A bit long.")
    r5 = Review(rating=4, comment="Charming story.")
    r6 = Review(rating=2, comment="Too slow for me.")

    book1.reviews.extend([r1, r2])
    book3.reviews.append(r3)
    book4.reviews.extend([r4, r5, r6])

    db.session.add_all([author1, author2, book1, book2, book3, book4, r1, r2, r3, r4, r5, r6])
    db.session.commit()
    print("Database seeded.")