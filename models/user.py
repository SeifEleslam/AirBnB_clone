#!/usr/bin/python3
"""User Model"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a user, inherits from BaseModel."""

    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
