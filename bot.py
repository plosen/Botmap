from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from logic import create_graph

# Инициализация бота
API_TOKEN = 'ваш_токен'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# База данных городов
CITIES = [
    {"name": "Prague", "lat": 50.0755, "lon": 14.4378},
    {"name": "Berlin", "lat": 52.5200, "lon": 13.4050},
    {"name": "Moscow", "lat": 55.7558, "lon": 37.6173},
]

# Команда для отображения всех городов
@dp.message_handler(commands=['show_all_cities'])
async def show_all_cities(message: types.Message):
    create_graph(CITIES)
    await message.reply("Карта всех городов создана! Посмотрите окно вывода.")

# Команда для отображения информации о конкретном городе
@dp.message_handler(commands=['show_city'])
async def show_city(message: types.Message):
    city_name = message.get_args()
    city = next((c for c in CITIES if c['name'].lower() == city_name.lower()), None)

    if city:
        await message.reply(f"Город: {city['name']}\nШирота: {city['lat']}\nДолгота: {city['lon']}")
    else:
        await message.reply("Город не найден. Убедитесь, что название введено правильно.")

# Команда для помощи
@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply("/show_all_cities - показать карту всех городов\n/show_city <город> - показать информацию о городе")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
