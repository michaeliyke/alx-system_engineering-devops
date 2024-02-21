"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine, MetaData
import sqlalchemy.orm as orm
import os


class DBStorage:
    """This class manages storage of hbnb models using a DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Returns a sqlachemy orm object of models currently the storage"""
        from models.base_model import Base

        USER = os.getenv("HBNB_MYSQL_USER")
        PWD = os.getenv("HBNB_MYSQL_PWD")
        HOST = os.getenv("HBNB_MYSQL_HOST")
        DB = os.getenv("HBNB_MYSQL_DB")
        ENV = os.getenv("HBNB_ENV")
        conn_str = "mysql+mysqldb://{}:{}@{}/{}".format(USER, PWD, HOST, DB)
        self.__engine = create_engine(conn_str, pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)

        if ENV == "test":
            metadata = MetaData()  # Meta data object
            metadata.reflect(self.__engine)  # Analyze db relationships
            # Drop all tables in their dependencies order
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieve all objects depending of the class name"""
        from models.city import City
        from models.state import State

        if cls:
            return self.__session.query(cls)
        # User, State, City, Amenity, Place and Review
        return [self.__session.query(x) for x in [City, State]]

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        # self.__session.add(self)
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """create all tables in the database"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from models.base_model import Base

        # for model in [BaseModel, User, Place, State, City, Amenity, Review]:
        # self.new(model)

        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        factory = orm.sessionmaker(bind=self.__engine)
        Session = orm.scoped_session(factory)
        self.__session = Session(bind=self.__engine, expire_on_commit=False)
