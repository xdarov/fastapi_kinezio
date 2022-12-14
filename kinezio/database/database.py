from sqlalchemy import Column, Date, Integer, String, create_engine
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


class FormatMixin:
    def dict(self) -> dict:
        values: dict = self.__dict__
        values.pop('_sa_instance_state')
        return values


class Bodyparts(Base, FormatMixin):
    __tablename__ = 'bodyparts'

    id = Column(Integer, primary_key=True)
    parts_name = Column(String, nullable=False)
    parent_id = Column(Integer)

    def __repr__(self):
        return f'{self.parts_name} {self.parent_id}'


class CharacterPain(Base, FormatMixin):
    __tablename__ = 'character_pain'

    id = Column(Integer, primary_key=True)
    vname = Column(String)


class Client(Base, FormatMixin):
    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    second_name = Column(String)
    surname = Column(String, nullable=False)
    phone = Column(String)
    birthdate = Column(Date)


class CuppingFactors(Base, FormatMixin):
    __tablename__ = 'cupping_factors'

    id = Column(Integer, primary_key=True)
    vname = Column(String)


class FrequencyOfPain(Base, FormatMixin):
    __tablename__ = 'frequency_of_pain'

    id = Column(Integer, primary_key=True)
    vname = Column(String)


class ProvokingFactors(Base, FormatMixin):
    __tablename__ = 'provoking_factors'

    id = Column(Integer, primary_key=True)
    vname = Column(String)
