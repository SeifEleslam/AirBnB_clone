#!/usr/bin/python3
"""State Model"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class representing a State, inherits from BaseModel."""

    name: str = ""

    def __init__(self, **kwargs):
        """Initialize a new State instance with given values."""
        super().__init__(**kwargs)
