"""
There is a survey that consists of n questions where each question's answer is either 0 (no) or 1 (yes).

The survey was given to m students numbered from 0 to m - 1 and m mentors numbered from 0 to m - 1.

The answers of the students are represented by a 2D integer array students where students[i] is an integer array
that contains the answers of the ith student (0-indexed).
The answers of the mentors are represented by a 2D integer array mentors where mentors[j] is an integer array
that contains the answers of the jth mentor (0-indexed).

Each student will be assigned to one mentor, and each mentor will have one student assigned to them.

The compatibility score of a student-mentor pair is the number of answers that are the same for both.

For example, if the student's answers were [1, 0, 1] and the mentor's answers were [0, 0, 1],
then their compatibility score is 2 because only the second and the third answers are the same.

You are tasked with finding the optimal student-mentor pairings to maximize the sum of the compatibility scores.
Given students and mentors, return the maximum compatibility score sum that can be achieved.

Example:
    Input: students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
    Output: 8
"""


def comparison(student, mentor):
    cs = 0
    for i in range(len(student)):
        if student[i] == mentor[i]:
            cs += 1
    return cs


def WrongSolution1(students, mentors):
    """ The best mentors for student i may be assigned to some student before"""
    mentor_assigned = []
    css = 0
    for i in range(len(students)):
        max_cs = 0
        mentor_id = 0
        for j in range(len(mentors)):
            if j not in mentor_assigned:
                cs = comparison(students[i], mentors[j])
                if cs > max_cs:
                    max_cs = cs
                    mentor_id = j
        print(i, mentor_id, max_cs)
        mentor_assigned.append(mentor_id)
        css += max_cs
    return css

def maxCompatibilitySum(students, mentors):
    pass


students = [[1, 1, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0]]
mentors = [[1, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0]]
print()
