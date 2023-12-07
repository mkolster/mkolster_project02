from PyQt6.QtWidgets import *
from federal_elections import *
from logic_state import StateLogic
import csv


class FederalLogic(QMainWindow, Ui_Voting_menu01):

    """
    Federal Logic runs federal voting menu window and associated buttons and links.
    """
    def __init__(self) -> None:
        """
        Initializes class and sends button to appropriate button.
        """
        super().__init__()
        self.setupUi(self)

        self.next_page.clicked.connect(lambda: self.federal_vote())

    def __check_radio(self) -> str:

        """
        Checks which radio button has been selected.
        :return: Candidate name in string
        """

        if self.alli_vote.isChecked():
            return 'Allison Ackers'
        elif self.cam_vote.isChecked():
            return 'Cameron Collins'
        elif self.diego_vote.isChecked():
            return 'Diego Donner'
        else:
            return ''

    def federal_vote(self) -> None:

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

        # Assigns very last value in data list to be location of federal vote. Checks which radio button was selected.

        new_value = self.__check_radio()

        if len(last_row) < 5:
            last_row.insert(4, new_value)
        else:
            last_row[4] = new_value

        data[-1] = last_row

        with open('election_results.csv', 'w', newline='') as results:
            writer = csv.writer(results)
            writer.writerows(data)

        results.close()

        self.__next_window()

        # Writes federal vote to csv file and continues to state vote window.

    def __next_window(self) -> None:

        """
        Calls state vote window.
        :return: None
        """

        self.hide()
        self.z = StateLogic()
        self.z.show()
