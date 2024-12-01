from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./quiz1.db"  # Або ваш шлях до бази даних

# Створення двигуна для підключення до бази даних
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # Для SQLite з багатопотоковістю

# Створення сесії
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Основний клас для декларативних моделей
from sqlalchemy.orm import declarative_base

# Функція для отримання сесії
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
