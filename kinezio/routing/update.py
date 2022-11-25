from fastapi import APIRouter, Depends
from database.database import get_db
from database import crud, schemas

router = APIRouter(prefix='/update', tags=['POST'])

@router.post('/body_parts')
def update_body_parts(
    body_parts: schemas.BodyPartsSchem,
    db: crud.Session = Depends(get_db)
):
    crud.update_body_parts(body_parts.dict(), db)
    return {'result': 'success'}


@router.post('/character_pain')
def update_character_pain(
    character_pain: schemas.CharacterPainSchem,
    db: crud.Session = Depends(get_db)
):
    crud.update_character_pain(character_pain.dict(), db)
    return {'result': 'success'}


@router.post('/client')
def update_client(
    client: schemas.ClientSchem,
    db: crud.Session = Depends(get_db)
):
    crud.update_client(client.dict(), db)
    return {'result': 'success'}


@router.post('/cupping_factors')
def update_cupping_factors(
    cupping_factors: schemas.CuppingFactorsSchem,
    db: crud.Session = Depends(get_db)
):
    crud.update_cupping_factors(cupping_factors.dict() ,db)
    return {'result': 'success'}


@router.post('/frequency_of_pain')
def update_frequency_of_pain(
    frequency_of_pain: schemas.FrequencyOfPainSchem,
    db: crud.Session = Depends(get_db)
):
    crud.update_frequency_of_pain(frequency_of_pain.dict(), db)
    return {'result': 'success'}

@router.post('/provoking_factors')
def update_provoking_factors(
    provoking_factors: schemas.ProvokingFactorsSchem,
    db: crud.Session = Depends(get_db)
):
    crud.update_provoking_factors(provoking_factors.dict(), db)
    return {'result': 'success'}
