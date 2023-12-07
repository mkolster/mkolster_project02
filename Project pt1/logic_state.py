import csv
from state_elections import *
from PyQt6.QtWidgets import *


class StateLogic(QMainWindow, Ui_State_Votes):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)

        self.next_page.clicked.connect(lambda: self.state_vote())

    def __check_radio(self) -> str:

        """
        Checks which radio button has been selected.
        :return: Candidate name in string
        """

        if self.leo_vote.isChecked():
            return 'Leonard Anderson'
        elif self.sarah_vote.isChecked():
            return 'Sarah Carlisle'
        elif self.jim_vote.isChecked():
            return 'James Seliman'
        else:
            return ''

    def state_vote(self) -> None:

        """
        Opens csv file and appends user's federal vote to existing user data from welcome menu. Moves to next window
        when all conditions are met.
        :return: None
        """

        with open('election_results.csv', 'r', newline='') as results:
            reader = csv.reader(results)
            data = list(reader)

        last_row_index = len(data) - 1
        last_row = data[last_row_index]

        new_value = self.__check_radio()

        # Assigns very last value in data list to be location of federal vote. Checks which radio button was selected.

        if len(last_row) < 6:
            last_row.insert(5, new_value)
        else:
            last_row[5] = new_value

        data[-1] = last_row

        # Writes federal vote to csv file and continues to state vote window.

        with open('election_results.csv', 'w', newline='') as results:
            writer = csv.writer(results)
            writer.writerows(data)

        results.close()

        self.__closer()

    def __closer(self) -> None:
        """
        Closes the program.
        :return: None
        """

        quit()
