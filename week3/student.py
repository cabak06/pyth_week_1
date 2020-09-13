import dataSheet
import course
import random


class Student:
    def __init__(self, name,gender,data_sheet: dataSheet,image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def __str__(self):
        return "Student: {name}\nGender: {gender}\nDataSheet: {data_sheet}\nImage_url: {image_url}\n".format(
            name=self.name,
            gender=self.gender,
            data_sheet=self.data_sheet,
            image_url=self.image_url,
        )  

    def __repr__(self):
        return "Student(%r,%r,%r,%r)" % (
            self.name,
            self.gender,
            self.data_sheet,
            self.image_url,
        )

    def get_avg_grade(self):
        tmp_grades = self.data_sheet.get_grades_as_list()
        total_sum = 0
        for grade in tmp_grades:
            total_sum += grade
        return total_sum / len(tmp_grades)



    def get_study_progression(self):
        tmp_ects = self.data_sheet.get_ects_as_list()
        total_sum = 0
        for ects in tmp_ects:
            total_sum += int(ects)
        return ((100/150)*total_sum)


    

            
