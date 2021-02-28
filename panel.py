from colorama import init, Fore, Back, Style

init(autoreset=True)


class Border(object):
    """Class for build the border of the panels"""

    green_color = Fore.LIGHTGREEN_EX
    magenta_color = Fore.LIGHTMAGENTA_EX
    green_background = Fore.BLACK + Back.LIGHTGREEN_EX + Style.BRIGHT
    magenta_background = Fore.BLACK + Back.LIGHTMAGENTA_EX + Style.BRIGHT
    styles = {
        'light_up': ('┌', '─', '┬', '┐'),
        'light_middle': ('│', '├', '┼', '┤'),
        'light_down': ('└', '─', '┴', '┘'),
        'heavy_up': ('┏', '━', '┳', '┓'),
        'heavy_middle': ('┃', '┣', '╋', '┫'),
        'heavy_down': ('┗', '━', '┻', '┛'),
        'double_up': ('╔', '═', '╦', '╗'),
        'double_middle': ('║', '╠', '╬', '╣'),
        'double_down': ('╚', '═', '╩', '╝'),
    }

    def __init__(self):
        """Default values for panel"""

        self.color = self.green_color
        self.background = self.green_background
        self.style_up = self.styles['light_up']
        self.up_border = {
            'ul': self.style_up[0],  # up_left ┏
            'up': self.style_up[1],  # up ━
            'um': self.style_up[2],  # up_middle ┳
            'ur': self.style_up[3]   # up_right ┓
        }
        self.style_middle = self.styles['light_middle']
        self.middle_border = {
            'lr': self.style_middle[0],  # left/right ┃
            'lt': self.style_middle[1],  # left┣
            'md': self.style_middle[2],  # middle ╋
            'rt': self.style_middle[3]   # right ┫
        }
        self.style_down = self.styles['light_down']
        self.down_border = {
            'dl': self.style_down[0],  # down_left ┗
            'dw': self.style_down[1],  # down ━
            'dm': self.style_down[2],  # down_middle ┻
            'dr': self.style_down[3]   # down_right ┛
        }

    def change_color(self, color):
        """Change the color of panel"""
        self.color = color

    def change_background(self, background):
        """Change the background of panel"""
        self.background = background

    def change_top_style(self, style):
        """Change the top style of panel"""

        self.up_border['ul'] = self.styles[style][0]
        self.up_border['up'] = self.styles[style][1]
        self.up_border['md'] = self.styles[style][2]
        self.up_border['ur'] = self.styles[style][3]

    def change_middle_style(self, style):
        """Change the  middle style of panel"""

        self.middle_border['lr'] = self.styles[style][0]
        self.middle_border['lt'] = self.styles[style][1]
        self.middle_border['md'] = self.styles[style][2]
        self.middle_border['rt'] = self.styles[style][3]

    def change_down_style(self, style):
        """Change the low style of panel"""

        self.down_border['dl'] = self.styles[style][0]
        self.down_border['dw'] = self.styles[style][1]
        self.down_border['dm'] = self.styles[style][2]
        self.down_border['dr'] = self.styles[style][3]


class HeadFootBorder(Border):
    """Building the head and the foot of a border"""

    WIDTH_MAXIMUM = 100

    def head(self, width):
        """Building the head of the panel"""

        spacing = " " * int((self.WIDTH_MAXIMUM - width) / 2)

        draw = '{}{}{}{}{}'.format(
            spacing,
            self.up_border['ul'],
            self.up_border['up'] * (width - 2),
            self.up_border['ur'],
            spacing)

        print(self.color + draw)

    def foot(self, width):
        """Building the foot of the panel"""

        spacing = " " * int((self.WIDTH_MAXIMUM - width) / 2)
        draw = '{}{}{}{}{}'.format(
            spacing,
            self.down_border['dl'],
            self.down_border['dw'] * (width - 2),
            self.down_border['dr'],
            spacing)

        print(self.color + draw)


class BodyBorder(HeadFootBorder):
    """Building the body of a border"""

    def body(self, width):
        """Building the body of the panel"""

        spacing = " " * int((self.WIDTH_MAXIMUM - width) / 2)
        in_spacing = width - 1
        draw = '{}{}{:>{}}{}'.format(
            spacing,
            self.middle_border['lr'],
            self.middle_border['lr'],
            in_spacing,
            spacing)

        print(self.color + draw)


class BodyBorderMenu(HeadFootBorder):
    """Building the body of a border"""

    def body(self, width):
        """Building the body of the panel"""

        spacing = " " * int((self.WIDTH_MAXIMUM - width) / 2)
        text = self.background + 'OPTIONS'
        in_spacing_content = (width - len(text)) - 1
        in_spacing = width - 1
        in_panel = '{}{}{:>{}}{}'.format(
            spacing,
            self.middle_border['lr'],
            self.middle_border['lr'],
            in_spacing,
            spacing)

        draw = '{}{}{}{:>{}}{}'.format(
            spacing,
            self.middle_border['lr'],
            text,
            self.middle_border['lr'],
            in_spacing_content,
            spacing)

        print(self.color + in_panel)
        print(self.color + draw)


border = Border()
head_foot_border = HeadFootBorder()
body_border = BodyBorder()
body_border_menu = BodyBorderMenu()
