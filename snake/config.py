
frame_len = .1

keys = {
    'DOWN': 0x42,
    'LEFT': 0x44,
    'RIGHT': 0x43,
    'UP': 0x41,
    'Q': 0x71,
    'ENTER': 0x0a,
    'SPACE': 0x20,
}

apple_domain = 1000

food_values = {
    'apple': 3,
}

game_sizes = {
    's': (15, 12),
    'm': (25, 20),
    'l': (40, 30),
}

initial_size = 4

difficulty_levels = {
    'easy': {'name': '简单', 'frame_len': 0.2, 'score_multiplier': 1},
    'normal': {'name': '普通', 'frame_len': 0.1, 'score_multiplier': 2},
    'hard': {'name': '困难', 'frame_len': 0.05, 'score_multiplier': 3},
}

current_difficulty = 'normal'
