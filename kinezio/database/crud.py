from sqlalchemy.orm import Session, joinedload, load_only
    # selectinload, lazyload, raiseload, contains_eager, noload
from .database import Bodyparts, CharacterPain, Client, CuppingFactors, \
    FrequencyOfPain, ProvokingFactors


def get_body_parts(db: Session):
    bodyparts = db.query(Bodyparts).all()
    return bodyparts


def get_character_pain(db: Session):
    character_pain = db.query(CharacterPain).all()
    return character_pain


def get_clients(db: Session):
    clients = db.query(Client).all()
    return clients


def get_cupping_factors(db: Session):
    cupping_factors = db.query(CuppingFactors).all()
    return cupping_factors


def get_frequency_of_pain(db: Session):
    frequency_of_pain = db.query(FrequencyOfPain).all()
    return frequency_of_pain


def get_provoking_factors(db: Session):
    provoking_factors = db.query(ProvokingFactors).all()
    return provoking_factors
