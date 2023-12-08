from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication,
                            QMainWindow,
                            QPushButton,
                            QLabel, 
                            QLineEdit, 
                            QVBoxLayout, 
                            QWidget)


import sys

def is_cbs(seq):
    stack = []
    for i in seq:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        return True
    return False
                
def need_to_move(seq):
    stack = []
    for i in seq:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == '(' and i == ')':
                stack.pop()
            else:
                stack.append(i)
    a = stack.count('(')
    b = stack.count(')')
    return max(a,b)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: gray;")
        self.setWindowTitle("CBSCheck v1 (GUI EDITION GOTY 20002)")

        self.setFixedSize(QSize(800, 640))

        self.helpText = QLabel()
        self.helpText.setText("To use the program:"
            "\nInput the brace sequence in the field below and press enter or the check button.")
        self.helpText.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.label = QLabel()

        self.button = QPushButton()
        self.button.setText("check")

        self.input = QLineEdit()
        self.input.textChanged

        layout = QVBoxLayout()

        layout.addWidget(self.helpText,0,Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.input,0,Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.label,1,Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        layout.addWidget(self.button,1, Qt.AlignmentFlag.AlignBottom)

        self.button.clicked.connect(self.get_result)

        self.input.returnPressed.connect(self.get_result)
        
        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def get_result(self):
        self.label.setText(str(is_cbs(self.input.text())))

program = QApplication(sys.argv)

window = MainWindow()
window.show()

program.exec()
