"""
Problem: Course Schedule
Difficulty: Medium
Link: https://leetcode.com/problems/course-schedule/

There are numCourses courses (0 to numCourses-1). Given prerequisites[i] = [a, b]
meaning you must take course b before a, return True if you can finish all courses.

Example:
    Input: numCourses = 2, prerequisites = [[1,0]]
    Output: True

This is essentially detecting a cycle in a directed graph.

Approach: DFS cycle detection — O(V + E) time, O(V + E) space
"""


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    # Build adjacency list
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = visiting (in stack), 2 = done
    state = [0] * num_courses

    def has_cycle(course: int) -> bool:
        if state[course] == 1:  # Cycle detected
            return True
        if state[course] == 2:  # Already processed
            return False

        state[course] = 1  # Mark as visiting
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True
        state[course] = 2  # Mark as done
        return False

    for course in range(num_courses):
        if has_cycle(course):
            return False

    return True


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))              # True
    print(can_finish(2, [[1, 0], [0, 1]]))      # False (cycle)
    print(can_finish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # True
