# Gautam Ahuja
# CS-1340: Computer Networks
# Assignment 3: Transport Layer - Transmission Control Protocol (TCP)
# utils.py file enables the server to answer the questions asked by the client.
# The ```utils.py``` file contains the following:
# - ```question_list``` : A list of questions to be sent to the client.
# - ```core_courses``` : A list of core courses and their credits.
# - ```courses_prereq``` : A dictionary of courses and their pre-requisites.
# - ```answer_list``` : A list of functions corresponding to the questions in ```question_list```.
# - ```init()``` : A function that sends the question list to the client.
# - ```next()``` : A function that sends the next question to the client.
# - ```q1()``` : A function that returns the answer to question 1.
# - ```q2()``` : A function that returns the answer to question 2.
# - ```q3()``` : ... and so on.

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
    "Physics": "Check with the Physics Department.",
    "Biology": "Check with the Biology Department.",
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
    "Programming Languages and Translation" : "Data Structures and Algorithms; Theory of Computation",
    "Embedded Systems" : "Computer Organisation and Systems",
    "Capstone Project" : "Talk to the advisor."
}

def q1():
    answer = '''The breakdown of academic and non-academic credits is as follows:
    .--------------------------------------------------------------------------------------------------------.
    |                                              Total Credits: 150                                        |
    |----------------------------------------------------|---------------------------------------------------|
    |                  Academic Credits: 144             |                Non-Academic Credits: 6            |
    |----------------------------------------------------|---------------------------------------------------|
    | FC Credits: 36 | CS Credits: 86 | Open Credits: 12 | Co-Curricular Credits: 4 | Internship Credits: 4  |
    *--------------------------------------------------------------------------------------------------------*
    '''
    return answer

def q2():
    answer = '''
    A minimum of 144 academic credits. 
    These academic credit breakdown is as follows:
    
    .----------------------------------------------------.
    |                  Academic Credits: 144             |
    |----------------------------------------------------|
    | FC Credits: 36 | CS Credits: 86 | Open Credits: 22 |
    *----------------------------------------------------*
    
    The remaining 22 academic credits can be earned by taking courses from
    any department within the university, including the Computer Science Department.
    '''
    return answer

def q3():
    answer = '''
    A minimum of 6 non-academic credits.
    These non-academic credit breakdown is as follows:
    
    .--------------------------------------------------.
    |                Non-Academic Credits: 6           |
    |--------------------------------------------------|
    | Co-Curricular Credits: 4 | Internship Credits: 4 |
    *--------------------------------------------------*
    '''
    return answer

def q4():
    answer = "The total number of CS credits required to complete the 4-year BSc Hons degree in CS is 86.\n"
    return answer

def q5():
    answer = '''
    CS Credits Breakdown: 
    A minimum of 86 credits from the Computer Science Department, divided as follows:
    The breakdown is as follows:
    
    .---------------------.
    |   CS Credits: 86    |
    |---------------------|
    | Core: 70            |
    | Electives: 12       |
    | Capstone Project: 4 |
    *---------------------*
    
    Additionaly, Students need to achieve a minimum grade of “B” in both Introduction to Computer Science 
    and Discrete Mathematics courses.
    '''
    return answer

def q6():
    answer = '''The Core Courses are as follows: 
======================================================
Bucket:
(Credits) Course Name
======================================================
    '''
    for i in range(len(core_courses)):
        answer += f'Bucket: {core_courses[i][0]}\n'
        for j in range(len(core_courses[i][1])):
            answer += f'\t({core_courses[i][1][j][0]}) {core_courses[i][1][j][1]}\n'
        answer += '------------------------------------------------------\n'
    answer += "\t*Physics & Biology courses are yet to be decided.\n"
    return answer

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
    answer = "The Foundation Courses are as follows:\n"
    for i in range(len(foundation_courses)):
        answer += f"\t{str(i + 1)}. {foundation_courses[i]}\n"
    return answer

def q8():
    sem_wise = [
        ["Calculus"],
        ["Introduction to Computer Science", "Discrete Mathematics"],
        ["Probability and Statistics", "Linear Algebra", "Data Structures and Algorithms"],
        ["Theory of Computation", "Computer Organisation and Systems"],
        ["Design Practices in CS", "Introduction to Machine Learning", "Computer Networks", "Information Security"],
        ["Design and Analysis of Algorithms", "Data Science and Management", "Embedded Systems"],
        ["Capstone Project", "Programming Languages and Translation"]
    ]
    answer = "The semester-wise breakdown of CS courses is as follows:\n"
    answer += "------------------------------------------------------\n"
    for i, courses in enumerate(sem_wise):
        answer += f"Semester {i + 1}:\n"
        for course in courses:
            answer += f"\t{course}\n"
    return answer

def q9(course_name):
    # Check if the user input is 'q' to quit.
    if course_name.lower() == 'q':
        return "(pre-req) Exiting pre-requisite search."
    # Check if the course is in the core courses.
    for key in courses_prereq:
        if key.lower().replace(" ", "") == course_name.lower().replace(" ", ""):
            return f"The pre-requisite for {key} is/are: {courses_prereq[key]}"
    return f"{course_name} is not a core course."


def q10():
    answer = "Ideal time to take elective courses is in the 8th Semester."
    answer += "\nSemester 8:\n"
    answer += "\tElective 1 (4 credits)\n"
    answer += "\tElective 2 (4 credits)\n"
    answer += "\tElective 3 (4 credits)"
    return answer

def init(client_socket):
    to_send = '''[GAUTAM AHUJA]

Welcome to the CS Course Advisor!
======================================================
List of questions:
'''
    questions_string = '\n'.join(question_list)
    to_send += questions_string
    to_send += '''
======================================================
(main) Enter the question number (or 'or 'q' for questions or 'quit' to quit): '''
    client_socket.send(to_send.encode())

def ques_list(client_socket):
    to_send = '''List of questions:\n'''
    questions_string = '\n'.join(question_list)
    to_send += questions_string
    to_send += '''
======================================================
(main) Enter the question number (or 'or 'q' for questions or 'quit' to quit): '''
    client_socket.send(to_send.encode())

def next(client_socket, optional=""):
    to_send = optional + '''

(main) Enter the next question number (or 'or 'q' for questions or 'quit' to quit): '''
    client_socket.send(to_send.encode())

# Answer List
answer_list = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]