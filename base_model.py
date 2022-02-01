#!/usr/bin/python3
"""Basemodel class"""

import models
import uuid
from datetime import datetime


class BaseModel:
    """ base model"""
    def __init__(self, *args, **kwargs):
        """initializing BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """update datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Changes class instance to dictionary"""
        dict_ = self.__dict__.copy()
        dict_["__class__"] = self.__class__.__name__
        dict_["updated_at"] = self.updated_at.isoformat()
        dict_["created_at"] = self.created_at.isoformat()
        return dict_

    def __str__(self):
        """return [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
