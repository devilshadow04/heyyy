'''
Interface of the exam
'''

import setup
import sys
import os
from exam import Exam
from question import Question


def parse_cmd_args(args):

    try:
        if len(args) < 3:
            print("Check command line arguments")
            return None
        path = args[1]
        duration = args[2]
        shuffle_flag = False
        if len(args) >= 4:
            if args[3] == "-r":
                shuffle_flag = True

        try:
            duration = int(duration)
            return (path, duration, shuffle_flag)
        except:
            print("Duration must be an integer")
            return None
    except:
        return None


def setup_exam(obj):
    '''
    Update exam object with question contents extracted from file
    Parameter:
        obj: Exam object
    Returns:
        (obj, status): tuple containing updated Exam object and status
        where status: bool, True if exam is setup successfully. Otherwise, False.
    '''
    try:
        file_name = os.path.join(obj.path_to_dir, "questions.txt")
        fobj = open(file_name, "r")
        ques = setup.extract_questions(fobj)
        if obj.set_questions(ques):
            obj.set_questions(ques)
            obj.set_exam_status()
            return (obj, True)
        else:
            return (obj, False)
    except:
        return (obj, False)


def main(args):
    '''
    Implement all stages of exam process.
    '''
    exam_details = parse_cmd_args(args)
    if exam_details == None:
        return
    else:
        (path, duration, shuffle_flag) = parse_cmd_args(args)
        txt_path = os.path.join(path, "questions.txt")
        csv_path = os.path.join(path, "students.csv")
        check_txt = os.path.exists(txt_path)
        check_csv = os.path.exists(csv_path)
        if not check_txt or not check_csv:
            print("Missing files")
            return
        else:
            exam_obj = Exam(duration, path, shuffle_flag)
            print("Setting up exam...")
            exam_obj, status = setup_exam(exam_obj)
            if status == False:
                print("Error setting up exam")
                return
            elif status == True:
                print("Exam is ready")
                while True:
                    n = input("Do you want to preview the exam [Y|N]? ")
                    if n.lower() == "y":
                        exam_obj.preview_exam()

                    elif n.lower() == "n":
                        break
                    else:
                        print("Invalid command.")

                return exam_obj, status

if __name__ == "__main__":

    main(sys.argv)
