import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    bot_token: str = os.getenv("BOT_TOKEN")
    db_url: str = os.getenv("DATABASE_URL", "sqlite:///database.db")


config = Config()