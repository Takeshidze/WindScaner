import json

from geopy.distance import geodesic
import math
from api_req import get_data

def calculate_azimuth(start_coords, end_coords):
    lat1, lon1 = start_coords
    lat2, lon2 = end_coords

    # Конвертируем координаты в радианы
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Вычисляем разницу долготы
    d_lon = lon2_rad - lon1_rad

    # Вычисляем азимут
    y = math.sin(d_lon) * math.cos(lat2_rad)
    x = math.cos(lat1_rad) * math.sin(lat2_rad) - math.sin(lat1_rad) * math.cos(lat2_rad) * math.cos(d_lon)
    azimuth_rad = math.atan2(y, x)
    azimuth_deg = math.degrees(azimuth_rad)

    # Нормализуем азимут в диапазон 0-360 градусов
    normalized_azimuth = (azimuth_deg + 360) % 360

    return normalized_azimuth

start_coord = (55.924912, 37.891909)  # Начальные координаты (широта, долгота)
end_coord = (55.925434, 37.816365)  # Конечные координаты (широта, долгота)
step_distance = 100  # Шаг расстояния (в метрах)

azi = calculate_azimuth(start_coord, end_coord)
current_distance = 0
current_coord = start_coord

upload = []

while current_distance < geodesic(start_coord, end_coord).meters:
    print(current_coord)
    data = get_data(current_coord)
    upload.append(data)#
    # Вычисляем следующую координату с учетом шага расстояния
    current_distance += step_distance
    current_coord = geodesic(start_coord, end_coord).destination(
        point=current_coord, bearing=azi, distance=0.1).format_decimal()

# Создаем файл для записи результатов
with open('result.json', 'w') as file:
    json.dump(upload, file)

