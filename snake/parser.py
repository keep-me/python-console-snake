
from optparse import OptionParser
import config

options = None


def init():
    global options

    parser = OptionParser()

    parser.add_option("-s", "--size",
                      action="store", dest="size", default='s',
                      help="Game size (s | m | l)")

    parser.add_option("-f", "--fullscreen",
                      action="store_true", dest="fullscreen", default=False,
                      help="Play fullscreen")

    parser.add_option("-t", "--theme",
                      action="store", dest="theme", default='classic',
                      help="Game theme (classic | minimal | jungle | custom)")

    parser.add_option("-d", "--difficulty",
                      action="store", dest="difficulty", default='normal',
                      help="Game difficulty (easy | normal | hard)")

    (options, args) = parser.parse_args()
    
    if options.difficulty in config.difficulty_levels:
        config.current_difficulty = options.difficulty
        config.frame_len = config.difficulty_levels[options.difficulty]['frame_len']
