import json
import pickle
import configparser
import sys
import os
import yaml


class Serialize:
    """
    Choose file to serialize
    """

    @staticmethod
    def save(file_path, table):
        """
        Choose file to save data
        """
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        cls = config.get('SerializationSettings', 'serialize')
        _serializer = sys.modules["serialize"].__dict__.get(cls)
        return _serializer.save(file_path, table)

    @staticmethod
    def load(file_path):
        """
        Choose file to load data
        """
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        cls = config.get('SerializationSettings', 'serialize')
        _serializer = sys.modules["serialize"].__dict__.get(cls)
        return _serializer.load(file_path)


class JsonSerialize:
    """
    Serialize database to json file
    """
    @staticmethod
    def load(file_name):
        """
        load data from file :filePath and return as list. If file doesn't
        exist, return empty list
        """
        if not os.path.isfile("./databases/" + file_name + ".json"):
            return []
        with open("./databases/" + file_name + ".json", "r") as f:
            data = json.load(f)
            return data

    @staticmethod
    def save(file_name, data):
        """
        serialize to file :filePath list :data
        """
        with open("./databases/" + file_name + ".json", "w") as f:
            json.dump(data, f)
            f.close()


class PickleSerialize:
    """
    Serialize database to pickle file
    """
    @staticmethod
    def save(file_name, data):
        """
        serialize to file :filePath list :data
        """
        with open("./databases/" + file_name + ".pickle", "wb") as f:
            pickle.dump(data, f)
            f.close()

    @staticmethod
    def load(file_name):
        """
        load data from file :filePath and return as list. If file doesn't
        exist, return empty list
        """
        if not os.path.isfile("./databases/" + file_name + ".pickle"):
            return []
        with open("./databases/" + file_name + ".pickle", "rb") as f:
            res = pickle.load(f)
            return res


class YamlSerialize:
    """
    Serialize database to yaml file
    """
    @staticmethod
    def save(file_name, data):
        """
        serialize to file :filePath list :data
        """
        with open("./databases/" + file_name + ".yaml", "w") as f:
            yaml.dump(data, f)

    @staticmethod
    def load(file_name):
        """
        load data from file :filePath and return as list. If file doesn't
        exist, return empty list
        """
        if not os.path.isfile("./databases/" + file_name + ".yaml"):
            return []
        with open("./databases/" + file_name + ".yaml", "r") as f:
            res = yaml.load(f)
            return res
