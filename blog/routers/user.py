from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas,database
from ..repository import user


router = APIRouter(
     prefix="/user",
     tags=['Users']
)

get_db = database.get_db



##users 
@router.post('/', response_model=schemas.ShowUser)
async def create_user(request:schemas.User, db:Session=Depends(get_db)):
    return await user.create_user(request,db)
    

##fetching using user from database on the basis of user id 
@router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id:int, db: Session= Depends(get_db)):
    return await user.get_user(id,db)