import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index():
    return {"success": False}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, reload=True)
