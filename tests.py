import unittest
import json
import yaml
import pickle
import Modules
import streamserialize
from serialize import YamlSerialize, JsonSerialize, PickleSerialize


class TestJsonSerialize(unittest.TestCase):

    def test_save_json(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        JsonSerialize.save("test", base)
        stream = streamserialize.json_to_stream(base)
        f = open('./databases/test.json', "r")
        self.assertEqual(json.load(stream), json.load(f))
        f.close()

    def test_load_json(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        f = open('./databases/test.json', "w")
        json.dump(base, f)
        f.close()
        stream = streamserialize.json_to_stream(base)
        self.assertEqual(json.load(stream), JsonSerialize.load("test"))


class TestYamlSerialize(unittest.TestCase):

    def test_save_yaml(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        YamlSerialize.save("test", base)
        stream = streamserialize.yaml_to_stream(base)
        f = open('./databases/test.yaml', "r")
        self.assertEqual(yaml.load(stream.read()), yaml.load(f))
        f.close()

    def test_load_yaml(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        f = open('./databases/test.yaml', "w")
        yaml.dump(base, f)
        f.close()
        stream = streamserialize.yaml_to_stream(base)
        self.assertEqual(yaml.load(stream.read()), YamlSerialize.load("test"))


class TestPickleStream(unittest.TestCase):

    def test_save_pickle(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        PickleSerialize.save("test", base)
        f = open('./databases/test.pickle', "rb")
        self.assertEqual(base, pickle.load(f))
        f.close()

    def test_load_pickle(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        f = open('./databases/test.pickle', "wb")
        pickle.dump(base, f)
        f.close()
        self.assertEqual(base, PickleSerialize.load("test"))


class TestModule(unittest.TestCase):

    def test_check_record(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "23"}]
        self.assertEqual(Modules.check_record_in_database("a", "b", base), 0)
        self.assertEqual(Modules.check_record_in_database("a", "b", []), -1)

    def test_print_record(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        self.assertEqual(Modules.print_one_record("c", "d", base), -1)
        self.assertEqual(Modules.print_one_record("a", "b", base), 1)

    def test_add_record(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        self.assertEqual(Modules.add_record("a", "b", "123", base), -1)
        self.assertEqual(Modules.add_record("c", "d", "567", base), 1)

    def test_delete_record(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        self.assertEqual(Modules.delete_record(0, base), [])

    def test_print_all_base(self):
        base = [{"first_name": "a", "last_name": "b", "phone_number": "123"}]
        self.assertEqual(Modules.print_all_database(base), 1)
        self.assertEqual(Modules.print_all_database([]), -1)
