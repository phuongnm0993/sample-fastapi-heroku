from sqlalchemy.orm import Session

from . import models, schemas


def get_sacom_bot_by_id(db: Session, bot_id: int):
    return db.query(models.SacomBot).filter(models.SacomBot.id == bot_id).first()

def activate_sacom_bot_by_id(db: Session, bot_id: int):
    db_sacom_bot = db.query(models.SacomBot).filter(models.SacomBot.id == bot_id).first()
    db_sacom_bot.is_active = True
    db.commit()
    db.refresh(db_sacom_bot)
    return db_sacom_bot

def deactivate_sacom_bot_by_id(db: Session, bot_id: int):
    db_sacom_bot = db.query(models.SacomBot).filter(models.SacomBot.id == bot_id).first()
    db_sacom_bot.is_active = False
    db.commit()
    db.refresh(db_sacom_bot)
    return db_sacom_bot
