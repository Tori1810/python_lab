

class View:
    """
    It is class with functions that print different messages
    """

    @staticmethod
    def print_menu():
        print("1:. Show all phonebook")
        print("2:. Get record from phonebook by full name")
        print("3:. Add record to phonebook")
        print("4:. Delete record from phonebook")
        print("5:. Exit")

    @staticmethod
    def print_input_first_name():
        print("Please, input first name: ")

    @staticmethod
    def print_input_last_name():
        print("Please, input last name: ")

    @staticmethod
    def print_input_phone_number():
        print("Please, input phone number: ")

    @staticmethod
    def print_confirm_question():
        print("Are you sure?  y/n")

    @staticmethod
    def print_delete_message():
        print("Record removed!")

    @staticmethod
    def print_add_message():
        print("Record added!")

    @staticmethod
    def print_if_record_exist():
        print("This record already exist!")

    @staticmethod
    def print_if_record_absent():
        print("No such record!")

    @staticmethod
    def print_program_completed():
        print("____Program completed____")

    @staticmethod
    def print_if_database_empty():
        print("Database is empty!")
