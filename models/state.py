#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type, storage
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            """
            curr_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    curr_cities.append(city)
            return curr_cities
