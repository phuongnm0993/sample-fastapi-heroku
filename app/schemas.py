from pydantic import BaseModel


class SacomBotBase(BaseModel):
    title: str
    is_active: bool


class SacomBotCreate(SacomBotBase):
    pass


class SacomBot(SacomBotBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True