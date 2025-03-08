from fastapi import FastAPI
from typing import Optional


app = FastAPI()

@app.get('/')
async def read_root():
    return{'message':'hello world'}

@app.get('/greet/{name}')
async def greet(name:str) -> dict:
    return{'message':f'hello {name}'}

# query parameter
@app.get('/greet2')
async def greet(name:str,age:int)->dict:
    return{"message":f"hello, {name}","Age":age}

# query optional parameter
@app.get('/greet3')
async def greet(name:Optional[str]="sabuj",age:Optional[int]=18)->dict:
    return{"Massage":f"Hello, {name}","Age":age}