import unittest
import json
import yaml
import pickle
from modules import Database
import streamserialize
from serialize import YamlSerialize, JsonSerialize, PickleSerialize, Serialize


class TestSerialize(unittest.TestCase):

    def test_save(self):
        self.assertEqual(Serialize.save("", []), None)

    def test_load(self):
        self.assertEqual(Serialize.load("test"), [{"first_name": "a",
                                                  "last_name": "b",
                                                   "phone_number": "123"}])


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
        self.assertEqual([], JsonSerialize.load(""))


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
        self.assertEqual([], YamlSerialize.load(""))


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
        self.assertEqual([], PickleSerialize.load("lala"))


class TestModule(unittest.TestCase):

    test_base = Database("test")

    def test_len(self):
        self.assertEqual(self.test_base.__len__(), len(self.test_base.base))

    def test_save(self):
        self.assertEqual(self.test_base.save("test"), None)

    def test_check_record(self):
        self.test_base.base = [{"first_name": "a", "last_name": "b",
                                "phone_number": "23"}]
        self.assertEqual(self.test_base.check_record_in_database("a", "b"), 0)
        self.test_base.base = []
        self.assertEqual(self.test_base.check_record_in_database("a", "b"), -1)

    def test_print_record(self):
        self.test_base.base = [{"first_name": "a", "last_name": "b",
                                "phone_number": "123"}]
        self.assertEqual(self.test_base.print_one_record("c", "d"), -1)
        self.assertEqual(self.test_base.print_one_record("a", "b"), 1)

    def test_add_record(self):
        self.test_base.base = [{"first_name": "a", "last_name": "b",
                                "phone_number": "123"}]
        self.assertEqual(self.test_base.add_record("a", "b", "123"), -1)
        self.assertEqual(self.test_base.add_record("c", "d", "567"), 1)

    def test_delete_record(self):
        self.test_base.base = [{"first_name": "a", "last_name": "b",
                                "phone_number": "123"}]
        self.assertEqual(self.test_base.delete_record(0), [])

    def test_print_all_base(self):
        self.test_base.base = [{"first_name": "a", "last_name": "b",
                                "phone_number": "123"}]
        self.assertEqual(self.test_base.print_all_database(), 1)
        self.test_base.base = []
        self.assertEqual(self.test_base.print_all_database(), -1)
