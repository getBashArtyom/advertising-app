from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from search import  find_nearest_banners
from fastapi.staticfiles import StaticFiles
from bson import ObjectId
from fastapi.responses import JSONResponse


from models import Banner

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]

templates = Jinja2Templates(directory=".")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/nearest_banners", response_class=HTMLResponse)
def nearest_banners(request: Request, user_lat: float, user_lon: float, price: float):

    banners = collection.find({"price": {"$lte": price}})

    nearest_banners = find_nearest_banners(user_lat, user_lon, banners)
    print(nearest_banners)
    if nearest_banners:
        return templates.TemplateResponse("nearest_banners.html", {"request": request, "banners": nearest_banners})
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Banner not found")

@app.get("/add_banner", response_class=HTMLResponse)
def add_banner(request: Request):
    return templates.TemplateResponse("add_banner.html", {"request": request})

@app.post("/add_banner")
def add_banner_post(banner: Banner):
    collection.insert_one(banner.dict())
    return {"message": "Banner added successfully!"}
    #

@app.get("/get_banner/{banner_id}")
def get_banner(banner_id: str):
    banner = collection.find_one({"_id": ObjectId(banner_id)})
    if banner:
        banner['_id'] = str(banner['_id'])
        # Если баннер найден, возвращаем его данные
        return JSONResponse(content=banner, status_code=200)

@app.post("/update_banner")
def update_banner(banner_data: dict):
    banner_id = banner_data.get("_id")
    updated_fields = {
        field: value for field, value in banner_data.items() if field != "_id"
    }
    result = collection.update_one({"_id": ObjectId(banner_id)}, {"$set": updated_fields})

@app.post("/delete_banner")
def update_banner(banner_data: dict):
    banner_id = banner_data.get("banner_id")
    result = collection.delete_one({'_id': ObjectId(banner_id)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
