import pytest
from fastapi.testclient import TestClient
from pymongo import MongoClient

from main import app


@pytest.fixture
def client():
    """Create a TestClient for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(scope="session")
def mongodb():
    """Fixture for MongoDB connection."""
    client = MongoClient("mongodb://localhost:27017")
    db = client["fake_ads"]

    yield db
    client.drop_database("fake_ads")
    client.close()


def test_db_connection(mongodb):
    assert mongodb.name == "fake_ads"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]


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


def test_insert_banner_data(mongodb):
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

    mongodb.banners.insert_one(banner_data)
    assert mongodb.banners.count_documents({"address": "ул. Шестая, 12"}) == 1


def test_insert_banner_data(mongodb):
    mongodb.delete_one({"address": "ул. Шестая, 12"})


assert mongodb.banners.count_documents({"address": "ул. Шестая, 12"}) == 0


def test_update_banner(client):
    banner_id = "661ec817ea487652df65478a"
    updated_data = {"_id": banner_id, "title": "Updated Banner", "price": 15.99}
    response = client.post("/update_banner", json=updated_data)
    assert response.status_code == 200


def test_delete_banner(client):
    banner_id = "661ec817ea487652df65478a"
    banner_data = {"banner_id": banner_id}
    response = client.post("/delete_banner", json=banner_data)
    assert response.status_code == 200
