from __future__ import print_function


def check_record_in_database(first_name, last_name, database):
    """
    This function checks if record in exist in database
    :returns: -1 if record not exist or this record index if it exist
    """
    index = 0
    for rec in database:
        if rec["first_name"] == first_name and rec["last_name"] == last_name:
            return index
        index += 1
    return -1


def print_one_record(first_name, last_name, database):
    """
    This function print one record from database
    returns: -1 if record cannot be printed or 1 if it possible
    :param index: number record in database
    """
    index = check_record_in_database(first_name, last_name, database)
    if index != -1:
        rec = database[index]
        print("%4d. " % (index+1), "%10s " % rec["first_name"], end=' ')
        print("%15s: " % rec["last_name"], "%20s " % rec["phone_number"])
        return 1
    else:
        return -1


def print_all_database(database):
    """
    This function print full database
    returns: -1 if database is empty or 1 when all database printed
    """
    len_database = len(database)
    if len_database == 0:
        return -1

    for index in range(0, len_database):
        rec = database[index]
        print("%4d. " % (index + 1), "%10s " % rec["first_name"], end=' ')
        print("%15s: " % rec["last_name"], "%20s " % rec["phone_number"])
    return 1


def add_record(first_name, last_name, phone_number, database):
    """
    This function add record to database
    returns: 1 if record added or -1 if not
    """
    index = check_record_in_database(first_name, last_name, database)
    if index == -1:
        new_rec = {}
        new_rec["first_name"] = first_name
        new_rec["last_name"] = last_name
        new_rec["phone_number"] = phone_number
        database.append(new_rec)
        return 1
    return -1


def delete_record(index, database):
    """
    This function delete one record from database
    returns: changed database
    :param index: number record in database
    """
    rec = database[index]
    database.remove(rec)
    return database
