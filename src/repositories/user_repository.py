from sqlalchemy.orm import Session
from src.db.models import User


class UserRepository:
    @staticmethod
    def get_by_telegram_id(db: Session, telegram_id: int) -> User | None:
        """
        Получить пользователя по Telegram Chat ID
        
        :param db: Сессия в БД
        :param telegram_id: Telegram Chat ID пользователя
        """
        return db.query(User).filter(User.telegram_id == telegram_id).first()

    @staticmethod
    def create(
        db: Session,
        telegram_id: int,
        username: str | None,
        first_name: str | None,
        last_name: str | None,
        language: str | None
    ) -> User:
        """
        Добавляет пользователя в таблицу `users`
        
        :param db: Сессия в БД
        :param telegram_id: Telegram Chat ID
        :param first_name: Имя пользователя
        :param last_name: Фамилия пользователя
        :param language: Язык пользователя
        """
        user = User(
            telegram_id=telegram_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            language=language
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
