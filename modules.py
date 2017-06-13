from __future__ import print_function
from iterator import Iterator
import serialize


class Database:

    def __init__(self, file_path):
        self.base = serialize.Serialize.load(file_path)

    def __iter__(self):
        return Iterator(self)

    def __len__(self):
        return len(self.base)

    def save(self, file_path):
        """
        This function write base to file
        """
        serialize.Serialize.save(file_path, self.base)

    def check_record_in_database(self, first_name, last_name):
        """
        This function checks if record in exist in database
        :returns: -1 if record not exist or this record index if it exist
        """
        index = 0
        for rec in self.base:
            if rec["first_name"] == first_name \
                    and rec["last_name"] == last_name:
                return index
            index += 1
        return -1

    def print_one_record(self, first_name, last_name):
        """
        This function print one record from database
        :returns: -1 if record cannot be printed or 1 if it possible
        """
        index = self.check_record_in_database(first_name, last_name)
        if index != -1:
            rec = self.base[index]
            print("%4d. " % (index+1), "%10s " % rec["first_name"], end=' ')
            print("%15s: " % rec["last_name"], "%20s " % rec["phone_number"])
            return 1
        else:
            return -1

    def print_all_database(self):
        """
        This function print full database
        :returns: -1 if database is empty or 1 when all database printed
        """
        len_database = len(self.base)
        if len_database == 0:
            return -1

        for index in range(0, len_database):
            rec = self.base[index]
            print("%4d. " % (index + 1), "%10s " % rec["first_name"], end=' ')
            print("%15s: " % rec["last_name"], "%20s " % rec["phone_number"])

        return 1

    def add_record(self, first_name, last_name, phone_number):
        """
        This function add record to database
        :returns: 1 if record added or -1 if not
        """
        index = self.check_record_in_database(first_name, last_name)
        if index == -1:
            new_rec = {}
            new_rec["first_name"] = first_name
            new_rec["last_name"] = last_name
            new_rec["phone_number"] = phone_number
            self.base.append(new_rec)
            return 1
        print(self.__iter__())
        return -1

    def delete_record(self, index):
        """
        This function delete one record from database
        :returns: changed database
        :param index: number record in database
        """
        rec = self.base[index]
        self.base.remove(rec)
        return self.base
