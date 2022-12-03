import java.io.File

fun itemPriority(item: Char): Int {
    // 'A' has an ASCII code of 65 and a priority of 27 => 38.
    // 'a' has an ASCII code of 97 and a priority of 1 => 96.
    val offset = if (item.isUpperCase()) 38 else 96
    return item.code - offset
}

fun sharedItem(rucksack: String): Char {
    return rucksack
        .chunked(rucksack.length / 2, {c -> c.toSet()})
        .reduce {a, b -> a.intersect(b)}
        .single()
}

fun prioritySum(filePath: String): Int {
    return File(filePath).useLines {lines -> lines
        .map {rucksack -> sharedItem(rucksack)}
        .map {item -> itemPriority(item)}
        .sum()
    }
}

fun testPart1(filePath: String, expected: Int? = null) {
    val sum = prioritySum(filePath)
    println("${filePath}: ${sum}")
    if (expected != null) {
        assert(sum == expected)
    }
}

fun part1() {
    testPart1("test_input.txt", 157)
    testPart1("input.txt", 8252)
}

fun main() {
    part1()
}
