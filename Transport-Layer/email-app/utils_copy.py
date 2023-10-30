import sys
import os 

question_list =[
    "1. What is breakdown of academic and non-academic credits required to complete the 4-year BSc Hons degree in CS ?",
    "2. What is the breakdown of academic credits ?",
    "3. What is the breakdown of non-academic credits ?",
    "4. What is the total number of CS credits required to complete the 4-year BSc Hons degree in CS?",
    "5. Could you provide a breakdown of CS credits ?",
    "6. What are the core courses ?",
    "7. What are the Foundation Courses ?",
    "8. What is the semester-wise breakdown of CS courses ?",
    "9. What is the pre-requisite for ...?",
    "10. What is the ideal semester to take elective courses ?",
]

core_courses = [
    ["Basic Science and Maths", 
        [[4, "Probability and Statistics"], [4, "Linear Algebra"], [4, "Calculus"], [4, "Physics"], [4, "Biology"]]
    ],
    ["Computational Thinking", 
        [[4, "Introduction to Computer Science"], [4, "Discrete Mathematics"], [4, "Data Structures and Algorithms"], [4, "Introduction to Machine Learning"], [4, "Data Science and Management"], [4, "Theory of Computation"], [4, "Design and Analysis of Algorithms"], [4, "Programming Languages and Translation"], [2, "Information Security"]]
    ],
    [ "Systems and Software",
        [[4,"Computer Organisation and Systems"], [4, "Design Practices in CS"], [4, "Computer Networks"], [4, "Embedded Systems"]]
    ],
    ["Project", 
        [[4, "Capstone Project"]]
    ],
]

courses_prereq = {
    "Probability and Statistics" : "Mathematics in Grades XI and XII. Alternatively, Quantitative Reasoning and Mathematical Thinking (FC 0306) + Calculus Enabler (MAT 1000)",
    "Linear Algebra" : "Check with the Mathematics Department.",
    "Calculus" : "Check with the Mathematics Department.",
    "Physics": "TBD",
    "Biology": "TBD",
    "Introduction to Computer Science" : "Mathematics in Grades XI and XII. Alternatively, a minimum of B grade in both Quantitative Reasoning and Mathematical Thinking (FC 0306) and Calculus (MAT 1000)",
    "Discrete Mathematics" : "Mathematics in Grades XI and XII. Alternatively, a minimum of B grade in both Quantitative Reasoning and Mathematical Thinking (FC 0306) and Calculus (MAT 1000)",
    "Data Structures and Algorithms" : "Introduction to Computer Science; Discrete Mathematics",
    "Theory of Computation" : "Data Structures and Algorithms",
    "Computer Organisation and Systems" : "Introduction to Computer Science",
    "Introduction to Machine Learning" : "Probability and Statistics; Linear Algebra; Data Structures and Algorithms",
    "Computer Networks" :  "Introduction to Computer Science; Data Structures and Algorithms",
    "Information Security" : "Data Structures and Algorithms; Probability and Statistics",
    "Design and Analysis of Algorithms" : "Data Structure and Algorithms; Linear Algebra",
    "Data Science and Management" : "Data Structures and Algorithms; Introduction to Machine Learning",
    "Programming Languages and Translations" : "Data Structures and Algorithms; Theory of Computation",
    "Embedded Systems" : "Computer Organisation and Systems"
}

def q1():
    answer = '''
    *--------------------------------------------------------------------------------------------------------*
    |                                              Total Credits: 150                                        |
    |----------------------------------------------------|---------------------------------------------------|
    |                  Academic Credits: 144             |                Non-Academic Credits: 6            |
    |----------------------------------------------------|---------------------------------------------------|
    | FC Credits: 36 | CS Credits: 86 | Open Credits: 12 | Co-Curricular Credits: 4 | Internship Credits: 4  |
    *--------------------------------------------------------------------------------------------------------*
    '''
    print(answer)

def q2():
    answer = '''A minimum of 144 academic credits. 
    These academic credit breakdown is as follows:
    *----------------------------------------------------*
    |                  Academic Credits: 144             |
    |----------------------------------------------------|
    | FC Credits: 36 | CS Credits: 86 | Open Credits: 22 |
    *----------------------------------------------------*
    The remaining 22 academic credits can be earned by taking courses from
    any department within the university, including the Computer Science Department.
    '''
    print(answer)

