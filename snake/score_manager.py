
import os
import json

SCORE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scores.json')

difficulty_levels = {
    'easy': {'name': '简单', 'frame_len': 0.2, 'score_multiplier': 1},
    'normal': {'name': '普通', 'frame_len': 0.1, 'score_multiplier': 2},
    'hard': {'name': '困难', 'frame_len': 0.05, 'score_multiplier': 3},
}


def ensure_score_file():
    if not os.path.exists(SCORE_FILE):
        default_data = {
            'high_scores': {
                'easy': 0,
                'normal': 0,
                'hard': 0,
            },
            'leaderboard': []
        }
        with open(SCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(default_data, f, indent=2, ensure_ascii=False)


def load_scores():
    ensure_score_file()
    try:
        with open(SCORE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {
            'high_scores': {
                'easy': 0,
                'normal': 0,
                'hard': 0,
            },
            'leaderboard': []
        }


def save_scores(data):
    try:
        with open(SCORE_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except IOError:
        pass


def get_high_score(difficulty='normal'):
    data = load_scores()
    return data['high_scores'].get(difficulty, 0)


def update_high_score(score, difficulty='normal'):
    data = load_scores()
    current_high = data['high_scores'].get(difficulty, 0)
    if score > current_high:
        data['high_scores'][difficulty] = score
        save_scores(data)
        return True
    return False


def add_to_leaderboard(score, difficulty='normal'):
    data = load_scores()
    entry = {
        'score': score,
        'difficulty': difficulty,
        'difficulty_name': difficulty_levels[difficulty]['name'],
    }
    data['leaderboard'].append(entry)
    data['leaderboard'].sort(key=lambda x: x['score'], reverse=True)
    data['leaderboard'] = data['leaderboard'][:10]
    save_scores(data)


def get_leaderboard():
    data = load_scores()
    return data['leaderboard']
