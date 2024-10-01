from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated

from models import *
from sqlalchemy import insert
from schemas import CreateUser, UpdateUser

from slugify import slugify
from sqlalchemy import select
from sqlalchemy import update

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.is_active == True)).all()
    if users is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no users'
        )
    return users

@router.get('/user_id')
async def user_by_id():
    pass

@router.post('/create')
async def create_user():
    pass

@router.put('/update')
async def update_user():
    pass

@router.delete('/delete')
async def delete_user():
    pass