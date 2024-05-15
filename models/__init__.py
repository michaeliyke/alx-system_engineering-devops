#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()  # We use the database here
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()  # We use file storage here

storage.reload()

