#!/usr/bin/env python3
"""This module defines the function top_students."""


def top_students(mongo_collection):
    """This function returns all students sorted by average score."""

    students = list(mongo_collection.find())

    for student in students:
        topics = student.get('topics')
        scores = [topic.get('score') for topic in topics]
        average_score = sum(scores) / len(scores)
        student['averageScore'] = average_score

    students_sorted = sorted(students, key=lambda x: x['averageScore'],
                             reverse=True)

    return students_sorted
