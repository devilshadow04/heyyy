from question import Question


class Exam:
    def __init__(self, duration, path, shuffle):
        self.duration = duration
        self.path_to_dir = path
        self.shuffle = shuffle
        self.exam_status = False
        self.questions = []
        self.set_name(path)

    def set_name(self, path):
        """
        Sets the name of the exam.
        """
        # you'll need to add some code here
        self.path_to_dir = path
        directory_name = path.split('/')[-1]
        self.name = directory_name.replace(" ", "_")

    def get_name(self):
        """
        Returns formatted string of exam name.
        """
        name = self.name.replace("_", " ").upper()
        return name

    def set_exam_status(self):
        '''
        Set exam_status to True only if exam has questions.
        '''
        if isinstance(self.questions, list):
            if len(self.questions) > 0:
                self.exam_status = True
            else:
                self.exam_status = False
        else:
            self.exam_status = False

    def set_duration(self, t):
        '''
        Update duration of exam.
        Parameter:
            t: int, new duration of exam.
        '''
        if isinstance(t, int):
            if t > 0:
                self.duration = t

    def set_questions(self, ls):
        '''
        Verifies all questions in the exam are complete.
        Parameter:
            ls: list, list of Question objects
        Returns:
            status: bool, True if set successfully.
        '''
        if not isinstance(ls, list):
            return False

        i = 0
        while i < len(ls):
            ques = ls[i]
            if i == len(ls) - 1:
                if ques.qtype != "end":
                    print("End marker missing or invalid")
                    return False
                else:
                    if ques.description != None or ques.answer_options != [] or ques.correct_answer != None or ques.marks != None:
                        print("End marker missing or invalid")
                        return False

            else:
                if ques.qtype == "end":
                    print("End marker missing or invalid")
                    return False
                if ques.description == None or ques.correct_answer == None:
                    print("Description or correct answer missing")
                    return False
                if ques.qtype == "single" or ques.qtype == "multiple":
                    if len(ques.answer_options) != 4:
                        print("Answer options incorrect quantity")
                        return False
                if ques.qtype == "short":
                    if isinstance(ques.answer_options, list) and len(ques.answer_options) == 4:
                        print("Answer options should not exist")
                        return False
            i += 1
        self.questions = ls
        return True

    def preview_exam(self):
        '''
        Returns a formatted string.
        '''
        i = 0
        string = ""
        string += f"{self.get_name()}\n"
        while i < len(self.questions):
            ques = self.questions[i]
            string += f"{ques.preview_question(i + 1)}\n\n"
            i += 1
        return string

    def copy_exam(self):
        new_exam = Exam(self.duration, self.path_to_dir, self.shuffle)
        i = 0
        new_questions = []
        while i < len(self.questions):
            question = self.questions[i]
            new_questions.append(question.copy_question())
            i += 1

        new_exam.set_questions(new_questions)
        return new_exam

    def __str__(self):
        pass