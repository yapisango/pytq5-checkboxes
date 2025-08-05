import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QCheckBox,
    QRadioButton, QVBoxLayout, QWidget,
    QButtonGroup, QLineEdit, QPushButton
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create widgets (but don't configure them yet)
        self.central_widget = QWidget()

        self.checkbox = QCheckBox("Do you like food?")

        self.radio1 = QRadioButton("Visa")
        self.radio2 = QRadioButton("Master Card")
        self.radio3 = QRadioButton("Gift Card")
        self.radio4 = QRadioButton("In-Store")
        self.radio5 = QRadioButton("Online")

        self.radio_group1 = QButtonGroup()
        self.radio_group2 = QButtonGroup()

        self.qline_edit = QLineEdit(self)

        self.button = QPushButton("Submit", self)
        self.button1 = QPushButton("#1", self)
        self.button2 = QPushButton("#2", self)
        self.button3 = QPushButton("#3", self)

        # Setup the window and layout
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Checkboxes & Radio Buttons")

        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Connect checkbox
        self.checkbox.setChecked(False)

        # Group radio buttons
        self.radio_group1.addButton(self.radio1)
        self.radio_group1.addButton(self.radio2)
        self.radio_group1.addButton(self.radio3)

        self.radio_group2.addButton(self.radio4)
        self.radio_group2.addButton(self.radio5)

        self.qline_edit.setGeometry(210, 10, 200, 40)
        self.qline_edit.setPlaceholderText("Enter your name")

        self.button.setGeometry(210, 10, 200, 40)

        self.button.setObjectName("button")
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        # Apply unified style
        self.setStyleSheet("""
            QCheckBox, QRadioButton{
                font-size: 24px;
                font-family: Arial;
                padding: 10px;
            }
            QLineEdit{
                font-size: 24px;
                font-family: Arial;
                padding: 10px;
            }
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid blue;
                border-radius: 15px;
            }
            QPushButton#button{
                background-color: green;
            }
            QPushButton#button1{
                background-color: blue;
            }
            QPushButton#button2{
                background-color: yellow;
            }
            QPushButton#button3{
                background-color: red;
            }
        """)

        # Add widgets to layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(self.radio5)
        layout.addWidget(self.qline_edit)
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        self.checkbox.stateChanged.connect(self.checkbox_changed)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

        self.button.clicked.connect(self.submit)
        self.button1.clicked.connect(self.submit)
        self.button2.clicked.connect(self.submit)
        self.button3.clicked.connect(self.submit)

        self.central_widget.setLayout(layout)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")

    def radio_button_changed(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

    def submit(self):
        text = self.qline_edit.text()
        print(f"Hello {text}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
