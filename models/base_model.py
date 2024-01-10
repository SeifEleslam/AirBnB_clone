#!/usr/bin/python3
"""Base Model"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    This is the base model class from which all other classes inherit.
    It provides common methods
    """
    id = None
    created_at = None
    updated_at = None

    def __init__(self, *args, **kwargs) -> None:
        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    self.__setattr__(key, datetime.fromisoformat(
                        kwargs[key]) if (
                            key == "created_at" or key == "updated_at"
                    ) else kwargs[key])
            return
        time_now = datetime.now()
        self.created_at = time_now
        self.updated_at = time_now
        self.id = str(uuid.uuid4())
        storage.new(self.to_dict())

    def __str__(self) -> str:
        """Return the string representation of class"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self) -> None:
        """Update the updated_at time with the current time"""
        self.updated_at = datetime.now()
        storage.new(self.to_dict())
        storage.save()

    def delete(self):
        """Remove instance from storage"""
        storage.delete(f"{self.__class__.__name__}.{self.id}")
        storage.save()

    def to_dict(self):
        """Convert object values to dictionary"""
        repr_dict = dict(self.__dict__)
        repr_dict["__class__"] = self.__class__.__name__
        repr_dict["created_at"] = repr_dict["created_at"].isoformat()
        repr_dict["updated_at"] = repr_dict["updated_at"].isoformat()
        return repr_dict
