from quiz_api.database import Base, engine

print("Import models:")
print(Base.metadata.tables.keys())

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("Tables are created!")
