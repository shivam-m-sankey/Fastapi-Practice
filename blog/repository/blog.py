from sqlalchemy.orm import Session
from.. import models, schemas
from fastapi import HTTPException, status

async def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs


async def create(request: schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

async def destroy(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id with {id} is not found')

    blog.delete(synchronize_session=False)
    db.commit()
    return 'Done'
async def update(id:int, request:schemas.Blog,db:Session):
    blog= db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog id with {id} is not found')
    blog.update(request.model_dump())
    db.commit()
    return 'Updated successfully'

async def show(id:int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{id} ID is not available')
    return blog