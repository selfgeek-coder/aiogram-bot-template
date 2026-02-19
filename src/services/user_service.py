from sqlalchemy.orm import Session
from src.repositories.user_repository import UserRepository


class UserService:
    @staticmethod
    def get_or_create_user(
        db: Session,
        telegram_id: int,
        username: str | None,
        first_name: str | None,
        last_name: str | None,
        language: str | None
    ):
        """
        Создает или получает пользователя из таблицы `users`
        
        :param db: Сессия в БД
        :param telegram_id: Telegram Chat ID
        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param language: Язык пользователя
        """
        
        user = UserRepository.get_by_telegram_id(db, telegram_id)

        if user:
            return user

        return UserRepository.create(
            db=db,
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language=language
        )