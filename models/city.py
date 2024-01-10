#!/usr/bin/python3
"""City Model"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City, inherits from BaseModel."""

    name: str = ""
    state_id: str = ""

    def __init__(self, **kwargs):
        """Initialize a new City instance with given values."""
        super().__init__(**kwargs)
