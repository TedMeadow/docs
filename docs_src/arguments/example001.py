from fastapi import FastAPI

app = FastAPI()


@app.get('/items/{item}')
async def root(item: str):
    return {'item': f'{item}'}