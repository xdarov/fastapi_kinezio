from fastapi import APIRouter, Depends
from database.database import get_db
from database import crud, schemas


router = APIRouter(prefix='/delete', tags=['DELETE'])


@router.post('/')
def delete_bodyparts():
    pass