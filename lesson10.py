import sys
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 OOP Template")
        self.resize(300, 150)

        self.count = 0
        mainlayout = QHBoxLayout()
        welcomeLbl = QLabel("Welcome to my APP")
        welcomeBtn = QPushButton("Click to Start")
        welcomeBtn.setStyleSheet("background-color: #456289")
        self.numberLbl = QLabel("0")
        plusBtn = QPushButton("+")

        plusBtn.clicked.connect(self.increase)
        minusBtn = QPushButton("-")
        minusBtn.clicked.connect(self.decrease)

        mainlayout.addWidget(welcomeLbl)
        mainlayout.addWidget(welcomeBtn)
        mainlayout.addWidget(plusBtn)
        mainlayout.addWidget(self.numberLbl)
        mainlayout.addWidget(minusBtn)

        self.setLayout(mainlayout)

    def increase(self):
        self.count += 1
        self.numberLbl.setText(str(self.count))

    def decrease(self):
        self.count -= 1
        self.numberLbl.setText(str(self.count))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())