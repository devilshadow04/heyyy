import os


class Candidate:
    def __init__(self, sid, name, time):
        self.sid = sid
        self.name = name
        self.extra_time = time
        self.exam = None
        self.confirm_details = False
        self.results = []

    def get_duration(self):
        '''
        Returns total duration of exam.
        '''
        total_time = self.extra_time + self.exam.duration
        return total_time

    def edit_sid(self, sid):
        '''
        Update attribute sid
        '''
        if isinstance(sid, str) and len(str(sid)) == 9:
            flag = False
            try:
                sid = int(sid)
                if sid > 0:
                    flag = True
            except:
                flag = False

            if flag == True:
                self.sid = str(sid)

    def edit_extra_time(self, t):
        '''
        Update attribute extra_time
        '''
        if isinstance(t, int):
            if int(t) > 0:
                self.extra_time = t

    def set_confirm_details(self, sid, name):
        '''
        Update attribute confirm_details
        '''
        if sid == self.sid and name == self.name:
            self.confirm_details = True
            return True
        else:
            self.confirm_details = False
            return False

    def log_attempt(self, data):
        '''
        Save data into candidate's file in Submissions.
        '''
        exam_path = self.exam.path_to_dir
        sub_path = os.path.join(exam_path, "submissions")
        if not os.path.exists(sub_path):
            os.makedirs(sub_path)
        data_path = os.path.join(sub_path, f"{self.sid}.txt")
        f = open(data_path, "w")
        f.write(data)

    def set_results(self, ls):
        '''
        Update attribute results if confirm_details are True
        '''
        if self.confirm_details == True and len(ls) == len(self.exam.questions) - 1:
            self.results = ls

    def do_exam(self, preview=True):
        '''
        Display exam and get candidate response from terminal during the exam.
        '''

        print(f"Candidate: {self.name}({self.sid})")
        t = self.get_duration()
        print(f"Exam duration: {t} minutes")
        print(f"You have {str(t)} minutes to complete the exam.")
        print(f"{self.exam.get_name()}")
        exam_questions = self.exam.questions
        i = 0
        data = ""
        while i < len(exam_questions):
            mark = 0.00
            ques = exam_questions[i]
            print(f"{ques.preview_question(i + 1, False)}")
            data += f"{ques.preview_question(i + 1, False)}\n"
            if i < len(exam_questions) - 1:
                if preview == True:
                    print(f"Response for Question {i + 1}: \n")

                else:
                    response = input(f"Response for Question {i + 1}: ")
                    data += f"Response for Question {i + 1}: {response}\n\n"
                    print()
                    if ques.qtype == "single":
                        if response == "A" or response == "B" or response == "C" or response == "D":
                            mark = ques.mark_response(response)
                    elif ques.qtype == "multiple":
                        flag = True
                        response_lst = response.split(", ")
                        if len(response_lst) != 2:
                            flag = False
                        else:
                            j = 0
                            while j < len(response_lst):
                                res = response_lst[j]
                                if res != "A" and res != "B" and res != "C" and res != "D":
                                    flag = False
                                j += 1

                        if flag == True:
                            mark = ques.mark_response(response)
                    elif ques.qtype == "short":
                        mark = ques.mark_response(response)

                    data += f"You have scored {mark:.2f} marks.\n"

            i += 1

        self.log_attempt(data)

    def __str__(self):
        pass
