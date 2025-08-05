# backend/app/db/init_db.py

from app.db.session import engine
from app.db.base import Base
from app.models import user_model  # Import to register the model

def init_db():
    Base.metadata.create_all(bind=engine) 