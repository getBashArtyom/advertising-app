from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]

collection.delete_many({})

# test
data = [
    {
        "address": "ул. Первая, 123",
        "cords": [55.123, 37.456],
        "type": "Banner",
        "owner": "Company A",
        "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.508750%2C48.704757&mode=whatshere&panorama%5Bdirection%5D=208.471993%2C11.685667&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.519885%2C48.701912&panorama%5Bspan%5D=121.169773%2C60.000000&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.508829%2C48.707983&whatshere%5Bzoom%5D=16.12&z=16" style="color:#eee;font-size:12px;position:absolute;top:14px;">Улица В.И. Ленина, 25 на карте Волгограда — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.508750%2C48.704757&mode=whatshere&panorama%5Bdirection%5D=208.471993%2C11.685667&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.519885%2C48.701912&panorama%5Bspan%5D=121.169773%2C60.000000&whatshere%5Bpoint%5D=44.508829%2C48.707983&whatshere%5Bzoom%5D=16.12&z=16" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>'
    },
    {
        "address": "ул. Вторая, 456",
        "cords": [55.789, 37.890],
        "type": "Billboard",
        "owner": "Company B",
        "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.508750%2C48.704757&mode=whatshere&panorama%5Bdirection%5D=34.357502%2C0.000000&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.511402%2C48.703675&panorama%5Bspan%5D=121.169773%2C60.000000&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.508829%2C48.707983&whatshere%5Bzoom%5D=16.12&z=16" style="color:#eee;font-size:12px;position:absolute;top:14px;">Улица В.И. Ленина, 25 на карте Волгограда — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.508750%2C48.704757&mode=whatshere&panorama%5Bdirection%5D=34.357502%2C0.000000&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.511402%2C48.703675&panorama%5Bspan%5D=121.169773%2C60.000000&whatshere%5Bpoint%5D=44.508829%2C48.707983&whatshere%5Bzoom%5D=16.12&z=16" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>'
    },

]
result = collection.insert_many(data)
print("Вставлены документы с идентификаторами:", result.inserted_ids)