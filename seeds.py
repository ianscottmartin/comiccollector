from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite///comicbkdata.db")

Session = sessionmaker()
session = Session()


users =
[User(), User(), User()]

session.bulk_save_objects(users)
session.commit()
