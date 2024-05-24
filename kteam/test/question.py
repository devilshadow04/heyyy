import random


def generate_order():
    """

    """
    num_lst = []
    num_lst.append(random.randint(0, 3))
    while True:
        if len(num_lst) == 4:
            break

        num = random.randint(0, 3)
        i = 0

        while i < len(num_lst):
            if num == num_lst[i]:
                break

            if i == len(num_lst) - 1:
                num_lst.append(num)

            i += 1
    return num_lst

class Question:

    def __init__(self, qtype):
        # you'll need to check if qtype is valid before assigning it
        if qtype == "single" or qtype == "multiple" or qtype == "short" or qtype == "end":
            self.qtype = qtype
        else:
            self.qtype = None
        self.description = None
        self.answer_options = []
        self.correct_answer = None
        self.marks = None

    def set_type(self, qtype):
        """
        Update instance variable qtype.
        """
        if qtype.lower() == "single" or qtype.lower() == "multiple" or qtype.lower() == "short" or qtype.lower() == "end":
            self.qtype = qtype
            return True
        return False

    def set_description(self, desc):
        """
        Update instance variable description.
        """
        if self.qtype == "end":
            return False
        if isinstance(desc, str) and len(desc) > 0:
            self.description = desc
            return True
        return False

    def set_correct_answer(self, ans):
        """
        Update instance variable correct_answer.
        """
        if self.qtype == "end":
            return False
        if isinstance(ans, str):
            if self.qtype == "single":
                if ans.upper() == "A" or ans.upper() == "B" or ans.upper() == "C" or ans.upper() == "D":
                    self.correct_answer = ans.upper()
                    return True
            elif self.qtype == "multiple":
                i = 0
                a = ans.split(", ")
                if len(a) < 2:
                    return False
                while i < len(a):
                    if a[i].upper() != "A" and a[i].upper() != "B" and a[i].upper() != "C" and a[i].upper() != "D":
                        return False
                    i += 1
                self.correct_answer = ans.upper()
                return True
            elif self.qtype == "short":
                self.correct_answer = ans
                return True
        return False

    def set_marks(self, num):
        """
        Update instance variable marks.
        """
        if self.qtype == "end":
            return False
        if isinstance(num, int) and num >= 0:
            self.marks = num
            return True
        return False

    def set_answer_options(self, opts):
        """
        Update instance variable answer_options.

        opts should have all flags equal to False when passed in.
        This method will update the flags based on the correct answer.
        Only then do we check that the number of correct answers is correct.
        """
        if self.qtype == "short" or self.qtype == "end":
            self.answer_options = opts
            return True
        elif self.qtype == "multiple" or self.qtype == "single":
            if isinstance(opts, list) and len(opts) == 4 and self.correct_answer != None:
                valid_ans_desc = ["A.", "B.", "C.", "D."]
                correct_ans_lst = self.correct_answer.split(", ")
                i = 0
                count = 0
                while i < len(opts):
                    if isinstance(opts[i], tuple) and len(opts[i]) == 2:
                        ans_desc = opts[i][0]
                        flag = opts[i][1]
                        if flag == False and isinstance(ans_desc, str):
                            ans_desc_first = ans_desc.split()[0]
                            if (ans_desc_first == valid_ans_desc[i]) and (flag == False):
                                j = 0
                                while j < len(correct_ans_lst):
                                    if correct_ans_lst[j] == ans_desc_first.rstrip("."):
                                        flag = True
                                        count += 1
                                    j += 1
                                self.answer_options.append((ans_desc, flag))
                            else:
                                self.answer_options = []
                                return False
                        else:
                            self.answer_options = []
                            return False
                    else:
                        self.answer_options = []
                        return False


                    i += 1

                if count == len(correct_ans_lst):
                    return True
                else:
                    return False
        return False

    def get_answer_option_descriptions(self):
        """
        Returns formatted string listing each answer description on a new line.
        Example:
        A. Answer description
        B. Answer description
        C. Answer description
        D. Answer description
        """
        if self.qtype == "short" or self.qtype == "end":
            return ""
        elif self.qtype == "single" or self.qtype == "multiple":
            i = 0
            str = ""
            while i < len(self.answer_options):
                ans_desc = self.answer_options[i][0]
                str += "{}\n".format(ans_desc)
                i += 1
            return str.rstrip()


    def preview_question(self, i=0, show=True):
        """
        Returns formatted string showing details of question.
        Parameters:
            i: int, placeholder for question number, DEFAULT = 0
            show: bool, True to show Expected Answers, DEFAULT = TRUE
        """
        string = ""
        if self.qtype == "end":
            return "-End-"
        else:
            if i == 0:
                i = "X"

            if self.qtype == "multiple":
                display_type = "Multiple Answers"
            else:
                display_type = f"{self.qtype.capitalize()} Answer"

            string += f"Question {i} - {display_type}[{self.marks}]\n"
            string += f"{self.description}\n"

            if self.qtype == "multiple" or self.qtype == "single":
                string += f"{self.get_answer_option_descriptions()}\n"

            if show == True:
                string += f"Expected Answer: {self.correct_answer}"

            return string.strip()



    def shuffle_answers(self):
        """
        Updates answer options with shuffled elements.
        Must call generate_order only once.
        """
        if self.qtype != "single" and self.qtype != "multiple":
            return
        order = Question.generate_order()
        i = 0
        shuffled_lst = []
        valid_options = ["A", "B", "C", "D"]
        while i < len(order):
            shuffled_options = self.answer_options[order[i]]
            shuffled_lst.append(shuffled_options)
            i += 1
        new_options_lst = []
        j = 0
        while j < len(shuffled_lst):
            ans_desc = shuffled_lst[j][0]
            ans_bool = shuffled_lst[j][1]
            ans_desc_lst = list(ans_desc)
            ans_desc_lst[0] = valid_options[j]
            new_ans_desc = "".join(ans_desc_lst)
            new_options_lst.append((new_ans_desc, ans_bool))
            j += 1

        self.answer_options = new_options_lst

        k = 0
        correct_ans = ""
        while k < len(new_options_lst):
            ans_bool = new_options_lst[k][1]
            ans_desc = new_options_lst[k][0]
            if ans_bool == True:
                correct_ans += f"{ans_desc[0]}, "
            k += 1
        self.correct_answer = correct_ans.strip(", ")

    def copy_question(self):

        new_question = Question(self.qtype)
        new_question.set_description(self.description)
        new_question.answer_options = self.answer_options
        new_question.set_correct_answer(self.correct_answer)
        new_question.set_marks(self.marks)
        return new_question

    def mark_response(self, response):
        if self.qtype == "end":
            return None
        if self.qtype == "single" or self.qtype == "short":
            if response == self.correct_answer:
                mark = self.marks
            else:
                mark = 0
        elif self.qtype ==  "multiple":
            mark = 0
            correct_ans_lst = self.correct_answer.split(", ")
            response_lst = response.split(", ")
            mark_for_one = self.marks/len(correct_ans_lst)
            i = 0
            while i < len(response_lst):
                res = response_lst[i]
                j = 0
                while j < len(correct_ans_lst):
                    if res == correct_ans_lst[j]:
                        mark += mark_for_one
                    j += 1
                i += 1
            mark = round(mark, 2)

        return mark


    def __str__(self):
        '''
        You are free to change this, this is here for your convenience.
        When you print a question, it'll print this string.
        '''
        return f'''Question {self.__hash__()}:
Type: {self.qtype}
Description: {self.description}
Possible Answers: {self.get_answer_option_descriptions()}
Correct answer: {self.correct_answer}
Marks: {self.marks}
'''

q = Question("multiple")
q.set_correct_answer("A, B")
q.set_marks(2)
print(q.mark_response("hello"))