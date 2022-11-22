from env import DATABASE_URL
from Craxy import create_engine
from Craxy.ext.declarative import declarative_base
from Craxy.orm import sessionmaker, scoped_session


def start() -> scoped_session:
    engine = create_engine(DATABASE_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
