'''
Interface of the exam
'''

import setup
import program_two

def main(args):
    cand_lst = program_two.main(args)
    if cand_lst != None:

        invalid_sid_count = 0
        name_error_count = 0
        while invalid_sid_count < 3 and name_error_count < 3:
            n = input("Enter your student identification number (SID) to start exam: ")
            if len(n) == 9 and n.isdigit():
                n = int(n)
                j = 0
                while j < len(cand_lst):
                    cand = cand_lst[j]
                    if int(cand.sid) == n:
                        print("Verifying candidate details...")
                        while name_error_count < 3:
                            name = input("Enter your full name as given during registration of exam: ")
                            if name.lower() == cand.name.lower():
                                print("Start exam....\n")
                                cand.do_exam(False)
                                return
                            else:
                                name_error_count += 1
                                if name_error_count != 3:
                                    print("Name does not match records.")

                        break

                    j += 1


                if j == len(cand_lst):
                    print("Candidate number not found for exam.")
                    while True:
                        a = input("Do you want to try again [Y|N]? ")
                        if a.lower() == "y":
                            invalid_sid_count += 1
                            break
                        elif a.lower() == "n":
                            return
                        else:
                            print("Response must be [Y|N].")

            else:
                print("Invalid SID.")
                invalid_sid_count += 1

        if invalid_sid_count == 3:
            print("Contact exam administrator.")

        elif name_error_count == 3:
            print("Contact exam administrator to verify documents.")

