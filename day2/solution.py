from typing import Dict, Tuple

SHAPE_SCORE = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

# opponent: you
OUTCOME_SCORE = {
    ('A', 'X'): 3, # rock, rock
    ('A', 'Y'): 6, # rock, paper
    ('A', 'Z'): 0, # rock, scissors
    ('B', 'X'): 0, # paper, rock
    ('B', 'Y'): 6, # paper, scissors
    ('B', 'Z'): 3, # paper, paper
    ('C', 'X'): 6, # scissors, rock
    ('C', 'Y'): 0, # scissors, paper
    ('C', 'Z'): 3, # scissors, scissors
}

def total_score(strategy: Tuple[Tuple[str, str]]) -> int:
    return sum(map(_turn_score, strategy))

def _turn_score(turn: Tuple[str, str]) -> int:
    return SHAPE_SCORE[turn[1]] + OUTCOME_SCORE[turn]

def test_total_score():
    strategy = (
        ('A', 'Y'),
        ('B', 'X'),
        ('C', 'Z'),
    )
    assert total_score(strategy) == 15
