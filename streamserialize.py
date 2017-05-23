from io import StringIO
import yaml
import pickle
import json


class JsonStream(StringIO):
    def read(self):
        return super().getvalue()


class YamlStream(StringIO):
    def read(self):
        return super().getvalue()


class PickleStream(StringIO):
    def read(self):
        return super().getvalue()


def pickle_to_stream(data):
    """
    Convert data to pickle stream
    """
    pickle_stream = PickleStream()
    pickle.dump(data, pickle_stream)
    return pickle_stream


def json_to_stream(data):
    """
    Convert data to json stream
    """
    json_stream = JsonStream()
    json.dump(data, json_stream)
    return json_stream


def yaml_to_stream(data):
    """
    Convert data to yaml stream
    """
    yaml_stream = YamlStream()
    yaml.dump(data, yaml_stream, Dumper=yaml.Dumper)
    return yaml_stream
