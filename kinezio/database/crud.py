from sqlalchemy.orm import Session, joinedload
from .database import Bodyparts, CharacterPain, Client, CuppingFactors, \
    FrequencyOfPain, ProvokingFactors

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
    bodyparts = db.query(Bodyparts).options(joinedload('*')).filter_by(
        parts_name=body_parts_attrs['parts_name']
    )
    if (before := bodyparts.options(joinedload('*')).first()) is not None:
        bodyparts.update(body_parts_attrs)
        res = {
            'status': 'success' if before != (after := bodyparts.first()) else 'no',
            'update': {
                'before': before,
                'after': after
            }
        }
    else:
        bodyparts = Bodyparts(**body_parts_attrs)
        db.add(bodyparts)
        res = {
            'status': 'success',
            'create': bodyparts
        }
    db.commit()
    # print(f'=====>{res}')
    return dict(res)


def update_character_pain(character_pain_attrs: dict, db: Session):
    characterpain = db.query(CharacterPain).filter_by(
        vname=character_pain_attrs['vname']
    )
    if characterpain.first() is None:
        characterpain = CharacterPain(**character_pain_attrs)
        db.add(characterpain)
        db.commit()


def update_client(client_attrs: dict, db: Session):
    client = Client(**client_attrs)
    db.add(client)
    db.commit()


def update_cupping_factors(cupping_factors_attrs: dict, db: Session):
    cupping_factors = db.query(CuppingFactors).filter_by(
        vname=cupping_factors_attrs['vname']
    )
    if cupping_factors.first() is None:
        cupping_factors = CuppingFactors(**cupping_factors_attrs)
        db.add(cupping_factors)
        db.commit()


def update_frequency_of_pain(frequency_of_pain_attrs: dict, db: Session):
    frequency_of_pain = db.query(FrequencyOfPain).filter_by(
        vname=frequency_of_pain_attrs['vname']
    )
    if frequency_of_pain.first() is None:
        frequency_of_pain = FrequencyOfPain(**frequency_of_pain_attrs)
        db.add(frequency_of_pain)
        db.commit()


def update_provoking_factors(provoking_factors_attrs: dict, db: Session):
    provoking_factors = db.query(ProvokingFactors).filter_by(
        vname=provoking_factors_attrs['vname']
    )
    if provoking_factors.first() is None:
        provoking_factors = ProvokingFactors(**provoking_factors_attrs)
        db.add(provoking_factors)
        db.commit()
