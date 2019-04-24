#!/usr/bin/python3
"""This is the file db_storage class for AirBnB"""

import os
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """describes DBStorage class"""
    __engine = None
    __session = None
    __all_classes = {State, City, Amenity, Place, Review, User}

    def __init__(self):
        """happens when a new instance of DBStorage is created"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(user, pwd, host, db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all
        objects depending of the class name (argument cls)"""
        if type(cls) is str:
            cls = eval(cls)
        dict_all = {}
        if cls is None:
            for table in self.__all_classes:
                type_obj = self.__session.query(table)
                for one_obj in type_obj:
                    cls_name = one_obj.__class__.__name__
                    k = cls_name + '.' + one_obj.id
                    dict_all[k] = one_obj
        else:
            all_rows = self.__session.query(cls).all()
            for obj in all_rows:
                k = obj.__class__.__name__ + '.' + obj.id
                dict_all[k] = obj
        return dict_all

    def reload(self):
        """creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        reloaded_sesh = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(reloaded_sesh)

    def new(self, obj):
        """adds an object to the current datatabase session
        """
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """close self.__session Session object"""
        self.__session.remove()
