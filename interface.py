"""This module build the interface"""

import sys
import time
import database
import panel
from colorama import init, Fore, Back, Style

init(autoreset=True)


class TypeWrite(object):
    """Display text in console character to character"""

    def __init__(self):
        self.on = True
        self.__delay = .1
        self.__color_fore = Fore.LIGHTGREEN_EX

    def change_delay(self, delay):
        """Change delay"""
        self.__delay = delay

    def change_color(self, color):
        """Change color"""
        self.__color_fore = color

    def iter_cursor(self, string):
        """Read character to character a string"""
        for pointer in string:
            print(self.__color_fore + pointer, end="")
            time.sleep(self.__delay)
            sys.stdout.flush()


def build_head():
    """Building the Head of Program"""
    # DATABASE CONSULT
    consult = 'SELECT seq FROM sqlite_sequence WHERE name = "origen"'
    result_consult = database.db.sql_select(consult)

    # TEXTS
    logo = '.:.G L O S S A R Y - CXP 86.:.'
    label = 'Terms on system:'
    total_terms = str(result_consult[0])

    # COLORS
    color_fore = Fore.LIGHTGREEN_EX
    color_back = Fore.BLACK + Back.LIGHTGREEN_EX + Style.BRIGHT

    # FORMAT
    logo_label = '{:<76} {}'.format(logo, label)
    show_total_terms = ' {} '.format(total_terms.zfill(4))
    second_line = '━' * (len(logo_label + show_total_terms) + 1)

    # DISPLAY
    print(color_fore + logo_label, color_back + show_total_terms)
    print(color_fore + second_line)


def print_welcome():
    """Building the welcome message"""

    text = 'WELCOME TO GLOSSARY - CXP 86'
    line = "-" * len(text)
    message = '{:>64} \n{:>64}'.format(text, line)

    typewrite.change_delay(.01)
    while typewrite.on:
        typewrite.iter_cursor(message)
        typewrite.on = False


def principal_menu():
    """Building the principal options menu"""

    panel.head_foot_border.head(70)
    panel.body_border_menu.body(70)
    panel.head_foot_border.foot(70)


#   object instances
typewrite = TypeWrite()
