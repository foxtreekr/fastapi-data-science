import sqlalchemy
from databases import Database

# Connecting to a database
DATABASE_URL = "sqlite:///chapter6_sqlalchemy.db"
database = Database(DATABASE_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)

# database instance return function
def get_database() -> Database:
    return database
