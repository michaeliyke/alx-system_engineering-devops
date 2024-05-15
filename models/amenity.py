#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import sqlalchemy.orm as orm


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    name = Column(String(129), nullable=False)
    place_amenities = orm.relationship("Place", )

