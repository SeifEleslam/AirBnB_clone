#!/usr/bin/python3
"""Amenity Model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing a Amenity, inherits from BaseModel."""

    name: str = ""
