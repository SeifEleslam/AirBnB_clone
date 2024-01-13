#!/usr/bin/python3
"""User Model"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """Class representing a user, inherits from BaseModel."""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
