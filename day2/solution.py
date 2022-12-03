from pathlib import Path
from typing import Generator, Iterable, Tuple

# Implementation

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

def total_score(strategy: Iterable[Tuple[str, str]]) -> int:
    return sum(map(turn_score, strategy))

def turn_score(turn: Tuple[str, str]) -> int:
    return SHAPE_SCORE[turn[1]] + OUTCOME_SCORE[turn]

def read_strategy(path: Path) -> Generator[Tuple[str, str], None, None]:
    with open(path) as f:
        for line in f:
            yield tuple(line.rstrip().split())

# Tests

TEST_STRATEGY = (
    ('A', 'Y'),
    ('B', 'X'),
    ('C', 'Z'),
)

def test_total_score():
    assert total_score(TEST_STRATEGY) == 15

def test_read_strategy():
    path = Path('test_input.txt')
    actual = tuple(read_strategy(path))
    assert actual == TEST_STRATEGY
