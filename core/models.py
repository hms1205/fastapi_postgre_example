from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Float
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)
    disabled = Column(Boolean, index=True, default=False)
    sensors = relationship("Sensor", back_populates="owner")


class Sensor(Base):
    __tablename__ = "sensors"

    id = Column(Integer, primary_key=True, index=True)
    administer_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="sensors")
    degrees = relationship("Degree", back_populates="sensor")


class Degree(Base):
    __tablename__ = "degrees"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(TIMESTAMP, index=True)
    degree = Column(Float, index=True)
    sensor_id = Column(Integer, ForeignKey("sensors.id"))
    sensor = relationship("Sensor", back_populates="degrees")
