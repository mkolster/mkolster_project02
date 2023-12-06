from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import *
from gui import *
import csv
from logic_federal import FederalLogic
from datetime import datetime



class Logic(QMainWindow, Ui_PyVote_welcome):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.vote_now.clicked.connect(lambda : self.printer())
        self.exit_welcome.clicked.connect(lambda : self.stop())

        self.good_input = False

    def printer(self):
        if self.last_name.text() != '' and self.first_name.text() != '':

            last = self.last_name.text().strip()
            first = self.first_name.text().strip()
            middle = self.middle_initial.text().strip()
            dob = self.voter_dob.date()
            dob = dob.toPyDate()

            if not self.checker(last):
                self.clear_and_print_message(self.last_name, 'Last name is not alphabetic')
            elif not self.checker(first):
                self.clear_and_print_message(self.first_name, 'First name is not alphabetic')
            elif not self.checker(middle):
                self.clear_and_print_message(self.middle_initial, 'Middle initial is not alphabetic')
            else:
                self.good_input = True

            if self.good_input:
                name = [last, first, middle, dob]



                with open('election_results.csv', 'r', newline='') as results:
                    reader = csv.reader(results)
                    data = list(reader)
                if len(data) > 0:

                    last_match = self.check_last(name, data)
                    first_match = self.check_first(name, data)
                    dob_match = self.check_dob(name, data)

                    if last_match and first_match and dob_match:
                        self.clear_and_print_warning(self.last_name, self.first_name, self.middle_initial, f'{last}, {first} {middle} has already voted')

                    if not (last_match and first_match and dob_match):
                        with open('election_results.csv', 'a', newline='') as results:
                            writer = csv.writer(results)
                            writer.writerow(name)

                        self.next_window()
                else:
                    with open('election_results.csv', 'a', newline='') as results:
                        writer = csv.writer(results)
                        writer.writerow(name)
                    self.next_window()
    def checker(self, name):
        return name.isalpha()


    def clear_and_print_message(self, line_edit, message):
        line_edit.clear()
        QMessageBox.warning(self, "Invalid Input", message)

    def clear_and_print_warning(self, line_edit1, line_edit2, line_edit3, message):
        line_edit1.clear()
        line_edit2.clear()
        line_edit3.clear()
        self.voter_dob.setDate(QDate(2000, 1, 1))
        QMessageBox.warning(self, "Invalid Input", message)

    def check_last(self, name, data):
        for row in data:
            if row[0] == name[0]:
                return True
        return False

    def check_first(self, name, data):
        for row in data:
            if row[1] == name[1]:
                return True
        return False

    def check_dob(self, name, data):
        entered_dob = name[3]
        for row in data:
            csv_dob = datetime.strptime(row[3], '%Y-%m-%d').date()
            if entered_dob == csv_dob:
                return True

        return False

    def next_window(self):

            self.hide()
            self.w = FederalLogic()
            self.w.show()
    def clear(self):
        self.last_name.clear()
        self.first_name.clear()
        self.middle_initial.clear()

    def stop(self):
        quit()