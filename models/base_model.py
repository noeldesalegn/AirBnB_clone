#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes:"""
import uuid
from datetime import datetime


class BaseModel:
    """Simple Base Model class"""
    def __init__(self, *args, **kwargs):
        """initialize imprtant instance attribute"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Update the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Returns the dict format of an object"""
        kvdict = self.__dict__
        kvdict["__class__"] = type(self).__name__
        kvdict["updated_at"] = self.updated_at.isoformat()
        kvdict["created_at"] = self.created_at.isoformat()
        return kvdict

    def __str__(self):
        """Returns information about the class in human readable format"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
