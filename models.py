from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Consumo(Base):
    __tablename__ = "consumo"

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    kwh = Column(Float, nullable=False)
    custo = Column(Float, nullable=False)
    observacao = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    dono = relationship("User", back_populates="consumos")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String)
    meta = Column(Float, default=150)

    consumos = relationship("Consumo", back_populates="dono")