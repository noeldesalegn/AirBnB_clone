#!/usr/bin/python3
from uuid import uuid4
import datetime
import models
"""
command interpreter to manage your AirBnB objects clone version
"""


class BaseModel:
    """ This  defines all common attributes/methods for other classes
    """
    st = "%Y-%m-%dT%H:%M:%S.%f"
    t = datetime.datetime

    def __init__(self, *args, **kwargs):
        """ Public instance attributes:
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = t.strptime(kwargs["created_at"], st)
                elif "updated_at" == key:
                    self.updated_at = t.strptime(kwargs["updated_at"], st)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = datetime.datetime.today()
            models.storage.new(self)

    def __str__(self):
        """ this magic fuction print valuse in a nice way  """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute updated_at
        with the current datetime
        """
        return("{}".format(self.created_at))

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        keys = {}
        keys["__class__"] = self.__class__.__name__
        for i, val in self.__dict__.items():
            if isinstance(val, (datetime.datetime, )):
                keys[i] = val.isoformat()
            else:
                keys[i] = val
        return keys
