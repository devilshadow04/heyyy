'''
Interface of the exam
'''

import setup
import program_one
import os
import sys

def assign_exam(exam_obj):
    path = exam_obj.path_to_dir
    csv_path = os.path.join(path, "students.csv")
    if os.path.exists(csv_path):
        f = open(csv_path)
        cand_lst = setup.extract_students(f)
        if cand_lst == [] or cand_lst == None:
            print("No candidates found in the file")
            return None
        print("Assigning exam to candidates...")
        i = 0
        while i < len(cand_lst):
            cand = cand_lst[i]
            cand.exam = exam_obj.copy_exam()
            if cand.exam.shuffle:
                cand_ques_lst = cand.exam.questions
                new_exam_ques = []
                j = 0
                while j < len(cand.exam.questions):
                    cand_ques = cand_ques_lst[j]
                    cand_ques.shuffle_answers()
                    new_exam_ques.append(cand_ques)
                    j += 1
                cand.exam.questions = new_exam_ques
            i += 1
        print(f"Complete. Exam allocated to {len(cand_lst)} candidates.")
        return cand_lst
    else:
        return None

def main(args):
    exam_obj, status = program_one.main(args)
    cand_lst = assign_exam(exam_obj)
    while True:
        n = input("Enter SID to preview student's exam (-q to quit): ")
        if n == "-q":
            break
        elif n == "-a":
            i = 0
            while i < len(cand_lst):
                cand = cand_lst[i]
                cand.do_exam()
                i += 1
        else:
            if len(n) == 9:
                try:
                    n = int(n)
                    j = 0
                    while j < len(cand_lst):
                        cand = cand_lst[j]
                        if cand.sid == str(n):
                            cand.do_exam()
                            break
                        if j == len(cand_lst) - 1:
                            print("SID not found in list of candidates.")
                        j += 1
                except:
                    print("SID is invalid.")

            else:
                print("SID is invalid.")
    return exam_obj, cand_lst

if __name__ == "__main__":
    main(sys.argv)