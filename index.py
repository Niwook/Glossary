"""This file managements the application flow"""

import database
import interface


def main():
    """Main loop"""

    while True:
        interface.build_head()
        interface.print_welcome()
        print("")
        interface.principal_menu()
        break


database.db.sql_close()
