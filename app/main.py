from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    response = {
        'message': 'Hello World!'
    }
    return response
