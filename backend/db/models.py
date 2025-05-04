# backend/db/models.py
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class GlobalGuess(Base):
    __tablename__ = 'global_guesses'
    guess = Column(String, primary_key=True)
    count = Column(Integer, default=0)

Base.metadata.create_all(engine)

def update_global_counter(guess):
    session = Session()
    obj = session.query(GlobalGuess).filter_by(guess=guess.lower()).first()
    if obj:
        obj.count += 1
    else:
        obj = GlobalGuess(guess=guess.lower(), count=1)
        session.add(obj)
    session.commit()
    session.close()
    return obj.count

def get_global_count(guess):
    session = Session()
    obj = session.query(GlobalGuess).filter_by(guess=guess.lower()).first()
    session.close()
    return obj.count if obj else 0
