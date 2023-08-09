#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel():
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")
    def save(self):
        self.updated_at = datetime.now()
    def to_dict(self):
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                self.__dict__[key] = value.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)
