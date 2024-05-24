

'''
Functions to setup the exam questions and candidate list for the exam.
'''
# please do not change or add another import
import question
import candidate
import io


def extract_questions(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each question found in the file.
    General procedure to extract question.
    1. Extract the following
        - type
        - question details (description)
        - possible answers (if any)
        - expected answer
        - marks
        (you shouldn't need to perform error handling on these details,
        this is handled in the next step).
    2. You'll need to convert the possible answers (if any) to a list of tuples (see
       "Section 1. Setup the exam - Question" for more details). All flags can be False.
    3. Create a question object and call the instance methods to set the
       attributes. This will handle the error handling.
    4. Repeat Steps 1-3 for the next question until there are no more questions.
    5. You will need to create an end question as well.
    6. Create the list for all your questions and return it.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Question objects.
    """
    line_lst = fobj.readlines()
    i = 0
    ques = []
    while i < len(line_lst):
        line = line_lst[i].rstrip("\n")
        if line == "":
            i += 1
            continue
        if line.startswith("Question - "):
            try:
                ques_type = line.split("Question - ")[1].strip().lower()
            except:
                ques_type = None
            if ques_type != "single" and ques_type != "multiple" and ques_type != "short" and ques_type != "end":
                current_ques = question.Question(None)
            else:
                current_ques = question.Question(ques_type)
            ques_des = ""
            lst = []
            j = i + 1
            while True:
                next_line = line_lst[j]
                if next_line.startswith("Possible Answers:") or next_line.startswith("Expected Answer:"):
                    break
                ques_des += next_line
                j += 1
            current_ques.set_description(ques_des.strip("\n"))
        elif line.startswith("Possible Answers:"):
            lst = []
            j = i + 1
            while j < len(line_lst):
                choice = line_lst[j].rstrip("\n")
                if choice.startswith("Expected Answer:"):
                    break
                lst.append((choice, False))
                j += 1

        elif line.startswith("Expected Answer:"):
            try:
                ques_correct_ans = line.split("Expected Answer: ")[1]
            except:
                ques_correct_ans = None
            current_ques.set_correct_answer(ques_correct_ans)
            current_ques.set_answer_options(lst)
        elif line.startswith("Marks: "):
            try:
                ques_marks = int(line.split("Marks: ")[1])
            except:
                ques_marks = None
            current_ques.set_marks(ques_marks)
            ques.append(current_ques)

        i += 1
    ques.append(question.Question("end"))
    return ques


def sort(to_sort: list, order: int=0)->list:
    """
    Sorts to_sort depending on settings of order.

    Parameters:
        to_sort: list, list to be sorted.
        order: int, 0 - no sort, 1 - ascending, 2 - descending
    Returns
        result: list, sorted results.
    """
    if not isinstance(to_sort, list):
        return None

    try:
        if order == 0:
            return to_sort
        elif order == 1:
            i = 0
            while i < len(to_sort):
                j = i + 1
                while j < len(to_sort):
                    if to_sort[i] >= to_sort[j]:
                        to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
                    j += 1
                i += 1
            return to_sort
        elif order == 2:
            i = 0
            lst = []
            while i < len(to_sort):
                j = i + 1
                while j < len(to_sort):
                    if to_sort[i] <= to_sort[j]:
                        to_sort[i], to_sort[j] = to_sort[j], to_sort[i]
                    j += 1
                i += 1
            return to_sort
        else:
            return to_sort
    except:
        return None


def extract_students(fobj: io.TextIOWrapper)->list:
    """
    Parses fobj to extract details of each student found in the file.

    Parameter:
        fobj: open file object in read mode
    Returns:
        result: list of Candidate objects sorted in ascending order
    """
    lst = []
    try:
        fobj_lst = fobj.readlines()
        i = 1
        while i < len(fobj_lst):
            line = fobj_lst[i].rstrip("\n")
            line_lst = line.split(",")
            sid = line_lst[0]
            name = line_lst[1]
            time = line_lst[2]
            if time == "":
                time = 0
            else:
                time = int(time)
            cand = candidate.Candidate(sid, name, time)
            lst.append((sid, cand))
            i += 1

        sort(lst, 1)
        j = 0
        cand_lst = []
        while j < len(lst):
            cand = lst[j][1]
            cand_lst.append(cand)
            j += 1
        return cand_lst
    except:
        return []

f = open("students.csv")
print(extract_students(f))