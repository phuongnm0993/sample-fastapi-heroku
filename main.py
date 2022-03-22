from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/sacom_bots/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/sacom_bots/{bot_id}", response_model=schemas.SacomBot)
def get_sacom_bot_by_id(bot_id: int, db: Session = Depends(get_db)):
    db_sacom_bot = crud.get_sacom_bot_by_id(db, bot_id=bot_id)
    if db_sacom_bot is None:
        raise HTTPException(status_code=404, detail="Sacom bot not found")
    return db_sacom_bot


@app.post("/sacom_bots/_default/activate", response_model=schemas.Item)
def activate_sacom_bot_by_id(db: Session = Depends(get_db)):
    return crud.activate_sacom_bot_by_id(db=db, bot_id=1)


@app.post("/sacom_bots/_default/deactivate", response_model=schemas.Item)
def deactivate_sacom_bot_by_id(db: Session = Depends(get_db)):
    return crud.deactivate_sacom_bot_by_id(db=db, bot_id=1)