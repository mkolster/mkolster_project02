from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import *
from welcome_identification import *
import csv
from logic_federal import FederalLogic
from datetime import datetime


class Logic(QMainWindow, Ui_PyVote_welcome):
    """
    Logic class runs welcome window and associated line edits and buttons.
    """

    def __init__(self):
        """
        Initializes class variables and sends buttons to appropriate functions.
        """

        super().__init__()
        self.setupUi(self)

        self.vote_now.clicked.connect(lambda: self.__printer())
        self.exit_welcome.clicked.connect(lambda: self.stop())

        self.__good_input = False

    def __printer(self) -> None:

        """
        The main function responsible for calling functions to check input values. When all conditions are met,
        __printer opens the next page to display the federal vote menu.
        :return: None
        """

        if self.last_name.text() != '' and self.first_name.text() != '':

            # Checks text entry boxes to ensure that something is entered in both last name and first name.
            # Not all voters will have a middle name, so no need to check that.

            last = self.last_name.text().strip()
            first = self.first_name.text().strip()
            middle = self.middle_initial.text().strip()
            dob = self.voter_dob.date()
            dob = dob.toPyDate()

            # Assigns variables to strings from text entry boxes and strips spaces.
            # Date of Birth (dob) is converted into usable string from date box in PyQt.

            if not self.__checker(last):
                self.__clear_and_print_message(self.last_name, 'Last name is not alphabetic')
            if not self.__checker(first):
                self.__clear_and_print_message(self.first_name, 'First name is not alphabetic')
            if not self.__checker(middle):
                self.__clear_and_print_message(self.middle_initial, 'Middle initial is not alphabetic')
            else:
                self.__good_input = True

            # Checks for alphabetic entries and clears text box text if numbers or symbols are entered.
            # If so, __good_input is changed to "True".

            if self.__good_input:
                name = [last, first, middle, dob]

                with open('election_results.csv', 'r', newline='') as results:
                    reader = csv.reader(results)
                    data = list(reader)

                    # Data in the csv file is converted to a list to be able to manipulate the data and compare inputs.

                if len(data) > 0:

                    last_match = self.__check_last(name, data)
                    first_match = self.__check_first(name, data)
                    dob_match = self.__check_dob(name, data)

                    # Entries in the text boxes are compared to existing data in the csv file to ensure that voters
                    # cannot vote more than once. If an entry has the same last name, first name, and date of birth
                    # as an existing voter in the csv file, they will be restricted from voting. (Voters could have the
                    # same last name and first name but different dates of birth, and voters could have the same last
                    # and date of birth in the case of twins, but have different first names.) Only if all three match
                    # are they barred from voting. Assumes voter honesty.

                    if last_match and first_match and dob_match:
                        self.__clear_and_print_warning(self.last_name, self.first_name, self.middle_initial,
                                                       f'{last}, {first} {middle} has already voted')
                    else:
                        with open('election_results.csv', 'a', newline='') as results:
                            writer = csv.writer(results)
                            writer.writerow(name)

                        self.next_window()

                # The voter's last, first, middle initial, and dob are entered into the csv file and the next window is
                # called.
                else:
                    with open('election_results.csv', 'a', newline='') as results:
                        writer = csv.writer(results)
                        writer.writerow(name)
                    self.next_window()

    def __checker(self, name: str) -> bool:

        """
        Checks to see if the input name is all alphabetic.

        :param name: either voter's first or last name depending on which function call
        :return: True or False
        """

        return name.isalpha()

    def __clear_and_print_message(self, line_edit: str, message: str) -> None:

        """
        If strings contain non-alphabetic characters, line edits are cleared.

        :param line_edit: the line_edit that contains a number or symbol
        :param message: Message denoting which line edit has the invalid entry
        :return: None
        """

        line_edit.clear()
        QMessageBox.warning(self, "Invalid Input", message)

    def __clear_and_print_warning(self, line_edit1: QLineEdit,
                                  line_edit2: QLineEdit, line_edit3: QLineEdit, message: str) -> None:

        """
        If voter has already voted this clears the text_entries, resets the date to default, and shows a warning.

        :param line_edit1: last name text entry
        :param line_edit2: first name text entry
        :param line_edit3: middle initial text entry
        :param message: (name) has already voted
        :return: None
        """

        line_edit1.clear()
        line_edit2.clear()
        line_edit3.clear()
        self.voter_dob.setDate(QDate(2000, 1, 1))
        QMessageBox.warning(self, "Invalid Input", message)

    def __check_last(self, name: list, data: list) -> bool:
        """
        Checks last name against csv file.
        :param name: list containing last, first, middle, dob
        :param data: csv file contents converted to list
        :return: True or False
        """

        for row in data:
            if row[0] == name[0]:
                return True
        return False

    def __check_first(self, name: list, data: list) -> bool:
        """
        Checks first name against csv file.
        :param name:  list containing last, first, middle, dob
        :param data: csv file contents converted to list
        :return: True or False
        """

        for row in data:
            if row[1] == name[1]:
                return True
        return False

    def __check_dob(self, name: list, data: list) -> bool:
        """
        Checks date of birth against csv file.
        :param name:  list containing last, first, middle, dob
        :param data: csv file contents converted to list
        :return: True or False
        """

        entered_dob = name[3]
        for row in data:
            csv_dob = datetime.strptime(row[3], '%Y-%m-%d').date()
            if entered_dob == csv_dob:
                return True

        return False

    def next_window(self) -> None:
        """
        Opens federal voting menu
        :return: None
        """

        self.hide()
        self.w = FederalLogic()
        self.w.show()

    def clear(self) -> None:
        """
        Clear function called when voter has voted or name entry has forbidden characters.
        :return: None
        """

        self.last_name.clear()
        self.first_name.clear()
        self.middle_initial.clear()

    def stop(self) -> None:
        """
        Closes program.
        :return: None
        """
        quit()
