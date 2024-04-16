import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock
import requests

from pymongo import MongoClient

from models import Banner



client = TestClient(app)

@pytest.fixture
def api_url():
    return "http://localhost:8000"

@pytest.fixture
def db_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["fake_ads"]
        yield db
    finally:
        client.close()

def test_db_connection(db_connection):
    assert db_connection.name == "fake_ads"


nearest_banners_test_data = [

    (0.0, 0.0, 7000, 200),

    (48.615201, 44.422771, 0, 404),

    (10, 50, 10000, 200),

    (10, 50, 1000000, 200),
]

@pytest.mark.parametrize("user_lat, user_lon, price, expected_status_code", nearest_banners_test_data)
def test_nearest_banners(user_lat, user_lon, price, expected_status_code):
    response = client.get(f"/nearest_banners?user_lat={user_lat}&user_lon={user_lon}&price={price}")
    assert response.status_code == expected_status_code


def test_update_banner_success():
    banner_data = {
        "address": "ул. Шестая, 12",
        "cords": [
            48.61194,
            44.422494
        ],
        "price": 1200,
        "type": "Щит на стойке",
        "owner": "zzzzz",
        "html_code": "<div style=\"position:relative;overflow:hidden;\"><a href=\"https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps\" style=\"color:#eee;font-size:12px;position:absolute;top:0px;\">Волгоград</a><a href=\"https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422615%2C48.612197&panorama%5Bspan%5D=121.169773%2C60.000000&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57\" style=\"color:#eee;font-size:12px;position:absolute;top:14px;\">Улица 64-й Армии — Яндекс Карты</a><iframe src=\"https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422615%2C48.612197&panorama%5Bspan%5D=121.169773%2C60.000000&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57\" width=\"560\" height=\"400\" frameborder=\"1\" allowfullscreen=\"true\" style=\"position:relative;\"></iframe></div>",
        "size": "300x200",
        "status": "В аренде",
        "exp_date": "01.11",
        "location": "Жопск"
    }

    response = client.post("/update_banner" , json=banner_data)

    assert response.status_code == 200


#qwe
def test_insert_banner_data(db_connection):
    banner_data = {
        "address": "ул. Шестая, 12",
        "cords": [
            48.61194,
            44.422494
        ],
        "price": 1200,
        "type": "Щит на стойке",
        "owner": "zzzzz",
        "html_code": "<div style=\"position:relative;overflow:hidden;\"><a href=\"https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps\" style=\"color:#eee;font-size:12px;position:absolute;top:0px;\">Волгоград</a><a href=\"https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422615%2C48.612197&panorama%5Bspan%5D=121.169773%2C60.000000&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57\" style=\"color:#eee;font-size:12px;position:absolute;top:14px;\">Улица 64-й Армии — Яндекс Карты</a><iframe src=\"https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422615%2C48.612197&panorama%5Bspan%5D=121.169773%2C60.000000&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57\" width=\"560\" height=\"400\" frameborder=\"1\" allowfullscreen=\"true\" style=\"position:relative;\"></iframe></div>",
        "size": "300x200",
        "status": "В аренде",
        "exp_date": "01.11",
        "location": "Жопск"
    }

    db_connection.banners.insert_one(banner_data)
    assert db_connection.banners.count_documents({"address": "ул. Шестая, 12"}) == 1

def delete_banner_data(db_connection):
        db_connection.banners.delete_one({"address": "ул. Шестая, 12"})




def test_add_banner(api_url):
    response = requests.get(f"{api_url}/add_banner")

    assert response.status_code == 200

    assert "text/html" in response.headers["content-type"]

