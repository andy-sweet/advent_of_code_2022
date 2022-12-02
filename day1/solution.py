from pathlib import Path
from typing import List
from heapq import heappop, heappush

# Implementation

def read_elf_item_calories(path: Path) -> List[List[int]]:
    elf_item_calories = [[]]
    with open(path) as f:
        for line in f:
            item = line.rstrip()
            if item == '':
                elf_item_calories.append([])
            else:
                elf_item_calories[-1].append(int(item))
    return elf_item_calories

def max_elf_calories(elf_item_calories: List[List[int]]) -> int:
    return max(sum(item) for item in elf_item_calories)

def top_three_elf_calories(elf_item_calories: List[List[int]]) -> int:
    return sum(sorted(sum(item) for item in elf_item_calories)[-3:])


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
    actual = read_elf_item_calories(path)
    assert actual == TEST_ELF_ITEM_CALORIES

def test_max_elf_calories():
    actual = max_elf_calories(TEST_ELF_ITEM_CALORIES)
    assert actual == 24000

def test_top_three_calories():
    actual = top_three_elf_calories(TEST_ELF_ITEM_CALORIES)
    assert actual == 45000

# The real deal

def main():
    path = Path('input.txt')
    elf_item_calories = read_elf_item_calories(path)
    print(f'part 1: {max_elf_calories(elf_item_calories)}')
    print(f'part 2: {top_three_elf_calories(elf_item_calories)}')

if __name__ == '__main__':
    main()

