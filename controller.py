from view import View
from modules import Database


class Controller:

    @staticmethod
    def run_get_record_from_database(obj):
        """
        This function allows users get record from database by full name
        """
        print("-"*80)
        View.print_input_first_name()
        f_name = input()
        View.print_input_last_name()
        l_name = input()
        flag = obj.print_one_record(f_name, l_name)
        if flag == -1:
            View.print_if_record_absent()
        print("-"*80)

    @staticmethod
    def run_show_all_database(obj):
        """
        This function shows all database
        """
        print("-"*80)
        flag = obj.print_all_database()
        if flag == -1:
            View.print_if_database_empty()
        print("-"*80)

    @staticmethod
    def run_add_record_to_database(obj):
        """
        This function allows users add record to database
        """
        View.print_input_first_name()
        f_name = input()
        View.print_input_last_name()
        l_name = input()
        View.print_input_phone_number()
        phone_number = input()
        flag = obj.add_record(f_name, l_name, phone_number)
        if flag == 1:
            View.print_add_message()
        else:
            View.print_if_record_exist()

    @staticmethod
    def run_delete_record_from_database(obj):
        """
        This function allows users delete record to database
        """
        View.print_input_first_name()
        f_name = input()
        View.print_input_last_name()
        l_name = input()
        index = obj.check_record_in_database(f_name, l_name)
        if index != -1:
            View.print_confirm_question()
            confirm = input()
            if confirm.lower() == 'y':
                obj.delete_record(index)
                View.print_delete_message()
        else:
            View.print_if_record_absent()

    def menu(self):
        """
        This function realizes possibility work with database from console
        """
        ch = ''
        phone_book = Database("base")

        while ch != '5':
            print()
            View.print_menu()
            ch = input()
            if ch == '1':
                self.run_show_all_database(phone_book)
            elif ch == '2':
                self.run_get_record_from_database(phone_book)
            elif ch == '3':
                self.run_add_record_to_database(phone_book)
            elif ch == '4':
                self.run_delete_record_from_database(phone_book)
            elif ch == '5':
                break
            else:
                continue

        phone_book.save("base")
        View.print_program_completed()
