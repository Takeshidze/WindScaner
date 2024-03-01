import folium
from folium.plugins import HeatMap
import numpy as np

# Ваши данные с координатами и скоростью ветра
data = [[40, 20, 10],
        [50, 30, 15],
        [30, 10, 8]]

# Создание объекта карты
m = folium.Map(location=[0, 0], zoom_start=2)

# Создание пустой матрицы для картографических данных
heatmap_data = np.zeros((100, 100))

# Заполнение матрицы данными о скорости ветра на основе координат
for point in data:
    latitude = point[0]
    longitude = point[1]
    speed = point[2]

    # Преобразование координат в пиксели на основе размера карты
    x = int((longitude + 180) * 100 / 360)
    y = int((-latitude + 90) * 100 / 180)

    # Запись значения скорости ветра в соответствующую ячейку матрицы
    heatmap_data[y, x] = speed

# Создание тепловой карты на основе матрицы данных и добавление ее на карту
heatmap = HeatMap(heatmap_data).add_to(m)

# Сохранение карты в файл
m.save("heatmap.html")