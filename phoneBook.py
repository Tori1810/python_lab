from controller import Controller
from keys_controller import KeysController
import configparser


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.cfg')

    if 'Controller' in config:
        if config['Controller']['type'] == 'ui':
            a = Controller()
            a.menu()
        elif config['Controller']['type'] == 'keys':
            a = KeysController()

#
# if __name__ == '__main__':
#     a = Controller()
#     a.menu()
