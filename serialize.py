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
    def save(filePath, table):
        """
        Choose file to save data
        """
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        cls = config.get('SerializationSettings', 'serialize')
        _serializer = sys.modules["serialize"].__dict__.get(cls)
        return _serializer.save(filePath, table)

    @staticmethod
    def load(filePath):
        """
        Choose file to load data
        """
        config = configparser.RawConfigParser()
        config.read('config.cfg')
        cls = config.get('SerializationSettings', 'serialize')
        _serializer = sys.modules["serialize"].__dict__.get(cls)
        return _serializer.load(filePath)


class JsonSerialize:
    """
    Serialize database to json file
    """
    @staticmethod
    def load(fileName):
        """
        load data from file :filePath and return as list. If file doesn't
        exist, return empty list
        """
        if not os.path.isfile("./databases/" + fileName + ".json"):
            return []
        with open("./databases/" + fileName + ".json", "r") as f:
            data = json.load(f)
            return data

    @staticmethod
    def save(fileName, data):
        """
            serialize to file :filePath list :data
        """
        with open("./databases/" + fileName + ".json", "w") as f:
            json.dump(data, f)
            f.close()


class PickleSerialize:
    """
    Serialize database to pickle file
    """
    @staticmethod
    def save(fileName, data):
        """
        serialize to file :filePath list :data
        """
        with open("./databases/" + fileName + ".pickle", "wb") as f:
            pickle.dump(data, f)
            f.close()

    @staticmethod
    def load(fileName):
        """
        load data from file :filePath and return as list. If file doesn't
        exist, return empty list
        """
        if not os.path.isfile("./databases/" + fileName + ".pickle"):
            return []
        with open("./databases/" + fileName + ".pickle", "rb") as f:
            res = pickle.load(f)
            return res


class YamlSerialize:
    """
    Serialize database to yaml file
    """
    @staticmethod
    def save(fileName, data):
        """
        serialize to file :filePath list :data
        """
        with open("./databases/" + fileName + ".yaml", "w") as f:
            yaml.dump(data, f)

    @staticmethod
    def load(fileName):
        """
        load data from file :filePath and return as list. If file doesn't
        exist, return empty list
        """
        if not os.path.isfile("./databases/" + fileName + ".yaml"):
            return []
        with open("./databases/" + fileName + ".yaml", "r") as f:
            res = yaml.load(f)
            return res
