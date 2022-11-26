from fastapi import APIRouter, Depends
from database.database import get_db
from database import crud


router = APIRouter(prefix='/delete', tags=['DELETE'])


def create_answer(res):
    if isinstance(res, dict):
        res = {
            'status': 'success',
            'delete': res
        }
    else:
        res = {
            'status': 'fail',
            'error': res
        }
    return res


@router.post('/body_parts')
def delete_body_parts(name: str, db: crud.Session = Depends(get_db)):
    res = crud.delete_element({'parts_name': name}, 'body_parts', db)
    return create_answer(res)


@router.post('/character_pain')
def delete_character_pain(name: str, db: crud.Session = Depends(get_db)):
    res = crud.delete_element({'vname': name}, 'character_pain', db)
    return create_answer(res)


@router.post('/client')
def delete_client(client_id: int, db: crud.Session = Depends(get_db)):
    res = crud.delete_element({'id': client_id}, 'client', db)
    return create_answer(res)


@router.post('/cupping_factors')
def delete_cuppin_gactors(name: str, db: crud.Session = Depends(get_db)):
    res = crud.delete_element({'vname': name}, 'cupping_factors', db)
    return create_answer(res)


@router.post('/frequency_of_pain')
def delete_frequency_of_pain(name: str, db: crud.Session = Depends(get_db)):
    res = crud.delete_element({'vname': name}, 'frequency_of_pain', db)
    return create_answer(res)


@router.post('/provoking_factors')
def delete_provoking_factors(name: str, db: crud.Session = Depends(get_db)):
    res = crud.delete_element({'vname': name}, 'provoking_factors', db)
    return create_answer(res)
