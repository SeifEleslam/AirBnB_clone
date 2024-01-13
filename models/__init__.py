#!/usr/bin/python3
"""Models Init"""

from models.engine.file_storage import FileStorage
from models.operations import Operations

ops = Operations()
storage = FileStorage()
storage.reload()
