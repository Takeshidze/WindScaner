import numpy as np
import matplotlib.pyplot as plt

def show_graph(data):
    coords = [d['coord'] for d in data['data']]
    winds = [d['wind_speed_10m'] for d in data['data']]
    wind_degrees = [d['wind_direction_10m'] for d in data['data']]
    gusts = [d['wind_gusts_10m'] for d in data['data']]

    # Построение графиков
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    # График скорости ветра и порывов
    distance = np.arange(0, len(coords) * 100, 100)  # создаем массив расстояний
    ax1.plot(distance, winds, label='Скорость ветра')
    ax1.plot(distance, gusts, label='Порывы ветра')
    ax1.set_xlabel('Расстояние, м')
    ax1.set_ylabel('Скорость ветра, Порывы, м/c')
    ax1.set_title('Скорость и порывы ветра')
    ax1.legend()

    # График направления ветра
    ax2.plot(distance, wind_degrees, label='Направление ветра')
    ax2.set_xlabel('Расстояние, м')
    ax2.set_ylabel('Направление ветра, градусы')
    ax2.set_title('Направление ветра')
    ax2.legend()

    # Добавление заголовка к всему изображению
    str = f'Общее расстояние {int(data["distance"])} м, Начальная координата {data["start_coord"]}, Конечная координата {data["end_coord"]}'
    fig.suptitle(str)

    plt.show()