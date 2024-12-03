from quiz_api.database import Base, engine

print("Import models:")
print(Base.metadata.tables.keys())

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Tables are created!")
from sqlalchemy import inspect

inspector = inspect(engine)
tables = inspector.get_table_names()
print(f"Existing tables: {tables}")
