import csv
from state_elections import *
from PyQt6.QtWidgets import *

class StateLogic(QMainWindow, Ui_State_Votes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.next_page.clicked.connect(lambda: self.state_vote())

        # self.alli_vote.clicked.connect(lambda : self.alli())
        # self.cam_vote.clicked.connect(lambda : self.cam())
        # self.diego_vote.clicked.connect(lambda : self.diego())

    def check_radio(self):
        if self.leo_vote.isChecked():
            return 'Leonard Anderson'
        elif self.sarah_vote.isChecked():
            return 'Sarah Carlisle'
        elif self.jim_vote.isChecked():
            return 'James Seliman'
        else:
            return ''

    def state_vote(self):
        with open('election_results.csv', 'r', newline='') as results:
            reader = csv.reader(results)
            data = list(reader)  # Convert the reader object to a list

        # Check if there is any data in the file

        # Find the last row and append a value to the last position
        last_row_index = len(data) - 1
        last_row = data[last_row_index]

        # Append the new value to the last row
        new_value = self.check_radio()

        if len(last_row) < 6:
            last_row.insert(5, new_value)
        else:
            last_row[5] = new_value

        data[-1] = last_row


        # Write the modified data back to the CSV file
        with open('election_results.csv', 'w', newline='') as results:
            writer = csv.writer(results)
            writer.writerows(data)

        results.close()

        self.closer()

    def closer(self):
        quit()
