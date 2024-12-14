import matplotlib.pyplot as plt
import geopandas as gpd


def create_graph(cities, marker_color='blue', ocean_color='lightblue', continent_color='lightgreen', show_borders=True):
    """
    Создает граф (карту) городов с возможностью заливки континентов и океанов и отображения географических объектов.

    :param cities: список словарей с информацией о городах (name, lat, lon)
    :param marker_color: цвет маркеров (по умолчанию 'blue')
    :param ocean_color: цвет океанов (по умолчанию 'lightblue')
    :param continent_color: цвет континентов (по умолчанию 'lightgreen')
    :param show_borders: если True, отображаются границы стран и континентов
    """
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    fig, ax = plt.subplots(figsize=(12, 8))

    world.plot(ax=ax, color=continent_color, edgecolor='black')  # Заливка континентов
    ax.set_facecolor(ocean_color)  # Заливка океанов

    if show_borders:
        world.boundary.plot(ax=ax, color="black", linewidth=1)  # Отображение границ стран и континентов

    latitudes = [city['lat'] for city in cities]
    longitudes = [city['lon'] for city in cities]
    names = [city['name'] for city in cities]

    ax.scatter(longitudes, latitudes, c=marker_color, alpha=0.7, s=100, edgecolors='black', linewidth=1.5)

    for name, x, y in zip(names, longitudes, latitudes):
        ax.text(x, y, name, fontsize=10, ha='right', color='black')

    plt.title("Карта городов с географическими объектами")
    plt.xlabel("Долгота")
    plt.ylabel("Широта")
    plt.grid(True)
    plt.show()
