from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["fake_ads"]
collection = db["ads"]

# collection.delete_many({})

# test
# data = [
#     {
#         "address": "ул. Первая, 123",
#         "cords": [48.683840, 44.477790],
#         "price": 4000,
#         "type": "Банер",
#         "owner": "Company A",
#         "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.490370%2C48.677806&mode=whatshere&panorama%5Bdirection%5D=209.515829%2C9.978950&panorama%5Bfull%5D=true&panorama%5Bid%5D=1339063221_742080036_23_1619694025&panorama%5Bpoint%5D=44.477965%2C48.683797&panorama%5Bspan%5D=77.389346%2C29.228027&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=15.04" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект имени В.И. Ленина — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.490370%2C48.677806&mode=whatshere&panorama%5Bdirection%5D=209.515829%2C9.978950&panorama%5Bfull%5D=true&panorama%5Bid%5D=1339063221_742080036_23_1619694025&panorama%5Bpoint%5D=44.477965%2C48.683797&panorama%5Bspan%5D=77.389346%2C29.228027&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=15.04" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>',
#         "size": "500x500",
#         "status": "В аренде",
#         "exp_date": "01.08"
#     },
#     {
#         "address": "ул. Вторая, 456",
#         "cords": [48.704110, 44.511995],
#         "price": 2500,
#         "type": "Цифровой банер",
#         "owner": "Company B",
#         "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.513228%2C48.703426&mode=whatshere&panorama%5Bdirection%5D=177.811134%2C14.026192&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.511502%2C48.703600&panorama%5Bspan%5D=77.832958%2C29.450570&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=17.43" style="color:#eee;font-size:12px;position:absolute;top:14px;">Проспект имени В.И. Ленина — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.513228%2C48.703426&mode=whatshere&panorama%5Bdirection%5D=177.811134%2C14.026192&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.511502%2C48.703600&panorama%5Bspan%5D=77.832958%2C29.450570&whatshere%5Bpoint%5D=44.511995%2C48.704110&whatshere%5Bzoom%5D=19.99&z=17.43" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>',
#         "type": "Щит на стойке",
#         "size": "300x200",
#         "status": "Не работает",
#     },
#     {
#         "address": "ул. Третья, 66",
#         "cords": [48.637395, 44.430676],
#         "price": 10000,
#         "type": "Рекламный щит",
#         "owner": "Company B",
#         "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.435926%2C48.633782&panorama%5Bdirection%5D=51.450964%2C5.535454&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.430931%2C48.637668&panorama%5Bspan%5D=82.205672%2C31.708912&utm_medium=mapframe&utm_source=maps&z=16.19" style="color:#eee;font-size:12px;position:absolute;top:14px;">Яндекс Карты — транспорт, навигация, поиск мест</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.435926%2C48.633782&panorama%5Bdirection%5D=51.450964%2C5.535454&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.430931%2C48.637668&panorama%5Bspan%5D=82.205672%2C31.708912&z=16.19" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>',
#         "type": "Щит на стойке",
#         "size": "300x200",
#         "status": "Не работает",
#     },
#     {
#         "address": "ул. Четвертая, 6",
#         "cords": [48.625972, 44.426502],
#         "price": 7000,
#         "type": "Щит",
#         "owner": "Company O",
#         "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.435926%2C48.633782&panorama%5Bdirection%5D=195.385695%2C2.692838&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.426497%2C48.625999&panorama%5Bspan%5D=44.820712%2C15.291226&utm_medium=mapframe&utm_source=maps&z=16.19" style="color:#eee;font-size:12px;position:absolute;top:14px;">Яндекс Карты — транспорт, навигация, поиск мест</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.435926%2C48.633782&panorama%5Bdirection%5D=195.385695%2C2.692838&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.426497%2C48.625999&panorama%5Bspan%5D=44.820712%2C15.291226&z=16.19" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>',
#         "type": "Щит на стойке",
#         "size": "300x200",
#         "status": "В аренде",
#         "exp_date": "06.10",
#     },
#     {
#         "address": "ул. Пятая, 17",
#         "cords": [48.615201, 44.422771],
#         "price": 6500,
#         "type": "Банер",
#         "owner": "Company С",
#         "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422738%2C48.613695&panorama%5Bspan%5D=121.169773%2C60.000000&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57" style="color:#eee;font-size:12px;position:absolute;top:14px;">Улица 64-й Армии — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422738%2C48.613695&panorama%5Bspan%5D=121.169773%2C60.000000&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>',
#         "type": "Щит на стойке",
#         "size": "300x200",
#         "status": "Не работает",
#     },
#     {
#         "address": "ул. Шестая, 22",
#         "cords": [48.611940, 44.422494],
#         "price": 1200,
#         "type": "Щит на стойке",
#         "owner": "Company D",
#         "html_code": '<div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/38/volgograd/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0px;">Волгоград</a><a href="https://yandex.ru/maps/38/volgograd/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422615%2C48.612197&panorama%5Bspan%5D=121.169773%2C60.000000&utm_medium=mapframe&utm_source=maps&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57" style="color:#eee;font-size:12px;position:absolute;top:14px;">Улица 64-й Армии — Яндекс Карты</a><iframe src="https://yandex.ru/map-widget/v1/?l=stv%2Csta&ll=44.430901%2C48.616793&mode=whatshere&panorama%5Bdirection%5D=183.456725%2C1.763250&panorama%5Bfull%5D=true&panorama%5Bpoint%5D=44.422615%2C48.612197&panorama%5Bspan%5D=121.169773%2C60.000000&whatshere%5Bpoint%5D=44.426502%2C48.625972&whatshere%5Bzoom%5D=14.59&z=15.57" width="560" height="400" frameborder="1" allowfullscreen="true" style="position:relative;"></iframe></div>',
#         "type": "Щит на стойке",
#         "size": "300x200",
#         "status": "В аренде",
#         "exp_date": "01.11"
#     },
#
# ]
# result = collection.insert_many(data)
