from fastapi import FastAPI
import emoji

app = FastAPI()

@app.get("/")
async def root(icon: str = ""):
    return {"meaning": emoji.demojize(icon)}