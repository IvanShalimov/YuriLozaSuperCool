from aiogram import Router, types, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.filters import CommandStart
import aiofiles
import random
import json
from aiogram.utils import markdown

from keyboards.common_keyboards import get_on_start_keyboard
MAIN_COMMAND = "new_fact"

router = Router()

@router.message(CommandStart())
async def handel_start(message: types.Message):
    await message.answer(
        text="Приветствую тебя, искатель мудрости Юрия Эдуардовича!",
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_keyboard()
    )

@router.message(F.text == "ℹ️ Познать мудрость Лозы!")
@router.message(Command("new_fact", prefix="!/"))
async def new_fact(message: types.Message):
    try:
        async with aiofiles.open('loza.json', mode='r', encoding='utf-8') as f:
            random_index = random.randint(0, 14)
            contents = await f.read()
            data = json.loads(contents)

            text = data['facts'][random_index]['text']
            print(text)

            await message.answer(
                text=text,
                parse_mode=ParseMode.HTML,
                reply_markup=get_on_start_keyboard()
            )

    except FileNotFoundError:
        print("Error: 'config.json' not found.")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

@router.message()
async def echo_message(message: types.Message):
    url = "https://tvcenter.ru/wp-content/uploads/2020/10/pic_959307cab95fc2d80cd86471397a4116.jpg"

    await message.answer(
        text=markdown.hbold("Лоза (в) ярости!")+markdown.hide_link(url),
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_keyboard()
    )