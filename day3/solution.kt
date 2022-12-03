import java.io.File

fun itemPriority(item: Char): Int {
    // 'A' has an ASCII code of 65 and a priority of 27 => 38.
    // 'a' has an ASCII code of 97 and a priority of 1 => 96.
    val offset = if (item.isUpperCase()) 38 else 96
    return item.code - offset
}

fun priority(rucksack: String): Int {
    val mid_point = rucksack.length / 2
    val compartments = rucksack.chunked(mid_point, {c -> c.toSet()})
    val shared_item = compartments[0].intersect(compartments[1]).single()
    return itemPriority(shared_item)
}

fun prioritySum(filePath: String): Int {
    return File(filePath).useLines {lines -> lines
        .map {r -> priority(r)}
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