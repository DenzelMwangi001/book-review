# Book Review Platform

A simple Flask-based web API for managing books, authors, and reviews. This project uses Flask, SQLAlchemy, and SQLite to create a backend for storing and retrieving book data and associated reviews.

## Features

- Add, update, delete books
- Link books to authors
- Add and view reviews for each book
- API endpoints to retrieve all books or a single book with nested author and review data
- Uses SQLAlchemy ORM and Flask-Migrate for database management
- Includes seeding script to populate the database with example data

## Technologies Used

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- BeautifulSoup (optional, for web scraping)

## Getting Started

### 1. Clone the repository

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Set up the database

flask db init
flask db migrate -m "Initial migration"
flask db upgrade
python seed.py

5. Run the application

flask run

Visit: http://127.0.0.1:5000/books


---

API Endpoints

Method	Endpoint	Description

GET	/books	Get all books with authors & reviews
GET	/books/<id>	Get a single book by ID
POST	/books	Add a new book
PATCH	/books/<id>	Update book info
DELETE	/books/<id>	Delete a book and its reviews



---

Example Seed Data

Authors: George Orwell, Jane Austen

Books: 1984, Animal Farm, Pride and Prejudice, Emma

Reviews: Sample reviews with ratings and comments for each book
