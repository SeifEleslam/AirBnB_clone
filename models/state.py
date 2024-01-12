#!/usr/bin/python3
"""State Model"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class representing a State, inherits from BaseModel."""

    name: str = ""
