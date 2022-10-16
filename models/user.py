#!/usr/bin/python3
"""
Defines public attributes for user class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''