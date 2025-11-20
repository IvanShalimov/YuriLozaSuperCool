from aiogram import BaseMiddleware
from aiogram.types import Message
import time

class RateLimitMiddleware(BaseMiddleware):

    def __init__(self, limit=3):
        self.limit = limit
        self.storage = {}

    async def __call__(self, handler, event: Message, data):
        user = event.from_user.id
        now = time.time()

        if user in self.storage and now - self.storage[user] < self.limit:
            await event.answer("Слишком частые запросы! Попробуйте позже.")
            return

        self.storage[user] = now
        return await handler(event, data)