#!/usr/bin/python3
from datetime import datetime
import uuid
from .engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
