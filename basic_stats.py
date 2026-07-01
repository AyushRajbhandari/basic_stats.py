# Author: Ayush Rajbhandari
# Date: 2026-06-30
# Description: Defines a Student class with private members and a basic_stats function
#              that calculates the mean, median, and mode of a list of Student grades.

"""
This module has a Student class and a basic_stats function.
It uses the statistics module to compute grade statistics.
"""

import statistics

class Student:
    """
    A class representing a student.
    Contains private data members for the student's name and grade.
    """

    def __init__(self, name, grade):
        """
        Initializes the Student object with a name and a grade.
        Both data members are strictly private.
        """
        self.__name = name
        self.__grade = grade

    def get_grade(self):
        """
        Returns the student's grade.
        """
        return self.__grade


def basic_stats(student_list):
    """ Takes a list of Student objects and returns the mean, median, and mode of the grades."""
    # Extract all grades into a list
    grades_list = [student.get_grade() for student in student_list]

    # Calculate statistics using the statistics module
    mean_grade = statistics.mean(grades_list)
    median_grade = statistics.median(grades_list)
    mode_grade = statistics.mode(grades_list)

    # Return exactly as a tuple in the specified order
    return (mean_grade, median_grade, mode_grade)
