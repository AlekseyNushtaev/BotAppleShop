from dotenv import load_dotenv
import os
from typing import Optional

# Загрузка переменных окружения из .env файла
load_dotenv()

# Токен бота Telegram
TG_TOKEN: Optional[str] = os.environ.get("TG_TOKEN")
