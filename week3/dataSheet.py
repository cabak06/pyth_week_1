import course

class DataSheet:
    def __init__(self, courses: list):
        self.courses = courses


    def __str__(self):
        return '{courses}'.format(
            courses = self.courses
        )    


    def get_grades_as_list(self):
        list_grades = []
        for course in self.courses:
            list_grades.append(course.grade)
        return list_grades


    def get_ects_as_list(self):
        list_ects = []
        for course in self.courses:
            list_ects.append(course.ects)
        return list_ects
