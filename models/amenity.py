#!/usr/bin/python3
"""Amenity Model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing a Amenity, inherits from BaseModel."""

    name: str = ""

    def __init__(self, **kwargs):
        """Initialize a new Amenity instance with given values."""
        super().__init__(**kwargs)
