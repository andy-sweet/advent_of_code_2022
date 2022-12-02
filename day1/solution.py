from pathlib import Path
from typing import Generator, Iterable, List
from heapq import heappushpop

# Implementation

def read_elf_item_calories(path: Path) -> Generator[List[int], None, None]:
    elf_item_calories = []
    with open(path) as f:
        for line in f:
            item = line.rstrip()
            if item == '':
                yield list(elf_item_calories)
                elf_item_calories.clear()
            else:
                elf_item_calories.append(int(item))
    yield elf_item_calories

def max_elf_calories(elf_item_calories: Iterable[List[int]]) -> int:
    return max(sum(elf) for elf in elf_item_calories)

def top_three_elf_calories(elf_item_calories: Iterable[List[int]]) -> List[int]:
    top_three = [0] * 3
    for elf in map(sum, elf_item_calories):
        heappushpop(top_three, elf)
    return top_three

# Tests

TEST_ELF_ITEM_CALORIES = [
    [1000, 2000, 3000],
    [4000],
    [5000, 6000],
    [7000, 8000, 9000],
    [10000],
]

def test_read_elf_item_calories():
    path = Path('test_input.txt')
    actual = list(read_elf_item_calories(path))
    assert actual == TEST_ELF_ITEM_CALORIES

def test_max_elf_calories():
    actual = max_elf_calories(TEST_ELF_ITEM_CALORIES)
    assert actual == 24000

def test_sum_top_three_calories():
    actual = sum(top_three_elf_calories(TEST_ELF_ITEM_CALORIES))
    assert actual == 45000

# The real deal

def main():
    path = Path('input.txt')
    elf_item_calories = read_elf_item_calories(path)
    top_three_elf_cals = top_three_elf_calories(elf_item_calories)
    print(f'part 1: {top_three_elf_cals[-1]}')
    print(f'part 2: {sum(top_three_elf_cals)}')

if __name__ == '__main__':
    main()

