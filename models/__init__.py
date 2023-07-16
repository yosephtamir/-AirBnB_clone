#!/usr/bin/python3
"""
This module is used to initialize the model
"""


from models.engine import file_storage
storage = file_storage.FileStorage()
storage.reload()
