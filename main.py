from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from search import  find_nearest_banners
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]
print(db)
templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/nearest_banners", response_class=HTMLResponse)
def nearest_banners(request: Request, user_lat: float, user_lon: float, price: float):

    banners = collection.find({"price": {"$lte": price}})

    # Преобразуем результат запроса в список словарей
    banners_list = list(banners)

    nearest_banners = find_nearest_banners(user_lat, user_lon, banners_list)

    return templates.TemplateResponse("nearest_banners.html", {"request": request, "banners": nearest_banners})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
