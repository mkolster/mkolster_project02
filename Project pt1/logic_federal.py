from PyQt6.QtWidgets import *
from federal_elections import *
from logic_state import StateLogic
import csv



class FederalLogic(QMainWindow, Ui_Voting_menu01):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.next_page.clicked.connect(lambda : self.federal_vote())

        # self.alli_vote.clicked.connect(lambda : self.alli())
        # self.cam_vote.clicked.connect(lambda : self.cam())
        # self.diego_vote.clicked.connect(lambda : self.diego())

    def check_radio(self):
        if self.alli_vote.isChecked():
            return 'Allison Ackers'
        elif self.cam_vote.isChecked():
            return 'Cameron Collins'
        elif self.diego_vote.isChecked():
            return 'Diego Donner'
        else:
            return ''

    def federal_vote(self):
        with open('election_results.csv', 'r', newline='') as results:
            reader = csv.reader(results)
            data = list(reader)  # Convert the reader object to a list

        # Check if there is any data in the file

        # Find the last row and append a value to the last position
        last_row_index = len(data) - 1
        last_row = data[last_row_index]

        # Append the new value to the last row
        new_value = self.check_radio()

        if len(last_row) < 5:
            last_row.insert(4, new_value)
        else:
            last_row[4] = new_value

        data[-1] = last_row


        # Write the modified data back to the CSV file
        with open('election_results.csv', 'w', newline='') as results:
            writer = csv.writer(results)
            writer.writerows(data)

        results.close()

        self.next_window()

    def next_window(self):

        self.hide()
        self.z = StateLogic()
        self.z.show()