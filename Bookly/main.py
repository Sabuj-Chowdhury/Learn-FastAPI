from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return{'message':'hello world'}

@app.get('/greet/{name}')
async def greet(name:str) -> dict:
    return{'message':f'hello {name}'}

# query parameter
@app.get('/greet2')
async def greet(name:str)->dict:
    return{"message":f"hello, {name}"}