from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database,models
from ..repository import blog
from typing import List
from .. import oauth2


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
) 

get_db = database.get_db

#fetch total blogs info
@router.get('/',response_model=List[schemas.ShowBlog])
async def all(db:Session = Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user) ):
    return await blog.get_all(db)
   

## Creating blog
@router.post('/',status_code=status.HTTP_201_CREATED)
async def create(request:schemas.Blog,db: Session= Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return await blog.create(request, db)

## taking as output
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
async def show(id:int, db: Session= Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return await blog.show(id,db)



#deleting blog
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id:int, db: Session = Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return await blog.destroy(id,db)

#updating blog
@router.put('/{id}', status_code= status.HTTP_202_ACCEPTED)
async def update(id:int, request:schemas.Blog,db: Session= Depends(get_db), current_user: schemas.User=Depends(oauth2.get_current_user)):
    return  await blog.update(id,request,db)