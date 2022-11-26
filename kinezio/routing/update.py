from fastapi import APIRouter, Depends
from database.database import get_db
from database import crud, schemas


router = APIRouter(prefix='/update', tags=['POST'])


def create_answer(res):
    if isinstance(res, tuple):
        res = {
            'status': 'success' if res[0] != res[1] else 'fail',
            'update': {
                'before': res[0],
                'after': res[1]
            }
        }
    else:
        res = {
            'status': 'success',
            'create': res
        } if res is not None else {
            'status': 'fail',
            'error': 'object already exists'
        }
    return res


@router.post('/body_parts')
def update_body_parts(
    body_parts: schemas.BodyPartsSchem,
    db: crud.Session = Depends(get_db)
):
    res = crud.update_body_parts(body_parts.dict(), db)
    return create_answer(res)


@router.post('/character_pain')
def update_character_pain(
    character_pain: schemas.CharacterPainSchem,
    db: crud.Session = Depends(get_db)
):
    res = crud.update_character_pain(character_pain.dict(), db)
    return create_answer(res)


@router.post('/client')
def update_client(
    client: schemas.ClientSchem,
    db: crud.Session = Depends(get_db)
):
    res = crud.update_client(client.dict(), db)
    return create_answer(res)


@router.post('/cupping_factors')
def update_cupping_factors(
    cupping_factors: schemas.CuppingFactorsSchem,
    db: crud.Session = Depends(get_db)
):
    res = crud.update_cupping_factors(cupping_factors.dict(), db)
    return create_answer(res)


@router.post('/frequency_of_pain')
def update_frequency_of_pain(
    frequency_of_pain: schemas.FrequencyOfPainSchem,
    db: crud.Session = Depends(get_db)
):
    res = crud.update_frequency_of_pain(frequency_of_pain.dict(), db)
    return create_answer(res)


@router.post('/provoking_factors')
def update_provoking_factors(
    provoking_factors: schemas.ProvokingFactorsSchem,
    db: crud.Session = Depends(get_db)
):
    res = crud.update_provoking_factors(provoking_factors.dict(), db)
    return create_answer(res)
