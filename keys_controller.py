import argparse
from modules import Database
from view import View


class KeysController:
    book = Database("base")

    parser = argparse.ArgumentParser(description='Keys controller '
                                                 'for Database.')

    parser.add_argument("-show", help="show all database",
                        action='store_true')
    parser.add_argument("-find", help="find record in database",
                        action='store_true')
    parser.add_argument("-add", help="add record to database",
                        action='store_true')
    parser.add_argument("-delete", help="delete record from database",
                        action='store_true')

    def run_get_record_from_database(self):
        print("-" * 80)
        View.print_input_first_name()
        f_name = input()
        View.print_input_last_name()
        l_name = input()
        flag = self.book.print_one_record(f_name, l_name)
        if flag == -1:
            View.print_if_record_absent()
        print("-" * 80)

    def run_show_all_database(self):
        print("-" * 80)
        flag = self.book.print_all_database()
        if flag == -1:
            View.print_if_database_empty()
        print("-" * 80)

    def run_add_record_to_database(self):
        View.print_input_first_name()
        f_name = input()
        View.print_input_last_name()
        l_name = input()
        View.print_input_phone_number()
        phone_number = input()
        flag = self.book.add_record(f_name, l_name, phone_number)
        if flag == 1:
            View.print_add_message()
        else:
            View.print_if_record_exist()

    def run_delete_record_from_database(self):
        View.print_input_first_name()
        f_name = input()
        View.print_input_last_name()
        l_name = input()
        index = self.book.check_record_in_database(f_name, l_name)
        if index != -1:
            View.print_confirm_question()
            confirm = input()
            if confirm.lower() == 'y':
                self.book.delete_record(index)
                View.print_delete_message()
        else:
            View.print_if_record_absent()

    def __init__(self):
        self.args = self.parser.parse_args()
        if self.args.show:
            self.run_show_all_database()
        elif self.args.find:
            self.run_get_record_from_database()
        elif self.args.add:
            self.run_add_record_to_database()
        elif self.args.delete:
            self.run_delete_record_from_database()
        self.book.save("base")
