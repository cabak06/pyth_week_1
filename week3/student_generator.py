
import random
import student
import dataSheet
import course
import csv
import matplotlib.pyplot as plt 


rand_nameList = ["Alfred","Peter","Hanne","Jane","Hans","Siv","Svend","Jon"]
rand_genderList = ["Male","Female"]

#datasheet/course-info
rand_courseNameList = ["Geography","Math","Science","Litterature","Business","Statistics"]
rand_classroomList = [100,200,300,400,500]
rand_teacherList = ['Mr. Hook','Mr. Wood','Miss Adler','Mrs Snow','Mr Twist']
rand_ECTS_List = [5,10,15,20,25,30]
rand_gradeList = [-2,int(),2,4,7,10,12]


rand_UrlList = ["https://pixabay.com/photos/friendship-fun-backlighting-funny-2366955/","https://pixabay.com/photos/three-wheeler-tricycle-trike-locked-336700/",
                  "https://pixabay.com/photos/hardwood-antique-backdrop-1851071/","https://pixabay.com/photos/sculpture-sand-sand-sculpture-70271/",
                  "https://pixabay.com/photos/lavender-lavender-field-894919/","https://pixabay.com/illustrations/poison-bottle-medicine-old-symbol-1481596/"
                 ]   


def generate_random_students():
    stud_calc = 0
    studentList = []
    #studentList = {}
    while stud_calc < 10:
        r_name = random.choice(rand_nameList)
        r_gender = random.choice(rand_genderList)
        r_Url = random.choice(rand_UrlList)
            
        #course/datasheet-info
        r_courseName = random.choice(rand_courseNameList)
        r_class = random.choice(rand_classroomList)
        r_teacher = random.choice(rand_teacherList)
        r_ECTS = random.choice(rand_ECTS_List)
        r_grade = random.choice(rand_gradeList)

        cours = course.Course(r_courseName,r_class,r_teacher,r_ECTS,r_grade)
        dat_sheet = dataSheet.DataSheet(cours)
        stud = student.Student(r_name,r_gender,dat_sheet,r_Url)
        studentList.append((stud))
       
        stud_calc +=1     
    
    return studentList
        


def read_students_to_CSV():
    students = generate_random_students()
    with open("student_info.csv", "w") as csv_file:
        csv_file.write(
            "stud_name,gender,course_name,teacher,ects,classroom,grade,img_url\n"
        )
        for s in students:
            #for c in s.data_sheet:
                csv_file.write(
                "{name},{gender},{course_name},{teacher},{ECTS},{classroom},{grade},{img_url}\n".format(
                    name=s.name,
                    gender= s.gender,               
                    course_name= s.data_sheet.courses.name,
                    teacher= s.data_sheet.courses.teacher,
                    ECTS = s.data_sheet.courses.ECTS,
                    classroom = s.data_sheet.courses.classroom,
                    grade = s.data_sheet.courses.grade,
                    img_url = s.image_url,
                    )
                ) 
   
           
#read_students_to_CSV()


def convert_CSV_to_list():

    stud_list = []
    with open('student_info.csv', 'r') as f:
        reader = csv.reader(f)
        reader.__next__()
        for row in reader:
            tmp_list = list(row)
            stud_name = tmp_list[0]
            stud_gender = tmp_list[1]
            cours_name = tmp_list[2]
            cours_class = tmp_list[5]
            cours_teacher = tmp_list[3]
            cours_ECTS = tmp_list[4]
            cours_grade = tmp_list[6]
            stud_imgURL = tmp_list[7]

            cours_Obj = course.Course(cours_name,cours_class,cours_teacher,cours_ECTS,cours_grade)
            dat_sheet = dataSheet.DataSheet(cours_Obj)
            stud_Obj = student.Student(stud_name,stud_gender,dat_sheet,stud_imgURL)

            stud_list.append(stud_Obj)
      
    return stud_list


#convert_CSV_to_list()


def get_average_grade():
    
    count_topics = 0
    count_sum = 0
    average = 0
    average_list = []
    tmp_list = []
    students = convert_CSV_to_list()
    
    #sorting
    students.sort(key=lambda x: x.name)
    
    names = []
    for student in students:
        names.append(student.name)
    
    #unique values
    names_set = set(names)
   
    for name in names_set:
        for student in students:
            if(name == student.name):
                img = student.image_url
                count_topics += 1
                count_sum += int(student.data_sheet.courses.grade)
        average = count_sum/count_topics
        tmp_list = [name,img,average]
        average_list.append(tmp_list)
        count_topics = 0
        count_sum = 0
        average = 0    
    
    return average_list
     


def get_barChart_average():
    average_list = get_average_grade()
    #sorting by average
    average_list.sort(key=lambda x: x[2])

    #creating the barchart
    name_list = ([item[0] for item in average_list])
    av_list = ([item[2] for item in average_list])
   
    plt.figure()
    plt.bar(name_list, av_list, linewidth=5)

    # Set chart title and label axes. 
    plt.title("Average Distribution", fontsize=24)
    plt.xlabel("Names", fontsize=14)
    plt.ylabel("Average", fontsize=14)
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)
    plt.show()

#get_barChart_average()


def get_progression_by_ects():
    #getting the list from csv_file
    students = convert_CSV_to_list()   
    count_ects = 0
    percent = 0
    progression_list = []
    tmp_list = []
      
    #sorting by names
    students.sort(key=lambda x: x.name)
    
    names = []
    for student in students:
        names.append(student.name)
    
    #unique values
    names_set = set(names)
    for name in names_set:
        for student in students:
            if(name == student.name):
                grade = int(student.data_sheet.courses.grade)
                if(grade >= 2):
                    count_ects += int(student.data_sheet.courses.ECTS)
                
        percent = (100/150)*count_ects        
        tmp_list = [name,percent]
        progression_list.append(tmp_list)
        count_ects = 0
        percent = 0
    
    return progression_list     



def get_barChart_progression():
    progression = get_progression_by_ects()
    
    #sorting by progression
    progression.sort(key=lambda x: x[1])

    #creating the barchart
    name_list = ([item[0] for item in progression])
    av_list = ([item[1] for item in progression])
   
    plt.figure()
    plt.bar(name_list, av_list, linewidth=5)

    # Set chart title and label axes. 
    plt.title("Progression", fontsize=24)
    plt.xlabel("Names", fontsize=14)
    plt.ylabel("Percent", fontsize=14)
    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    plt.show()

#get_barChart_progression()

