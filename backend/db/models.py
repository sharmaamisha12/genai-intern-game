from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GlobalGuess(Base):
    __tablename__ = "global_guesses"

    guess = Column(String, primary_key=True)
    count = Column(Integer, default=0)