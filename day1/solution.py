from pathlib import Path
from typing import List

def max_elf_calories(elf_item_calories: List[List[int]]) -> int:
    return max(sum(item) for item in elf_item_calories)

def read_elf_item_calories(path: Path) -> List[List[int]]:
    with open(path) as f:
        lines = f.read().splitlines()
    elf_item_calories = [[]]
    for item in lines:
        if item == '':
            elf_item_calories.append([])
        else:
            elf_item_calories[-1].append(int(item))
    return elf_item_calories

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

def main():
    path = Path('input.txt')
    elf_item_calories = read_elf_item_calories(path)
    print(max_elf_calories(elf_item_calories))

if __name__ == '__main__':
    main()
