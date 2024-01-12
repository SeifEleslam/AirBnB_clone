#!/usr/bin/python3
"""Review Model"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a Review, inherits from BaseModel."""

    place_id: str = ""
    user_id: str = ""
    text: str = ""
