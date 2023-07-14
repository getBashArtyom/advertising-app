from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from search import  find_nearest_banners

app = FastAPI()


client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/nearest_banners", response_class=HTMLResponse)
def nearest_banners(request: Request, user_lat: float, user_lon: float):
    banners = collection.find()

    nearest_banners = find_nearest_banners(user_lat, user_lon, banners, limit=5)
    #print(nearest_banners)
    return templates.TemplateResponse("nearest_banners.html", {"request": request, "banners": nearest_banners})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)