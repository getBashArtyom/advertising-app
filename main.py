from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()


client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    banners = collection.find()

    return templates.TemplateResponse("index.html", {"request": request, "banners": banners})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)