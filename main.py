import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QCheckBox,
    QRadioButton, QVBoxLayout, QWidget, QButtonGroup
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

        # Setup the window and layout
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Checkboxes & Radio Buttons")

        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Connect checkbox
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        # Group radio buttons
        self.radio_group1.addButton(self.radio1)
        self.radio_group1.addButton(self.radio2)
        self.radio_group1.addButton(self.radio3)

        self.radio_group2.addButton(self.radio4)
        self.radio_group2.addButton(self.radio5)

        # Apply styling
        self.setStyleSheet("""
            QCheckBox, QRadioButton {
                font-size: 24px;
                font-family: Arial;
                padding: 10px;
            }
        """)

        # Add widgets to layout
        layout.addWidget(self.checkbox)
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        layout.addWidget(self.radio3)
        layout.addWidget(self.radio4)
        layout.addWidget(self.radio5)

        self.radio1.toggled.connect(self.radio_button_changed)
        self.radio2.toggled.connect(self.radio_button_changed)
        self.radio3.toggled.connect(self.radio_button_changed)
        self.radio4.toggled.connect(self.radio_button_changed)
        self.radio5.toggled.connect(self.radio_button_changed)

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


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
