from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import sys

this_file_path = os.path.dirname(__file__)
sys.path.append(os.path.join(this_file_path, "../"))

Base = declarative_base()
path = "Persistencia/ppai.db"
engine = create_engine("sqlite:///" + path, echo=True)
Session = sessionmaker(bind=engine)


session = Session()


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

