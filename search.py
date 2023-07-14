from math import radians, cos, sin, sqrt, atan2


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371
    lat1_rad, lon1_rad, lat2_rad, lon2_rad = map(radians, [lat1, lon1, lat2, lon2])

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = sin(dlat / 2) ** 2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c

    return distance


def find_nearest_banners(user_lat, user_lon, banners, limit=5):
    banners_with_distance = []
    for banner in banners:
        banner_lat, banner_lon = banner['cords']
        distance = calculate_distance(user_lat, user_lon, banner_lat, banner_lon)
        banners_with_distance.append((banner, distance))

    banners_with_distance.sort(key=lambda x: x[1])  #

    nearest_banners = []
    for banner, distance in banners_with_distance[:limit]:
        banner['distance'] = distance
        nearest_banners.append(banner)

    return nearest_banners