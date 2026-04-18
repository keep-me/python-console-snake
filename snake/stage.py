
import console
import math
import config
import parser
import themes

MIN_WIDTH = 10
MIN_HEIGHT = 8


def init():
    global size, width, height, padding, boundaries, chosen_theme

    available_size = console.getTerminalSize()
    
    min_terminal_width = 40
    min_terminal_height = 20
    
    if available_size[0] < min_terminal_width:
        available_size = (min_terminal_width, available_size[1])
    if available_size[1] < min_terminal_height:
        available_size = (available_size[0], min_terminal_height)

    width, height = available_size

    chosen_size = config.game_sizes[parser.options.size]

    if parser.options.fullscreen:
        width = available_size[0] // 2 - 4
        height = available_size[1] - 4
    else:
        if chosen_size[0] > available_size[0] // 2:
            width = available_size[0] // 2
        else:
            width = chosen_size[0]

        if chosen_size[1] > available_size[1] - 4:
            height = available_size[1] - 4
        else:
            height = chosen_size[1]

    if width < MIN_WIDTH:
        width = MIN_WIDTH
    if height < MIN_HEIGHT:
        height = MIN_HEIGHT

    size = (width, height)

    padding_x = int(math.floor(available_size[0] - width * 2) / 4)
    padding_y = int(math.floor(available_size[1] - height) / 2)

    if padding_x < 0:
        padding_x = 0
    if padding_y < 0:
        padding_y = 0

    padding = (padding_y, padding_x, padding_y, padding_x)

    boundaries = {
        "bottom": int(math.floor(height / 2)),
        "left": int(math.floor(-width / 2)),
        "right": int(math.floor(width / 2)),
        "top": int(math.floor(-height / 2)),
    }

    chosen_theme = themes.game_themes[parser.options.theme]
