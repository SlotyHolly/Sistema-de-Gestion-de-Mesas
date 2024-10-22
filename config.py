import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 'postgresql://user:password@localhost:5432/restaurant_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False