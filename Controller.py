import Modules
import View
import serialize


def run_get_record_from_database(phone_book):
    """
    This function allows users get record from database by full name
    """
    print("-"*80)
    View.print_input_first_name()
    f_name = input()
    View.print_input_last_name()
    l_name = input()
    flag = Modules.print_one_record(f_name, l_name, phone_book)
    if flag == -1:
        View.print_if_record_absent()
    print("-"*80)


def run_show_all_database(phone_book):
    """
    This function shows all database
    """
    print("-"*80)
    flag = Modules.print_all_database(phone_book)
    if flag == -1:
        View.print_if_database_empty()
    print("-"*80)


def run_add_record_to_database(phone_book):
    """
    This function allows users add record to database
    """
    View.print_input_first_name()
    f_name = input()
    View.print_input_last_name()
    l_name = input()
    View.print_input_phone_number()
    phone_number = input()
    flag = Modules.add_record(f_name, l_name, phone_number, phone_book)
    if flag == 1:
        View.print_add_message()
    else:
        View.print_if_record_exist()


def run_delete_record_from_database(phone_book):
    """
    This function allows users delete record to database
    """
    View.print_input_first_name()
    f_name = input()
    View.print_input_last_name()
    l_name = input()
    index = Modules.check_record_in_database(f_name, l_name, phone_book)
    if index != -1:
        View.print_confirm_question()
        confirm = input()
        if confirm.lower() == 'y':
            Modules.delete_record(index, phone_book)
            View.print_delete_message()
    else:
        View.print_if_record_absent()


def menu():
    """
    This function realizes possibility work with database from console
    """
    ch = ''
    phone_book = serialize.Serialize.load("base")

    while ch != '5':
        print()
        View.print_menu()
        ch = input()
        if ch == '1':
            run_show_all_database(phone_book)
        elif ch == '2':
            run_get_record_from_database(phone_book)
        elif ch == '3':
            run_add_record_to_database(phone_book)
        elif ch == '4':
            run_delete_record_from_database(phone_book)
        elif ch == '5':
            break
        else:
            continue

    serialize.Serialize.save("base", phone_book)
    View.print_program_completed()
