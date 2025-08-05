import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QCheckBox,
    QRadioButton, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle("PyQt5 Checkboxes & Radio Buttons")

        # Create central widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout()

        # Create and style checkbox
        self.checkbox = QCheckBox("Do you like food?")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)

        # Create radio buttons
        self.radio1 = QRadioButton("Visa")
        self.radio2 = QRadioButton("Master Card")
        self.radio3 = QRadioButton("Gift Card")

        # Set style
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

        # Set layout on the central widget
        self.central_widget.setLayout(layout)

    def checkbox_changed(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You do not like food")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

