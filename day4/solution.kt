// Implementation

import java.io.File

class Range(
    val lower: Int,
    val upper: Int,
) {
    fun contained(other: Range): Boolean {
        return this.lower >= other.lower
            && this.upper <= other.upper
    }

    fun overlaps(other: Range): Boolean {
        return maxOf(this.lower, other.lower) <= minOf(this.upper, other.upper)
    }
}

fun parseAssignment(assignment: String): Range {
    val values = assignment.split('-').map(String::toInt).toList()
    return Range(values[0], values[1])
}

fun parseAssignments(line: String): Pair<Range, Range> {
    val values = line.split(',').map(::parseAssignment).toList()
    return Pair(values[0], values[1])
}

fun eitherAssignmentContained(assignments: Pair<Range, Range>): Boolean {
    return assignments.first.contained(assignments.second)
        || assignments.second.contained(assignments.first)
}

fun assignmentsOverlap(assignments: Pair<Range, Range>): Boolean {
    return assignments.first.overlaps(assignments.second)
}

fun countContainedAssignments(filePath: String): Int {
    return File(filePath).useLines {lines -> lines
        .map(::parseAssignments)
        .filter(::eitherAssignmentContained)
        .count()
    }
}

fun countOverlappingAssignments(filePath: String): Int {
    return File(filePath).useLines {lines -> lines
        .map(::parseAssignments)
        .filter(::assignmentsOverlap)
        .count()
    }
}

// Tests

fun testPart1(filePath: String, expected: Int? = null) {
    val count = countContainedAssignments(filePath)
    println("${filePath}: ${count}")
    if (expected != null) {
        assert(count == expected)
    }
}

fun testPart2(filePath: String, expected: Int? = null) {
    val count = countOverlappingAssignments(filePath)
    println("${filePath}: ${count}")
    if (expected != null) {
        assert(count == expected)
    }
}

// Main

fun part1() {
    testPart1("test_input.txt", 2)
    testPart1("input.txt")
}

fun part2() {
    testPart2("test_input.txt", 4)
    testPart2("input.txt")
}

fun main() {
    part1()
    part2()
}