def q3():
    answer=''' A minimum of 6 non-academic credits.
    These non-academic credit breakdown is as follows:
    *--------------------------------------------------*
    |                Non-Academic Credits: 6           |
    |--------------------------------------------------|
    | Co-Curricular Credits: 4 | Internship Credits: 4 |
    *--------------------------------------------------*
    '''

def q4():
    answer = "The total number of CS credits required to complete the 4-year BSc Hons degree in CS is 86."
    print(answer)

def q5():
    answer = '''CS Credits Breakdown: 
    A minimum of 86 credits from the Computer Science Department, divided as follows:
    The breakdown is as follows:
    |---------------------|
    |   CS Credits: 86    |
    |---------------------|
    | Core: 70            |
    | Electives: 12       |
    | Capstone Project: 4 |
    *---------------------*
    Additionaly, Students need to achieve a minimum grade of “B” in both Introduction to Computer Science 
    and Discrete Mathematics courses.
    '''
    print(answer)

def q6():
    print("The Core Courses are as follows: ")
    print("======================================================")
    print("Bucket:")
    print("\t(Credits) Course Name")
    print("======================================================")
    for i in range(len(core_courses)):
        print(f"Bucket: {core_courses[i][0]}")
        for j in range(len(core_courses[i][1])):
            print(f"\t({core_courses[i][1][j][0]}) {core_courses[i][1][j][1]}")
        print("------------------------------------------------------")
    print("Physics & Biology courses are To be decided.")

def q7():
    foundation_courses = [
        "Economy, Politics and Society",
        "Environmental Studies",
        "Great Books",
        "Indian Civilizations",
        "Introduction to Critical Thinking",
        "Literature and the World",
        "Mind and Behaviour",
        "Principels of Science",
        "Quantitative Reasoning and Mathematical Thinking"
    ]
    print("The Foundation Courses are as follows: ")
    for i in range(len(foundation_courses)):
        print(f"\t{str(i+1)}. {foundation_courses[i]}")

def q8():
    sem_wise = [
                    ["Calculus"],
                    ["Introduction to Computer Science", "Discrete Mathematics"],
                    ["Probability and Statistics", "Linear Algebra", "Data Structures and Algorithms"],
                    ["Theory of Computation", "Computer Organisation and Systems"],
                    ["Design Practices in CS", "Introduction to Machine Learning", "Computer Networks" , "Information Security"],
                    ["Design and Analysis of Algorithms", "Data Science and Management", "Embedded Systems"],
                    ["Capstone Project", "Programming Languages and Translation"]
            ]
    print("The semester-wise breakdown of CS courses is as follows: ")
    print("======================================================")
    for i in range(len(sem_wise)):
        print(f"Semester {i+1}:")
        for j in range(len(sem_wise[i])):
            print(f"\t{sem_wise[i][j]}")

def q9():
    print("Enter the course name (or 'q' to quit pre-requisite search): ", end="")
    course_name = input()
    if course_name == 'q':
        return
    # check if the course is in the core_courses
    for i in range(len(core_courses)):
        for j in range(len(core_courses[i][1])):
            if core_courses[i][1][j][1].lower().replace(" ", "") == course_name.lower().replace(" ", ""):
                print(f"The pre-requisite for {course_name} is/are: {courses_prereq[course_name]}")
                return
    print(f"{course_name} is not a core course.")

def q10():
    print("Ideal time to take elective courses is in the 8th Semester.")
    print("Semester 8:")
    print("\tElective 1 (4 credits)")
    print("\tElective 2 (4 credits)")
    print("\tElective 3 (4 credits)")


answer_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]


def init(clientsocket):
    to_send = '''
    Welcome to the CS Course Advisor!
    ==================================
    List of questions:
    '''
    questions_string = '\n'.join(question_list)
    to_send += questions_string
    to_send += '''
    ==================================
    Enter the question number (or 'q' to quit): '''
    clientsocket.send(to_send.encode())

if __name__ == "__main__":
    question_number = input()
    if question_number == 'q':
        sys.exit()
    question_number = int(question_number)
    if question_number < 1 or question_number > len(question_list):
        print("Invalid question number.")
        sys.exit()
    print("==================================")
    answer_list[question_number-1]()
    print("==================================")
    print("Thank you for using CS Course Advisor!")