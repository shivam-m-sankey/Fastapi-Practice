from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

## Request Model
class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]



@app.get('/blog')
async def index(limit : int, published:bool, sort:Optional[str] = None):
    if published:
        return {"data":f"{limit} published blogs from db"}
    else:
        return {"data":f"{limit} unpublished blogs from db"}

@app.get('/blog/unpublised')
async def unpublishedblog():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
async def ahow(id: int):
    #fetch blog with id = id
    return {"data": id} 
@app.get('/blog/{id}/comments')
async def comments(id):
    return {'data' : {1,2}}

@app.post("/blog")
async def createblog(request: Blog):                    
    return {'data': f'Blog title is {request.title}'}

#if __name__=="__main__":
 #   uvicorn.run(app, host="127.0.0.1", port= 9000)