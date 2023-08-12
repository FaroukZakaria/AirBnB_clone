#!/usr/bin/python3
import json
import os


class FileStorage:
    def __init__(self, path):
        self.__file_path = path
        self.__objects = {}

    def all(self):
        return(self.__objects)

    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        ser = {}
        for key, obj in self.__objects.items():
            ser[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(ser, f, indent=4)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                ser = json.load(f)
                self.__objects = ser
