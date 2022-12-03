import os
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Generator, Iterable, Tuple

THIS_DIR = Path(os.path.realpath(__file__)).parent

# Implementation
class Move(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

class Result(Enum):
    LOSS = auto()
    DRAW = auto()
    WIN = auto()

class Strategy(Enum):
    YOUR = auto()
    ELF = auto()

MOVE_SCORE = {
    Move.ROCK: 1,
    Move.PAPER: 2,
    Move.SCISSORS: 3,
}

RESULT_SCORE = {
    Result.LOSS: 0,
    Result.DRAW: 3,
    Result.WIN: 6,
}

YOUR_MOVE = {
    'X': Move.ROCK,
    'Y': Move.PAPER,
    'Z': Move.SCISSORS,
}

YOUR_RESULT = {
    'X': Result.LOSS,
    'Y': Result.DRAW,
    'Z': Result.WIN,
}

THEIR_MOVE = {
    'A': Move.ROCK,
    'B': Move.PAPER,
    'C': Move.SCISSORS,
}

BEATS = {
    Move.ROCK: Move.SCISSORS,
    Move.PAPER: Move.ROCK,
    Move.SCISSORS: Move.PAPER,
}

LOSES = {v: k for k, v in BEATS.items()}

@dataclass
class Turn:
    them: Move
    you: Move

    def result(self) -> Result:
        if self.you == self.them:
            return Result.DRAW
        if BEATS[self.you] == self.them:
            return Result.WIN
        return Result.LOSS

    def score(self) -> int:
        return MOVE_SCORE[self.you] + RESULT_SCORE[self.result()]

    @classmethod
    def from_line(cls, line: str, strategy: Strategy) -> 'Turn':
        return cls.from_your_line(line) if strategy == Strategy.YOUR else cls.from_elf_line(line)

    @classmethod
    def from_your_line(cls, line: str) -> 'Turn':
        parts = line.rstrip().split()
        return cls(
            them=THEIR_MOVE[parts[0]],
            you=YOUR_MOVE[parts[1]],
        )

    @classmethod
    def from_elf_line(cls, line: str) -> 'Turn':
        parts = line.rstrip().split()
        them = THEIR_MOVE[parts[0]]
        result = YOUR_RESULT[parts[1]]
        if result == Result.WIN:
            you = LOSES[them]
        elif result == Result.LOSS:
            you = BEATS[them]
        else:
            you = them
        return cls(them=them, you=you)

def total_score(turns: Iterable[Turn]) -> int:
    return sum(map(Turn.score, turns))

def read_turns(path: Path, strategy: Strategy) -> Generator[Turn, None, None]:
    with open(path) as f:
        for line in f:
            yield Turn.from_line(line, strategy) 

# Tests

def test_read_turns_with_your_strategy():
    path = THIS_DIR / 'test_input.txt'
    actual = tuple(read_turns(path, Strategy.YOUR))
    expected = (
        Turn(them=Move.ROCK, you=Move.PAPER),
        Turn(them=Move.PAPER, you=Move.ROCK),
        Turn(them=Move.SCISSORS, you=Move.SCISSORS),
    )
    assert actual == expected
    assert total_score(actual) == 15

def test_read_turns_with_elf_strategy():
    path = THIS_DIR / 'test_input.txt'
    actual = tuple(read_turns(path, Strategy.ELF))
    expected = (
        Turn(them=Move.ROCK, you=Move.ROCK),
        Turn(them=Move.PAPER, you=Move.ROCK),
        Turn(them=Move.SCISSORS, you=Move.ROCK),
    )
    assert actual == expected
    assert total_score(actual) == 12

# Main

def part1():
    path = THIS_DIR / 'input.txt'
    turns = read_turns(path, Strategy.YOUR)
    score = total_score(turns)
    print(f'part1: {score}')
    assert score == 11841

def part2():
    path = THIS_DIR / 'input.txt'
    turns = read_turns(path, Strategy.ELF)
    score = total_score(turns)
    print(f'part2: {score}')
    assert score == 13022

def main():
    part1()
    part2()

if __name__ == '__main__':
    main()