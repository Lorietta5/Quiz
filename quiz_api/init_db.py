# init_db.py


from quiz_api.database import Base, engine

Base.metadata.drop_all(bind=engine)

Base.metadata.create_all(bind=engine)

print("Tables are created!")
