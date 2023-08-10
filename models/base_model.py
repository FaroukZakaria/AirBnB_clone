#!/usr/bin/python3
import uuid
from datetime import datetime
"""Creating a super class which subclasses would inherit from"""


class BaseModel():
    """The initialization of Model attributes"""
    def __init__(self, *args, **kwargs):
        """Definitions"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)

            if 'created_at' in kwargs:
                self.created_at = kwargs['created_at'].isoformat()

            if 'updated_at' in kwargs:
                self.updated_at = kwargs['updated_at'].isoformat()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Update modification date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of Class
            with keyworded items and includes class name"""
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                self.__dict__[key] = value.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)
