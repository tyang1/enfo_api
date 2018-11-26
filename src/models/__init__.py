#It’s a good idea to keep your SQLAlchemy object instance in separate file, to avoid circular imports:

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()