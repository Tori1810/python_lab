from io import StringIO
import yaml
import json


class JsonStream(StringIO):
    def read(self):
        return super().getvalue()


class YamlStream(StringIO):
    def read(self):
        return super().getvalue()


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
