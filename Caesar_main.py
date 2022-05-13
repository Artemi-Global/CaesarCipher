from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QSettings
import sys

from Caesar_ui import Caesar_ui
from Caesar_logic import Caesar

class Caesar_MainWindow(QMainWindow, Caesar_ui):
    def __init__(self):
        super().__init__()
        self.setup_UI()
        self.Caesar = Caesar()

    def onTranslateClicked(self):
        message = self.textEdit_Input.toPlainText()
        offset = self.spin_offset.value()
        box_index = self.box_mode.currentIndex()

        translated_message = self.Caesar.modes[box_index](message, offset)
        self.textEdit_Output.setText(translated_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Caesar_MainWindow()
    window.show()
    sys.exit(app.exec_())
