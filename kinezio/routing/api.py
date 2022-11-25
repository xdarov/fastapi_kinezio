from fastapi import APIRouter, Depends
from database.database import get_db
from database import crud


router = APIRouter(prefix='/api', tags=['API_GET'])


@router.get('/body_parts')
def body_parts(db: crud.Session = Depends(get_db)):
    return {'body_parts': crud.get_body_parts(db)}


@router.get('/character_pain')
def character_pain(db: crud.Session = Depends(get_db)):
    return {'character_pain': crud.get_character_pain(db)}


@router.get('/clients')
def client(db: crud.Session = Depends(get_db)):
    return {'client': crud.get_client(db)}


@router.get('/cupping_factors')
def cupping_factors(db: crud.Session = Depends(get_db)):
    return {'cupping_factors': crud.get_cupping_factors(db)}


@router.get('/frequency_of_pain')
def frequency_of_pain(db: crud.Session = Depends(get_db)):
    return {'frequency_of_pain': crud.get_frequency_of_pain(db)}


@router.get('/provoking_factors')
def provoking_factors(db: crud.Session = Depends(get_db)):
    return {'provoking_factors': crud.get_provoking_factors(db)}
