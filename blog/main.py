from fastapi import FastAPI
from .database import engine
from .routers import blog, user,authentication
from . import models

app = FastAPI()

## Creating database
models.Base.metadata.create_all(engine)

## User Login
app.include_router(authentication.router)

#routing blog
app.include_router(blog.router)

#routinig user
app.include_router(user.router)




