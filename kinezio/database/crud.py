from sqlalchemy.orm import Session, joinedload, load_only, selectinload, \
    lazyload, raiseload, contains_eager
from .database import Bodyparts, CharacterPain, Client, CuppingFactors, \
    FrequencyOfPain, ProvokingFactors
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

'''=========================================='''
'''=================  API  =================='''
'''=========================================='''


def get_body_parts(db: Session):
    bodyparts = db.query(Bodyparts).order_by(Bodyparts.id).all()
    return bodyparts


def get_character_pain(db: Session):
    character_pain = db.query(CharacterPain).order_by().all()
    return character_pain


def get_client(db: Session):
    client = db.query(Client).order_by(Client.id).all()
    return client


def get_cupping_factors(db: Session):
    cupping_factors = db.query(CuppingFactors).order_by(
        CuppingFactors.id).all()
    return cupping_factors


def get_frequency_of_pain(db: Session):
    frequency_of_pain = db.query(FrequencyOfPain).order_by(
        FrequencyOfPain.id).all()
    return frequency_of_pain


def get_provoking_factors(db: Session):
    provoking_factors = db.query(ProvokingFactors).order_by(
        ProvokingFactors.id).all()
    return provoking_factors


'''=========================================='''
'''================  UPDATE  ================'''
'''=========================================='''


def update_body_parts(body_parts_attrs: dict, db: Session):
    bodyparts = db.query(Bodyparts).filter_by(
        parts_name=body_parts_attrs['parts_name']
    )
    if (before := bodyparts.first()) is not None:
        before = before.dict()
        bodyparts.update(body_parts_attrs)
        res = before, bodyparts.first().dict()
    else:
        bodyparts = Bodyparts(**body_parts_attrs)
        db.add(bodyparts)
        db.commit()
        db.refresh(bodyparts)
        res = bodyparts.dict()
    return res


def update_character_pain(character_pain_attrs: dict, db: Session):
    characterpain = db.query(CharacterPain).filter_by(
        vname=character_pain_attrs['vname']
    )
    if characterpain.first() is None:
        characterpain = CharacterPain(**character_pain_attrs)
        db.add(characterpain)
        db.commit()
        db.refresh(characterpain)
        res = characterpain.dict()
        return res


def update_client(client_attrs: dict, db: Session):
    client = Client(**client_attrs)
    db.add(client)
    db.commit()
    db.refresh(client)
    res = client.dict()
    return res


def update_cupping_factors(cupping_factors_attrs: dict, db: Session):
    cupping_factors = db.query(CuppingFactors).filter_by(
        vname=cupping_factors_attrs['vname']
    )
    if cupping_factors.first() is None:
        cupping_factors = CuppingFactors(**cupping_factors_attrs)
        db.add(cupping_factors)
        db.commit()
        db.refresh(cupping_factors)
        res = cupping_factors.dict()
        return res


def update_frequency_of_pain(frequency_of_pain_attrs: dict, db: Session):
    frequency_of_pain = db.query(FrequencyOfPain).filter_by(
        vname=frequency_of_pain_attrs['vname']
    )
    if frequency_of_pain.first() is None:
        frequency_of_pain = FrequencyOfPain(**frequency_of_pain_attrs)
        db.add(frequency_of_pain)
        db.commit()
        db.refresh(frequency_of_pain)
        res = frequency_of_pain.dict()
        return res


def update_provoking_factors(provoking_factors_attrs: dict, db: Session):
    provoking_factors = db.query(ProvokingFactors).filter_by(
        vname=provoking_factors_attrs['vname']
    )
    if provoking_factors.first() is None:
        provoking_factors = ProvokingFactors(**provoking_factors_attrs)
        db.add(provoking_factors)
        db.commit()
        db.refresh(provoking_factors)
        res = provoking_factors.dict()
        return res


'''=========================================='''
'''================  DELETE  ================'''
'''=========================================='''


MODELS = {
    'body_parts': Bodyparts,
    'character_pain': CharacterPain,
    'client': Client,
    'cupping_factors': CuppingFactors,
    'frequency_of_pain': FrequencyOfPain,
    'provoking_factors': ProvokingFactors
}


def delete_element(condition: dict, model, db: Session):
    try:
        frequency_of_pain = db.query(MODELS[model]).filter_by(**condition)
        res = frequency_of_pain.one().dict()
        db.delete(frequency_of_pain.one())
        db.commit()
        return res
    except MultipleResultsFound:
        return "MultipleResultsFound"
    except NoResultFound:
        return "NoResultFound"
