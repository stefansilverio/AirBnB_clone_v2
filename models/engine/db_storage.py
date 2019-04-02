#!/usr/bin/python3
"""DBStorage class"""


from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """describes DBStorage class"""
    __engine = None
    __session = None
    __all_classes = {"Amenity", "City", "Place", "Review", "State", "User"}

    def __init__(self):
        """happens when a new instance of DBStorage is created"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects depending of the class name (argument cls)"""
        dict_all = {}
        if cls is None:
            all_rows = self.__session.query(Amenity, City, Place, Review, State, User).all()
            for obj in all_rows:
                cls_name =  obj.__class__.__name__
                k = obj.__class__.__name__ + '.' + obj.id
                dict_all[k] = obj
        else:
            cls_name = cls.__name__
            if cls_name in self.__all_classes:
                all_rows = self.__session.query(cls_name).all()
                for obj in all_rows:
                    k = cls_name + '.' + obj.id
                    dict_all[k] = obj
        return dict_all

    def reload(self):
        """creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        reloaded_sesh = sessionmaker(bind=self.__engine, expire_on_commit=False)
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