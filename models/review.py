#!/usr/bin/python3
"""Review Model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review, inherits from BaseModel."""

    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, **kwargs):
        """Initialize a new Review instance with given values."""
        super().__init__(**kwargs)
