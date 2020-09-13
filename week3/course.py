class Course:
    def __init__(self, name, classroom, teacher, ECTS, grade = None):
       
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

    
    def __str__(self):
        return "Course: {name}\nClassroom: {room}\nTeacher: {teacher}\nECTS: {ECTS}\nOpt_Grade: {grade}".format(
            name=self.name,
            room=self.classroom,
            teacher=self.teacher,
            ECTS=self.ECTS,
            grade=self.grade,
        )    
    
    
    def __repr__(self):
        return "Course(%r, %r, %r,%r,%r)" % (
            self.name,
            self.classroom,
            self.teacher,
            self.ECTS,
            self.grade,
        )
    

