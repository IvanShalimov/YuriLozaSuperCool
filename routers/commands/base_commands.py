from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
import aiofiles
import random
import json

router = Router()


@router.message(Command("new_fact", prefix="!/"))
async def new_fact(message: types.Message):
    try:
#        if not os.path.exists(".loza.json"):
#           await message.answer(f"Файл {".loza.json"} не найден. Текущая директория: {os.getcwd()}")
#           print(f"Файлы в текущей директории: {os.listdir('.')}")
        async with aiofiles.open('loza.json', mode='r', encoding='utf-8') as f:
            random_index = random.randint(1, 15)
            contents = await f.read()
            data = json.loads(contents)

            await message.answer(
                text=data['facts'][random_index]['text'],
                parse_mode=ParseMode.HTML,
                # reply_markup=get_on_help_keyboard()
            )

    except FileNotFoundError:
        print("Error: 'config.json' not found.")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
