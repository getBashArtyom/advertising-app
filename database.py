from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]

collection.delete_many({})

# test
data = [
    {
        "address": "ул. Первая, 123",
        "cords": [48.683840, 44.477790],
        "type": "Banner",
        "owner": "Company A",
        "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.490370%2C48.677806&mode=whatshere&panorama%5Bdirection%5D=209.515829%2C9.978950&panorama%5Bfull%5D=true&panorama%5Bid%5D=1339063221_742080036_23_1619694025&panorama%5Bpoint%5D=44.477965%2C48.683797&panorama%5Bspan%5D=77.389346%2C29.228027&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=15.04" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект имени В.И. Ленина — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.490370%2C48.677806&mode=whatshere&panorama%5Bdirection%5D=209.515829%2C9.978950&panorama%5Bfull%5D=true&panorama%5Bid%5D=1339063221_742080036_23_1619694025&panorama%5Bpoint%5D=44.477965%2C48.683797&panorama%5Bspan%5D=77.389346%2C29.228027&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=15.04" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>'
    },
    {
        "address": "ул. Вторая, 456",
        "cords": [48.704110, 44.511995],
        "type": "Billboard",
        "owner": "Company B",
        "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.513228%2C48.703426&mode=whatshere&panorama%5Bdirection%5D=177.811134%2C14.026192&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.511502%2C48.703600&panorama%5Bspan%5D=77.832958%2C29.450570&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=17.43" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект имени В.И. Ленина — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.513228%2C48.703426&mode=whatshere&panorama%5Bdirection%5D=177.811134%2C14.026192&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.511502%2C48.703600&panorama%5Bspan%5D=77.832958%2C29.450570&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=17.43" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>'
    },

]
result = collection.insert_many(data)
print("Вставлены документы с идентификаторами:", result.inserted_ids)