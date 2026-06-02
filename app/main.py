from fastapi import FastAPI
app = FastAPI(title='Async Payment API')

@app.get('/')
async def root():
    return {'status':'ok'}
