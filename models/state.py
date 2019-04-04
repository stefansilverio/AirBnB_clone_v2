#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship(
            "City", backref='state', cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """ gets a list of city objects with that state id """
        all_obj = models.storage.all()
        cities_list = []
        for k, v in all_obj.items():
            if v.__class__.__name__ == 'City' and v.state_id == self.id:
                cities_list.append(v)
        return cities_list
