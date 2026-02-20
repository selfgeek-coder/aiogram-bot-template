from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from src.db.database import SessionLocal
from src.services.user_service import UserService


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    with SessionLocal() as db:
        user = UserService.get_or_create_user(
            db=db,
            telegram_id=message.from_user.id,
            username=message.from_user.username,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            language=message.from_user.language_code
        )
        

    await message.answer(
        f"Привет, <b>{message.from_user.first_name}</b>!\n"
    )
    