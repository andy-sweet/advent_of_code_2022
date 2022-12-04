// Implementation

import java.io.File

fun itemPriority(item: Char): Int {
    // 'A' has an ASCII code of 65 and a priority of 27 => 38.
    // 'a' has an ASCII code of 97 and a priority of 1 => 96.
    val offset = if (item.isUpperCase()) 38 else 96
    return item.code - offset
}

fun sharedItem(rucksack: String): Char {
    return rucksack
        .chunked(rucksack.length / 2, CharSequence::toSet)
        .reduce(Set<Char>::intersect) 
        .single()
}

fun prioritySum(filePath: String): Int {
    return File(filePath).useLines {lines -> lines
        .map(::sharedItem)
        .map(::itemPriority)
        .sum()
    }
}

fun groupItem(rucksacks: List<String>): Char {
    return rucksacks
        .map(String::toSet)
        .reduce(Set<Char>::intersect) 
        .single()
}

fun groupPrioritySum(filePath: String): Int {
    return File(filePath).useLines {lines -> lines
        .chunked(3)
        .map(::groupItem)
        .map(::itemPriority)
        .sum()
    }
}

// Tests

fun testPart1(filePath: String, expected: Int? = null) {
    val sum = prioritySum(filePath)
    println("${filePath}: ${sum}")
    if (expected != null) {
        assert(sum == expected)
    }
}

fun testPart2(filePath: String, expected: Int? = null) {
    val sum = groupPrioritySum(filePath)
    println("${filePath}: ${sum}")
    if (expected != null) {
        assert(sum == expected)
    }
}

// Main

fun part1() {
    testPart1("test_input.txt", 157)
    testPart1("input.txt", 8252)
}

fun part2() {
    testPart2("test_input.txt", 70)
    testPart2("input.txt", 2828)
}

fun main() {
    part1()
    part2()
}
