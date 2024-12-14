import matplotlib.pyplot as plt


def create_graph(cities):
    """
    Создает граф (карту) городов по их координатам.

    :param cities: список словарей с информацией о городах (name, lat, lon)
    """
    if not cities:
        return "Нет данных для отображения карты."

    # Разделение данных на координаты и названия
    latitudes = [city['lat'] for city in cities]
    longitudes = [city['lon'] for city in cities]
    names = [city['name'] for city in cities]

    # Создание карты
    plt.figure(figsize=(10, 6))
    plt.scatter(longitudes, latitudes, c='blue', alpha=0.7, s=50)

    # Добавление названий городов
    for name, x, y in zip(names, longitudes, latitudes):
        plt.text(x, y, name, fontsize=8, ha='right')

    plt.title("Карта городов")
    plt.xlabel("Долгота")
    plt.ylabel("Широта")
    plt.grid(True)
    plt.show()
