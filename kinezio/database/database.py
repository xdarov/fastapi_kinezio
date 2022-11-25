from sqlalchemy import Column, Date, Integer, MetaData, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .dbsettings import get_db_settings


engine = create_engine(get_db_settings(), echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Bodyparts(Base):
    __tablename__ = 'bodyparts'

    id = Column(Integer, primary_key=True)
    parts_name = Column(String, nullable=False)
    parent_id = Column(Integer)


class CharacterPain(Base):
    __tablename__ = 'character_pain'

    id = Column(Integer, primary_key=True)
    vname = Column(String)


class Client(Base):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String)
    surname = Column(String, nullable=False)
    phone = Column(String)
    birthdate = Column(Date)


class CuppingFactors(Base):
    __tablename__ = 'cupping_factors'

    id = Column(Integer, primary_key=True)
    vname = Column(String)


class FrequencyOfPain(Base):
    __tablename__ = 'frequency_of_pain'

    id = Column(Integer, primary_key=True)
    vname = Column(String)


class ProvokingFactors(Base):
    __tablename__ = 'provoking_factors'

    id =Column (Integer, primary_key=True)
    vname =Column (String)
